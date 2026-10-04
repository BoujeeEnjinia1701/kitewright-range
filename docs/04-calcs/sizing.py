"""Kitewright Range sizing calculations (KWR-CAL-001).

Run from the repo root:  python docs/04-calcs/sizing.py
Reads the geometry from cad/src/model.py, works out the mass and balance from the part volumes
and the bought-part masses, then the aerodynamics, hover, energy, structure and cost, and writes
docs/04-calcs/results.csv. Every assumption is stated in ASSUMPTIONS below and in 01-sizing.md.
"""
from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "cad" / "src"))
from model import PARAMS as P, BOUGHT_MASS, build_parts, derived, surface_z  # noqa: E402

G = 9.81
A = {  # assumptions
    "rho_5000": 0.736,          # kg/m3, ISA at 5,000 m (requirement R1 uses 0.74)
    "rho_sl": 1.225,
    "mu_5000": 1.63e-5,         # Pa s at about -17 C
    "foam": 30.0,               # kg/m3, XPS
    "skin_wing": 0.22,          # kg/m2 of wetted area: 80 g/m2 glass, epoxy, primer
    "skin_tail": 0.18,
    "ply": 520.0,               # kg/m3, mix of 3 mm poplar lite-ply (450) and 6 mm birch ply (680) in the box
    "lite_ply": 450.0,          # kg/m3, poplar lite-ply hatch
    "birch": 680.0,             # kg/m3, 6 mm birch aircraft plywood (Core deck doubler, decision 10A)
    "fus_skin": 0.20,           # kg/m2 glass on the fuselage outside
    "carbon": 1550.0,           # kg/m3
    # printed parts: (wall thickness mm, infill fraction, material density kg/m3)
    "print": {"nose": (1.6, 0.10, 1070.0), "socket": (2.4, 0.30, 1070.0), "pylon": (1.2, 0.10, 1070.0),
              "caps": (2.0, 1.00, 1070.0), "legclamps": (2.0, 0.40, 1070.0), "legfair": (0.8, 0.0, 1070.0),
              "tail_mount": (1.6, 0.20, 1070.0), "feet": (1.6, 0.30, 1200.0)},
    "clmax": 1.30,              # wing with plain ailerons, Re about 3e5
    "e": 0.75,                  # Oswald factor with booms and pylons
    "cf": 0.0060, "ff_wing": 1.25, "ff_tail": 1.20, "interference": 1.15,
    "eta_prop_cruise": 0.65, "eta_drive_cruise": 0.85,
    "fm": 0.65, "eta_drive_hover": 0.82,
    "lift_thrust_sl_n": 68.7,   # 7.0 kgf maker static thrust per motor, 5215 class, 22 x 7 in, 6S, sea level (KWR-DDR-003)
    "cell_wh": 5.0 * 3.6, "cells_per_pack": 18, "packs": 2,   # 21700 cells of 5.0 Ah (KWR-DDR-003)
    "usable_frac": 0.90, "cold_frac": 0.95, "reserve": 0.20,
    "p_systems_w": 38.0,        # avionics 15, payload 10, pack heaters in flight 10, servos 3
    "vtol_s": 125.0, "vtol_spike": 1.20, "climb_m": 400.0, "climb_ms": 2.5,
    "n_limit": 2.5,             # limit load factor in cruise (gusts and turns)
    "sigma_carbon_mpa": 600.0,  # allowable bending stress, pultruded or roll-wrapped carbon tube
    "payload_kg": 1.0,
}


def vol_m3(s):
    return s.volume / 1e9


def area_m2(s):
    return s.area / 1e6


def centroid_x(s):
    from build123d import Compound
    try:
        return s.center().X
    except Exception:
        return Compound([s]).center().X


def masses(m, packs=None, cell_mass=None, airframe_factor=1.0):
    """Return a list of (name, kg, x_mm) for every item, made parts from volumes."""
    out = []
    for k, s in m.items():
        base = k.rsplit("_", 1)[0] if k[-2:] in ("_l", "_r") else k
        if base == "fus":
            kg = vol_m3(s) * A["ply"] + 0.35 * A["fus_skin"]        # 0.35 m2 of glass outside the 156 mm box (0.33 at 140 mm)
        elif base == "core_deck":
            kg = vol_m3(s) * A["birch"]
        elif base == "hatch":
            kg = vol_m3(s) * A["lite_ply"]
        elif base in ("wing", "ail"):
            kg = vol_m3(s) * A["foam"] + area_m2(s) * A["skin_wing"]
            if base == "wing":
                kg += 0.035   # root rib, two hardpoints, conduit
        elif base in ("stab", "fin"):
            kg = vol_m3(s) * A["foam"] + area_m2(s) * A["skin_tail"]
        elif base in ("spar", "joiner", "boom", "tail_boom", "legrods"):
            kg = vol_m3(s) * A["carbon"]
        elif base in A["print"]:
            wall, infill, rho = A["print"][base]
            shell = min(area_m2(s) * wall / 1000, vol_m3(s))
            kg = (shell + (vol_m3(s) - shell) * infill) * rho
        elif base == "packs":
            n = len(list(s.solids()))
            kg = n * (packs if packs else BOUGHT_MASS["packs"])
        elif base == "pbolts":
            kg = 2 * BOUGHT_MASS["pbolts"]
        elif base in ("mounts", "escs", "motors", "props"):
            kg = 2 * BOUGHT_MASS[base]
        elif base in BOUGHT_MASS:
            kg = BOUGHT_MASS[base]
        else:
            raise KeyError(k)
        if base in ("fus", "hatch", "wing", "ail", "stab", "fin"):
            kg *= airframe_factor
        out.append((k, kg, centroid_x(s)))
    D = derived(P)
    out.append(("harness", BOUGHT_MASS["harness"], D["x_cg"]))
    out.append(("servos, ailerons", 2 * BOUGHT_MASS["servos"], P["spar_x"] + 120))
    out.append(("servos, tail", 2 * BOUGHT_MASS["servos"], P["stab_le"] + 40))
    out.append(("cruise ESC", BOUGHT_MASS["cruise_esc"], 30.0))
    out.append(("Core power leads", BOUGHT_MASS["core_leads"], D["x_cg"] - 100.0))   # to the Core's rear grommets
    out.append(("Antenna extension leads", BOUGHT_MASS["ant_leads"], P["gnss_x"]))
    return out


def aero(mass, D, rho=A["rho_5000"], extra_cda=0.0):
    S = D["wing_area_m2"]
    W = mass * G
    # drag areas CdA (m2), each with its basis
    cda = {
        "fuselage and nose (frontal, Cd 0.35)": P["fus_w"] / 1000 * P["fus_h"] / 1000 * 0.35,
        "wing (wetted 2.05 S, Cf, form factor)": 2.05 * S * A["cf"] * A["ff_wing"],
        "tail surfaces (wetted 2.05 S)": 2.05 * (D["stab_area_m2"] + D["fin_area_m2"]) * A["cf"] * A["ff_tail"],
        "booms (wetted, Cf)": 2 * math.pi * 0.025 * D["boom_len"] / 1000 * 2 * A["cf"],
        "pylons (frontal, Cd 0.30)": 2 * 0.044 * 0.090 * 0.30,
        "lift motors, mounts, ESCs (frontal, Cd 0.8)": 4 * (P["lift_motor_d"] / 1000 * P["lift_motor_h"] / 1000 + 0.040 * 0.045) * 0.8,
        "stopped lift propellers and hubs": 4 * (0.030 * 0.010 + 0.036 * 0.006) * 1.0,
        "leg fairings and feet": 4 * (0.016 * 0.143 * 0.25 + 0.036 * 0.010 * 0.8),
        "payload (Cd 0.4 on 0.0088 m2)": P["payload"][1] / 1000 * P["payload"][2] / 1000 * 0.40,
        "Core underside: plate, rail, shoe (0.150 x 0.024 m, Cd 0.5) and two pin knobs": 0.150 * 0.024 * 0.5 + 2 * 0.018 * 0.024 * 1.0,
        "GNSS mast, pitot": 0.0006,
        "tail boom (wetted, Cf)": math.pi * 0.020 * 0.85 * A["cf"],
    }
    cda_total = (sum(cda.values()) + extra_cda) * A["interference"]
    cd0 = cda_total / S
    k = 1 / (math.pi * A["e"] * D["aspect_ratio"])
    vs = math.sqrt(2 * W / (rho * S * A["clmax"]))
    best = None
    for i in range(0, 400):
        v = 1.25 * vs + i * 0.05
        cl = 2 * W / (rho * S * v * v)
        cd = cd0 + k * cl * cl
        p = 0.5 * rho * v ** 3 * S * cd
        if best is None or p < best[2]:
            best = (v, cl, p, cl / cd)
    v, cl, p_aero, ld = best
    eta = A["eta_prop_cruise"] * A["eta_drive_cruise"]
    p_elec = p_aero / eta + A["p_systems_w"]
    return dict(cda=cda, cda_total=cda_total, cd0=cd0, k=k, vs=vs, v=v, cl=cl, ld=ld, p_aero=p_aero,
                p_elec=p_elec, eta=eta, wl=W / S)


def hover(mass, D, rho=A["rho_5000"], thrust_sl=None, prop_d=None):
    T = mass * G
    disc = D["lift_disc_area_m2"] if prop_d is None else 4 * math.pi * (prop_d / 2) ** 2
    p_ideal = T ** 1.5 / math.sqrt(2 * rho * disc)
    p_elec = p_ideal / A["fm"] / A["eta_drive_hover"]
    t_max = 4 * (thrust_sl or A["lift_thrust_sl_n"]) * rho / A["rho_sl"]
    return dict(T=T, disc=disc, p_ideal=p_ideal, p_elec=p_elec, t_max=t_max, margin=t_max / T - 1,
                disc_loading=T / disc, sl_throttle_thrust=T / (4 * A["lift_thrust_sl_n"]),
                current_a=p_elec / 21.6)


def energy(mass, D, pack_wh, n_packs, thrust_sl=None, prop_d=None, extra_cda=0.0):
    a = aero(mass, D, extra_cda=extra_cda)
    h = hover(mass, D, thrust_sl=thrust_sl, prop_d=prop_d)
    nominal = pack_wh * n_packs
    usable = nominal * A["usable_frac"] * A["cold_frac"]
    available = usable * (1 - A["reserve"])
    e_vtol = h["p_elec"] * A["vtol_s"] / 3600 * A["vtol_spike"]
    t_climb = A["climb_m"] / A["climb_ms"]
    e_climb = mass * G * A["climb_ms"] / a["eta"] * t_climb / 3600
    cruise_wh = available - e_vtol - e_climb
    t_min = cruise_wh / a["p_elec"] * 60
    rng_km = a["v"] * t_min * 60 / 1000
    return dict(nominal=nominal, usable=usable, available=available, e_vtol=e_vtol, e_climb=e_climb,
                cruise_wh=cruise_wh, endurance_min=t_min, range_km=rng_km, aero=a, hover=h)


def structure(mass, D):
    """Bending checks at the limit load with the carbon allowable (safety factor = allowable / stress)."""
    def z_mod(od, idia):
        return math.pi * (od ** 4 - idia ** 4) / (32 * od)
    W = mass * G
    n = A["n_limit"]
    half_lift = n * W / 2                                      # N per panel
    y_c = (D["span"] / 2 - P["fus_w"] / 2) * 0.45 / 1000       # m from the root to the panel lift centroid
    m_root = half_lift * y_c                                   # N m at the root rib
    sp = m_root * 1000 / z_mod(P["spar_od"], P["spar_id"])
    jn = m_root * 1000 / z_mod(P["joiner_od"], P["joiner_id"])
    t_motor = A["lift_thrust_sl_n"] * A["rho_5000"] / A["rho_sl"]   # full thrust at altitude
    t_motor_sl = A["lift_thrust_sl_n"]                               # worst case: full thrust at sea level
    arm = (P["motor_half_span"] - (P["pylon_x"][1] - P["pylon_x"][0]) / 2) / 1000
    m_boom = t_motor_sl * arm
    bm = m_boom * 1000 / z_mod(P["boom_od"], P["boom_id"])
    # tail boom: stabiliser download in a 2.5 g pull-up, taken as 15 % of weight at the tail arm
    m_tail = 0.15 * n * W * D["tail_arm"] / 1000
    tb = m_tail * 1000 / z_mod(P["tail_boom_od"], P["tail_boom_id"])
    # pylon bolts: two M5 per pylon carry both motors' sea-level thrust plus the nose-down moment
    f_bolt = (2 * t_motor_sl) / 2 + m_boom * 0 / 1
    m_pitch = t_motor_sl * (P["motor_half_span"] / 1000)      # one motor at full thrust, the other off
    f_bolt_max = f_bolt + m_pitch / ((P["pylon_bolts_x"][1] - P["pylon_bolts_x"][0]) / 1000)
    return dict(m_root=m_root, spar_mpa=sp, joiner_mpa=jn, boom_nm=m_boom, boom_mpa=bm, tail_nm=m_tail,
                tail_mpa=tb, sf_spar=A["sigma_carbon_mpa"] / sp, sf_joiner=A["sigma_carbon_mpa"] / jn,
                sf_boom=A["sigma_carbon_mpa"] / bm, sf_tail=A["sigma_carbon_mpa"] / tb, bolt_n=f_bolt_max,
                bolt_sf=4300 / f_bolt_max, t_motor_alt=t_motor)


def bom_cost():
    total = 0.0
    rows = list(csv.DictReader(open(ROOT / "bom" / "bom.csv")))
    for r in rows:
        total += float(r["qty"]) * float(r["unit_cost_usd"])
    return total, rows


def main(verbose=True):
    D = derived(P)
    m = build_parts(P)
    items = masses(m)
    mtow = sum(kg for _, kg, _ in items)
    x_cg = sum(kg * x for _, kg, x in items) / mtow
    empty = mtow - A["payload_kg"]
    pack_wh = A["cell_wh"] * A["cells_per_pack"]
    E = energy(mtow, D, pack_wh, A["packs"])
    S = structure(mtow, D)
    cost, _ = bom_cost()
    a, h = E["aero"], E["hover"]

    # further options for R2 and R7 after the 2026-10-03 decisions (same geometry, mass and energy changed)
    opt = {}
    pk = BOUGHT_MASS["packs"]
    opt["B: two 6S4P packs of 5.0 Ah cells"] = (mtow + 2 * 0.44, pack_wh * 4 / 3, 2, 2 * 120.0)
    lite = sum(kg for _, kg, _ in masses(m, airframe_factor=0.65)) - (sum(kg for _, kg, _ in items) - mtow)
    opt["E: moulded carbon airframe"] = (lite, pack_wh, 2, 1200.0)
    opt["F: moulded carbon airframe and two 6S4P packs"] = (lite + 2 * 0.44, pack_wh * 4 / 3, 2, 1200.0 + 240.0)
    opt_res = {}
    for name, vals in opt.items():
        mm, wh, n, dc = vals[:4]
        ts, pd, xc = (vals[4:] + (None, None, 0.0))[:3] if len(vals) > 4 else (None, None, 0.0)
        e = energy(mm, D, wh, n, thrust_sl=ts, prop_d=pd, extra_cda=xc)
        opt_res[name] = dict(mass=mm, endurance=e["endurance_min"], range=e["range_km"], margin=e["hover"]["margin"],
                             cost=cost + dc, dcost=dc, dmass=mm - mtow)

    R = {
        "mtow_kg": mtow, "empty_kg": empty, "x_cg_mm": x_cg, "x_cg_target_mm": D["x_cg"],
        "cg_frac_mac": (x_cg - D["x_le_mac"]) / D["mac"],
        "span_m": D["span"] / 1000, "wing_area_m2": D["wing_area_m2"], "aspect_ratio": D["aspect_ratio"],
        "wing_loading_n_m2": a["wl"], "cd0": a["cd0"], "cda_m2": a["cda_total"], "ld_cruise": a["ld"],
        "v_stall_ms": a["vs"], "v_cruise_ms": a["v"], "cl_cruise": a["cl"], "p_cruise_aero_w": a["p_aero"],
        "p_cruise_elec_w": a["p_elec"], "hover_power_w": h["p_elec"], "hover_current_a": h["current_a"],
        "disc_loading_n_m2": h["disc_loading"], "thrust_max_5000_n": h["t_max"], "hover_margin": h["margin"],
        "sl_hover_thrust_frac": h["sl_throttle_thrust"],
        "pack_wh": pack_wh, "nominal_wh": E["nominal"], "usable_wh": E["usable"], "available_wh": E["available"],
        "e_vtol_wh": E["e_vtol"], "e_climb_wh": E["e_climb"], "cruise_wh": E["cruise_wh"],
        "endurance_min": E["endurance_min"], "range_km": E["range_km"],
        "spar_sf": S["sf_spar"], "joiner_sf": S["sf_joiner"], "boom_sf": S["sf_boom"], "tail_sf": S["sf_tail"],
        "root_moment_nm": S["m_root"], "boom_moment_nm": S["boom_nm"], "pylon_bolt_n": S["bolt_n"],
        "pylon_bolt_sf": S["bolt_sf"],
        "disc_below_wing_top_mm": D["disc_below_wing_top"], "lift_cruise_disc_gap_mm": D["lift_to_cruise_disc_y"],
        "rear_disc_to_te_mm": D["rear_disc_to_te"], "vh": D["vh"], "vv": D["vv"],
        "boom_len_mm": D["boom_len"], "panel_len_mm": P["panel_span"] + 25,
        "cost_usd": cost, "cost_vs_target_usd": cost - 5000.0,
        "pack_current_a_per_cell": h["current_a"] / (A["packs"] * 3),
    }
    with open(ROOT / "docs" / "04-calcs" / "results.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["quantity", "value"])
        for k, v in R.items():
            w.writerow([k, f"{v:.4g}"])
        for name, o in opt_res.items():
            for k, v in o.items():
                w.writerow([f"option {name}: {k}", f"{v:.4g}"])
    if verbose:
        for k, v in R.items():
            print(f"{k:28s} {v:10.4g}")
        print("\nmass breakdown (kg):")
        for n, kg, x in sorted(items, key=lambda t: -t[1]):
            print(f"  {n:22s} {kg:6.3f}  x={x:7.1f}")
        print("\ndrag areas (m2):")
        for n, v in a["cda"].items():
            print(f"  {n:48s} {v:.5f}")
        print("\noptions:")
        for n, o in opt_res.items():
            print(f"  {n:44s} " + " ".join(f"{k}={v:.3g}" for k, v in o.items()))
    return R, opt_res, items


if __name__ == "__main__":
    main()
