"""Kitewright Range parametric model (build123d), TRL 3, constructable design (KWR-DDR-002, KWR-DDR-003).

Run from the repo root:  python cad/src/model.py
Builds every component of the all-electric quadplane from PARAMS, runs the constructability
checks (no overlaps, nothing floating, design-around geometry, transport lengths) and exports
STEP and STL files to cad/step and cad/stl.

Axes and units: millimetres. X runs from the nose (firewall at x = 0) toward the tail, Y is to
the right wing (+Y is the right wing seen from behind), Z is up with the ground at z = 0 when the
aircraft stands on its landing feet. The wing spar line is straight at 30 % chord.

The Kitewright Core hangs under the fuselage floor at the centre of gravity to the family envelope
(core_envelope.py, the Kitewright interface table of 2026-10-04, decision 10A): four M4 hard points on a
220 x 130 mm pattern in a 6 mm birch doubler on the floor, its lid up through a 200 x 112 mm opening, its
rail and payload shoe under the fuselage. The Core's GNSS receiver rides the hatch mast and its antennas
go to the hatch on extension leads.

PRELIMINARY, NOT FOR FABRICATION. Every size here is a TRL 3 design figure; bought parts are
envelopes of a specification, not of a named product.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

from build123d import (Box, Compound, Cylinder, Face, Line, Location, Plane, Polyline, Pos, Rot, Solid,
                       Spline, Wire, export_step, export_stl, extrude, loft, make_face)

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import core_envelope as CE  # noqa: E402

PARAMS = {
    # fuselage box (3 mm birch ply, glass cloth outside)
    "fus_len": 750.0, "fus_w": 156.0, "fus_h": 150.0, "fus_z0": 195.0, "ply": 3.0, "ply_thick": 6.0,   # 156 wide: 150 inside for the Core (decision 10A; was 140)
    "bulkheads": (252.0, 645.0),            # x of the two inner bulkheads (front faces); rear one moved aft from 585 for the rear pack (10A)
    "doubler_x": (380.0, 580.0), "doubler_z": (290.0, 342.0),
    "hatch_t": 3.0,
    # nose cone and cruise drive
    "nose_len": 55.0, "nose_tip_d": 60.0, "cruise_motor_d": 46.0, "cruise_motor_l": 38.0,
    "cruise_prop_d": 356.0,                 # 14 in folding propeller
    "thrust_line_z": 270.0,
    # wing (NACA 2412, straight spar at 30 % chord, no sweep of the spar line, no dihedral)
    "root_chord": 310.0, "tip_chord": 250.0, "panel_span": 1180.0, "spar_x": 420.0, "chord_z": 320.0,
    "spar_z": 325.0, "spar_od": 22.0, "spar_id": 20.0, "joiner_od": 20.0, "joiner_id": 16.0, "joiner_len": 640.0,
    "aileron_y": (700.0, 1230.0), "hinge_frac": 0.75,
    "wing_bolt_x": 544.0, "wing_bolt_z": 324.0,
    # lift system
    "boom_y": 490.0, "boom_z": 205.0, "boom_od": 25.0, "boom_id": 23.0, "motor_half_span": 531.0,
    "boom_overhang": 40.0,
    "pylon_x": (350.0, 510.0), "pylon_w": 44.0, "pylon_bolts_x": (380.0, 480.0),
    "clamp_x": ((352.0, 378.0), (482.0, 508.0)), "clamp_t": 6.0,
    "lift_motor_d": 62.0, "lift_motor_h": 36.0, "mount_h": 20.0, "lift_prop_d": 558.8,   # 22 in propellers on 5215-class motors (KWR-DDR-003)
    "leg_inset": 70.0, "leg_rod_d": 12.0, "foot_d": 36.0, "leg_fair": (32.0, 16.0),
    # tail
    "tail_boom_od": 20.0, "tail_boom_id": 17.0, "tail_boom_x": (650.0, 1500.0), "tail_z": 300.0,
    "stab_chord": 170.0, "stab_span": 640.0, "stab_le": 1335.0, "stab_z": 326.0,
    "fin_root": 170.0, "fin_tip": 130.0, "fin_h": 300.0,
    # bays and the Kitewright Core to the family envelope (core_envelope.py, decision 10A)
    "pack": (138.0, 75.0, 82.0), "pack_x": (60.0, 506.0),   # front pack in the nose bay, rear pack behind the Core lid (10A)
    "core_deck": (300.0, 6.0),                # birch doubler on the floor carrying the Core's four M4 hard points: length, thickness
    "payload": (140.0, 88.0, 100.0),          # payload body under its shoe: inside the Core's 88 mm neck and clear of its pigtail plug
    "gnss_x": 660.0, "gnss_mast": 120.0,
    "pitot_y": -800.0,
    # rules
    "x_cg_frac": 0.28,                      # target centre of gravity, fraction of the mean chord
    "disc_clear_min": 70.0,                 # rotor discs at least this far below the wing-top plane
    "case_len": 1300.0,                     # longest transport case
}


# ----------------------------------------------------------------------------- derived figures
def chord(y, P=PARAMS):
    t = (abs(y) - P["fus_w"] / 2) / P["panel_span"]
    return P["root_chord"] + (P["tip_chord"] - P["root_chord"]) * min(max(t, 0.0), 1.0)


def le_x(y, P=PARAMS):
    return P["spar_x"] - 0.3 * chord(y, P)


def naca(xc, t=0.12, m=0.02, p=0.4):
    """Upper and lower surface heights (fractions of chord) of a NACA 4-digit section at xc."""
    yt = 5 * t * (0.2969 * math.sqrt(xc) - 0.1260 * xc - 0.3516 * xc ** 2 + 0.2843 * xc ** 3 - 0.1015 * xc ** 4)
    if m == 0:
        return yt, -yt
    yc = m / p ** 2 * (2 * p * xc - xc ** 2) if xc < p else m / (1 - p) ** 2 * ((1 - 2 * p) + 2 * p * xc - xc ** 2)
    return yc + yt, yc - yt


def surface_z(x, y, upper=True, P=PARAMS):
    c = chord(y, P)
    xc = (x - le_x(y, P)) / c
    u, l = naca(min(max(xc, 0.0), 1.0))
    return P["chord_z"] + (u if upper else l) * c


def derived(P=PARAMS):
    D = {}
    cr, ct = P["root_chord"], P["tip_chord"]
    lam = ct / cr
    D["span"] = 2 * P["panel_span"] + P["fus_w"]
    D["wing_area_m2"] = (2 * P["panel_span"] * (cr + ct) / 2 + P["fus_w"] * cr) / 1e6
    D["mac"] = 2 / 3 * cr * (1 + lam + lam ** 2) / (1 + lam)
    D["y_mac"] = P["fus_w"] / 2 + P["panel_span"] / 3 * (1 + 2 * lam) / (1 + lam)
    D["x_le_mac"] = P["spar_x"] - 0.3 * D["mac"]
    D["x_cg"] = round(D["x_le_mac"] + P["x_cg_frac"] * D["mac"], 1)
    D["aspect_ratio"] = D["span"] ** 2 / (D["wing_area_m2"] * 1e6)
    D["motor_x"] = (D["x_cg"] - P["motor_half_span"], D["x_cg"] + P["motor_half_span"])
    D["boom_x"] = (D["motor_x"][0] - P["boom_overhang"], D["motor_x"][1] + P["boom_overhang"])
    D["boom_len"] = D["boom_x"][1] - D["boom_x"][0]
    D["mount_top"] = P["boom_z"] + P["mount_h"]
    D["motor_top"] = D["mount_top"] + P["lift_motor_h"]
    D["disc_z"] = D["motor_top"] + 5.0                     # propeller blade mid-plane
    yb = P["boom_y"]
    D["wing_top_at_boom"] = max(surface_z(le_x(yb, P) + f * chord(yb, P), yb, True, P) for f in [i / 50 for i in range(51)])
    D["disc_below_wing_top"] = D["wing_top_at_boom"] - D["disc_z"]
    D["front_disc_to_le"] = le_x(yb, P) - (D["motor_x"][0] + P["lift_prop_d"] / 2)
    D["rear_disc_to_te"] = (D["motor_x"][1] - P["lift_prop_d"] / 2) - (le_x(yb, P) + chord(yb, P))
    # lift disc against the cruise propeller disc (vertical plane at the cruise propeller)
    xp = -P["nose_len"] - P["cruise_motor_l"] - 12.0
    dx = abs(xp - D["motor_x"][0])
    half = math.sqrt(max((P["lift_prop_d"] / 2) ** 2 - dx ** 2, 0.0))
    D["cruise_prop_x"] = xp
    D["lift_to_cruise_disc_y"] = (yb - half) - P["cruise_prop_d"] / 2
    D["rear_disc_to_stab"] = P["stab_le"] - (D["motor_x"][1] + P["lift_prop_d"] / 2)
    D["lift_disc_to_fus"] = yb - P["lift_prop_d"] / 2 - P["fus_w"] / 2
    D["leg_x"] = (D["motor_x"][0] + P["leg_inset"], D["motor_x"][1] - P["leg_inset"])
    D["leg_top"] = P["boom_z"] - P["boom_od"] / 2
    D["core_z"] = P["fus_z0"] - CE.CORE["spacer"][2]          # Core plate top: the floor underside is its deck
    D["shoe_bot"] = D["core_z"] + CE.CORE["shoe"][3]
    D["ground_to_payload"] = D["shoe_bot"] - P["payload"][2]
    D["ground_to_core_knobs"] = D["core_z"] + CE.CORE["knob"][1]
    D["ground_to_cruise_tip"] = P["thrust_line_z"] - P["cruise_prop_d"] / 2
    D["tail_arm"] = P["stab_le"] + 0.25 * P["stab_chord"] - (D["x_le_mac"] + 0.25 * D["mac"])
    D["stab_area_m2"] = P["stab_chord"] * P["stab_span"] / 1e6
    D["fin_area_m2"] = (P["fin_root"] + P["fin_tip"]) / 2 * P["fin_h"] / 1e6
    D["vh"] = D["stab_area_m2"] * D["tail_arm"] / (D["wing_area_m2"] * D["mac"])
    D["vv"] = D["fin_area_m2"] * D["tail_arm"] / (D["wing_area_m2"] * D["span"])
    D["lift_disc_area_m2"] = 4 * math.pi * (P["lift_prop_d"] / 2000) ** 2
    D["overall_len"] = P["tail_boom_x"][1] + 10 - D["cruise_prop_x"]
    D["fin_top"] = P["stab_z"] + 0.05 * P["stab_chord"] + P["fin_h"]
    return D


# ----------------------------------------------------------------------------- geometry helpers
def _airfoil_face(c, x_le, y, z0, t=0.12, m=0.02, n=36):
    xs = [0.5 * (1 - math.cos(math.pi * i / n)) for i in range(n + 1)]   # 0 (LE) to 1 (TE)
    up = [(x_le + x * c, y, z0 + naca(x, t, m)[0] * c) for x in xs]
    lo = [(x_le + x * c, y, z0 + naca(x, t, m)[1] * c) for x in xs]
    pts = list(reversed(up)) + lo[1:]
    w = Wire([Spline(*pts), Line(pts[-1], pts[0])])
    return Face(w)


def _vert_airfoil_face(c, x_le, z, t=0.10, n=30):
    """Symmetric section lying in a horizontal plane at height z (for the fin), thickness along Y."""
    xs = [0.5 * (1 - math.cos(math.pi * i / n)) for i in range(n + 1)]
    up = [(x_le + x * c, naca(x, t, 0)[0] * c, z) for x in xs]
    lo = [(x_le + x * c, naca(x, t, 0)[1] * c, z) for x in xs]
    pts = list(reversed(up)) + lo[1:]
    return Face(Wire([Spline(*pts), Line(pts[-1], pts[0])]))


def box(x0, x1, y0, y1, z0, z1):
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(x1 - x0, y1 - y0, z1 - z0)


def cyl_x(x0, x1, y, z, d):
    return Pos((x0 + x1) / 2, y, z) * Rot(0, 90, 0) * Cylinder(d / 2, x1 - x0)


def cyl_y(y0, y1, x, z, d):
    return Pos(x, (y0 + y1) / 2, z) * Rot(90, 0, 0) * Cylinder(d / 2, y1 - y0)


def cyl_z(z0, z1, x, y, d):
    return Pos(x, y, (z0 + z1) / 2) * Cylinder(d / 2, z1 - z0)


def tube_x(x0, x1, y, z, od, idia):
    return cyl_x(x0, x1, y, z, od) - cyl_x(x0 - 1, x1 + 1, y, z, idia)


def tube_y(y0, y1, x, z, od, idia):
    return cyl_y(y0, y1, x, z, od) - cyl_y(y0 - 1, y1 + 1, x, z, idia)


def mirror_y(shape):
    from build123d import Plane as _P, mirror
    return mirror(shape, about=_P.XZ)


# ----------------------------------------------------------------------------- components
def wing_solid(side=1, P=PARAMS):
    """Outer mould line of one wing panel (side +1 right, -1 left), root rib face at |y| = fus_w / 2."""
    y0 = P["fus_w"] / 2
    y1 = y0 + P["panel_span"]
    fr = _airfoil_face(chord(y0, P), le_x(y0, P), y0, P["chord_z"])
    ft = _airfoil_face(chord(y1, P), le_x(y1, P), y1, P["chord_z"])
    s = loft([fr, ft], ruled=True)
    return s if side > 0 else mirror_y(s)


def aileron_cutter(side=1, P=PARAMS):
    ya, yb = P["aileron_y"]
    h = P["hinge_frac"]
    pts = [(le_x(ya, P) + h * chord(ya, P), ya), (le_x(yb, P) + h * chord(yb, P), yb),
           (le_x(yb, P) + chord(yb, P) + 5, yb), (le_x(ya, P) + chord(ya, P) + 5, ya)]
    if side < 0:
        pts = [(x, -y) for x, y in pts]
    face = make_face(Polyline(*pts, close=True))
    return Pos(0, 0, P["chord_z"] - 60) * extrude(face, 120)


def build_parts(P=PARAMS):
    D = derived(P)
    L, W, H, z0, t = P["fus_len"], P["fus_w"], P["fus_h"], P["fus_z0"], P["ply"]
    z1 = z0 + H
    yb, zb, rb = P["boom_y"], P["boom_z"], P["boom_od"] / 2
    m = {}

    # 1 fuselage box: two sides, floor, firewall, two bulkheads, rear wall, wing-root doublers
    outer = box(0, L, -W / 2, W / 2, z0, z1)
    inner = box(6, L - 6, -W / 2 + t, W / 2 - t, z0 + t, z1 + 1)
    fus = outer - inner
    for xb in P["bulkheads"]:
        fus += box(xb, xb + t, -W / 2 + t, W / 2 - t, z0 + t, z1)
    dx0, dx1 = P["doubler_x"]
    dz0, dz1 = P["doubler_z"]
    th = P["ply_thick"]
    for s in (1, -1):
        y_in = s * (W / 2 - t)
        fus += box(dx0, dx1, min(y_in, y_in - s * th), max(y_in, y_in - s * th), dz0, dz1)
    fus -= cyl_y(-W, W, P["spar_x"], P["spar_z"], P["joiner_od"] + 0.5)
    fus -= cyl_y(-W, W, P["wing_bolt_x"], P["wing_bolt_z"], 5.5)
    fus -= cyl_x(L - 10, L + 1, 0, P["tail_z"], P["tail_boom_od"] + 0.5)
    xc = D["x_cg"]
    ox, oy = CE.CORE["deck_opening"]
    fus -= box(xc - ox / 2, xc + ox / 2, -oy / 2, oy / 2, z0 - 1, z0 + t + 1)          # floor opening for the Core lid
    for fx, fy in CE.frame_points():
        fus -= cyl_z(z0 - 1, z0 + t + 1, xc - fx, fy, 4.3)
    m["fus"] = fus
    # 1a Core deck doubler: 6 mm birch on the floor, the Core's four M4 hard points and the lid opening
    dl, dt = P["core_deck"]
    dk = box(xc - dl / 2, xc + dl / 2, -W / 2 + t, W / 2 - t, z0 + t, z0 + t + dt)
    dk -= box(xc - ox / 2, xc + ox / 2, -oy / 2, oy / 2, z0, z0 + t + dt + 1)
    for fx, fy in CE.frame_points():
        dk -= cyl_z(z0, z0 + t + dt + 1, xc - fx, fy, 4.3)
    m["core_deck"] = dk

    # 2 hatch (3 mm ply) with the GNSS mast hole
    m["hatch"] = box(0, L, -W / 2, W / 2, z1, z1 + P["hatch_t"]) - cyl_z(z1 - 1, z1 + 10, P["gnss_x"], 0, 8.5)

    # 3 nose cone and cruise motor mount (printed ASA), hollow behind a 6 mm motor face
    from build123d import Rectangle, Circle
    zt = P["thrust_line_z"]
    rect = Plane(origin=(0, 0, (z0 + z1) / 2), x_dir=(0, 1, 0), z_dir=(1, 0, 0)) * Rectangle(W, H)
    tip = Plane(origin=(-P["nose_len"], 0, zt), x_dir=(0, 1, 0), z_dir=(1, 0, 0)) * Circle(P["nose_tip_d"] / 2)
    nose = loft([tip, rect])
    m["nose"] = nose

    # 4 tail boom socket (printed), glued inside the rear of the fuselage
    tz = P["tail_z"]
    m["socket"] = box(650, L - 6, -25, 25, tz - 25, tz + 25) - cyl_x(640, L, 0, tz, P["tail_boom_od"])

    # 5, 6 wing panels with spars, root bolt holes, pitot hole; 7 ailerons
    spar_len = P["panel_span"] - 20
    pit_y = P["pitot_y"]
    pit_x0 = le_x(pit_y, P) - 110
    pit_x1 = le_x(pit_y, P) + 40
    pit_z = P["chord_z"] + 1.0
    for side, key in ((1, "r"), (-1, "l")):
        w = wing_solid(side, P)
        y0 = side * W / 2
        spar = tube_y(min(y0, y0 + side * spar_len), max(y0, y0 + side * spar_len), P["spar_x"], P["spar_z"],
                      P["spar_od"], P["spar_id"])
        w -= cyl_y(min(y0, y0 + side * (spar_len + 1)), max(y0, y0 + side * (spar_len + 1)), P["spar_x"], P["spar_z"], P["spar_od"])
        w -= cyl_y(min(y0, y0 + side * 30), max(y0, y0 + side * 30), P["wing_bolt_x"], P["wing_bolt_z"], 5.5)
        for xb in P["pylon_bolts_x"]:
            w -= cyl_z(250, 400, xb, side * yb, 5.5)
        if side < 0:
            w -= cyl_x(pit_x0, pit_x1, pit_y, pit_z, 6.0)
        cut = aileron_cutter(side, P)
        m[f"ail_{key}"] = w & cut
        m[f"wing_{key}"] = w - cut
        m[f"spar_{key}"] = spar

    # 8 joiner tube through the fuselage and into both spars
    m["joiner"] = tube_y(-P["joiner_len"] / 2, P["joiner_len"] / 2, P["spar_x"], P["spar_z"], P["joiner_od"], P["joiner_id"])

    # 9 wing bolts, nylon M5 x 40, head inside the fuselage
    bolts = []
    for s in (1, -1):
        yi = s * (W / 2 - t - th)
        shank = cyl_y(min(yi, s * (W / 2 + 25)), max(yi, s * (W / 2 + 25)), P["wing_bolt_x"], P["wing_bolt_z"], 5.0)
        head = cyl_y(min(yi, yi - s * 4), max(yi, yi - s * 4), P["wing_bolt_x"], P["wing_bolt_z"], 9.0)
        bolts.append(shank + head)
    m["wing_bolts"] = Compound(bolts)

    # 10 boom pylons (printed ASA), conforming to the wing lower skin, saddle on the boom
    px0, px1 = P["pylon_x"]
    pw = P["pylon_w"]
    for side, key in ((1, "r"), (-1, "l")):
        y = side * yb
        py = box(px0, px1, y - pw / 2, y + pw / 2, zb, P["chord_z"] + 10)
        py -= wing_solid(side, P)
        py -= cyl_x(px0 - 1, px1 + 1, y, zb, P["boom_od"])
        for xb in P["pylon_bolts_x"]:
            py -= cyl_z(250, 400, xb, y, 5.5)
        m[f"pylon_{key}"] = py
        # pylon through-bolts M5, from washers on the upper skin down into nuts in the pylon
        pb = []
        for xb in P["pylon_bolts_x"]:
            zt_ = max(surface_z(xb + d, y, True, P) for d in (-7.5, -4, 0, 4, 7.5)) + 0.3
            pb.append(cyl_z(zt_ - 85, zt_ + 0.2, xb, y, 5.0) + cyl_z(zt_ + 0.2, zt_ + 1.7, xb, y, 15.0))
        m[f"pbolts_{key}"] = Compound(pb)
        # 11 clamp caps, two per pylon
        caps = []
        for cx0, cx1 in P["clamp_x"]:
            cap = box(cx0, cx1, y - pw / 2, y + pw / 2, zb - rb - P["clamp_t"], zb) - cyl_x(cx0 - 1, cx1 + 1, y, zb, P["boom_od"])
            caps.append(cap)
        m[f"caps_{key}"] = Compound(caps)
        # 12 lift boom, carbon tube
        m[f"boom_{key}"] = tube_x(D["boom_x"][0], D["boom_x"][1], y, zb, P["boom_od"], P["boom_id"])
        # 13 motor mounts with ESCs (bought aluminium tube clamp mounts)
        mounts, motors, props, escs, legs_c, rods, feet, fairs = [], [], [], [], [], [], [], []
        for k, mx in enumerate(D["motor_x"]):
            mt = box(mx - 20, mx + 20, y - 20, y + 20, zb - rb - 5, D["mount_top"]) - cyl_x(mx - 21, mx + 21, y, zb, P["boom_od"])
            mounts.append(mt)
            motors.append(cyl_z(D["mount_top"], D["motor_top"], mx, y, P["lift_motor_d"]))
            hub = cyl_z(D["motor_top"], D["motor_top"] + 10, mx, y, 30)
            blade = box(mx - P["lift_prop_d"] / 2, mx + P["lift_prop_d"] / 2, y - 18, y + 18, D["motor_top"] + 2, D["motor_top"] + 8)
            props.append(hub + blade)
            ex0, ex1 = (mx + 100, mx + 155) if k == 0 else (mx - 155, mx - 100)
            escs.append(box(ex0, ex1, y - 13, y + 13, zb - rb - 10, zb - rb))
        for lx in D["leg_x"]:
            cl = box(lx - 15, lx + 15, y - 18, y + 18, zb - rb - 22, zb + rb + 5) - cyl_x(lx - 16, lx + 16, y, zb, P["boom_od"])
            cl -= cyl_z(zb - rb - 23, zb - rb - 2, lx, y, P["leg_rod_d"])
            legs_c.append(cl)
            rods.append(cyl_z(8.0, zb - rb - 2, lx, y, P["leg_rod_d"]))
            ft = cyl_z(0, 10, lx, y, P["foot_d"]) + cyl_z(10, 28, lx, y, 22)
            feet.append(ft - cyl_z(8.0, 29, lx, y, P["leg_rod_d"]))
            from build123d import Ellipse
            zf0, zf1 = 28.0, zb - rb - 22
            fair = Pos(lx, y, zf0) * extrude(Ellipse(P["leg_fair"][0] / 2, P["leg_fair"][1] / 2), zf1 - zf0)
            fairs.append(fair - cyl_z(zf0 - 1, zf1 + 1, lx, y, P["leg_rod_d"] + 0.4))
        m[f"mounts_{key}"] = Compound(mounts)
        m[f"motors_{key}"] = Compound(motors)
        m[f"props_{key}"] = Compound(props)
        m[f"escs_{key}"] = Compound(escs)
        m[f"legclamps_{key}"] = Compound(legs_c)
        m[f"legrods_{key}"] = Compound(rods)
        m[f"feet_{key}"] = Compound(feet)
        m[f"legfair_{key}"] = Compound(fairs)

    # 14 cruise motor and folding propeller on the nose cone face
    xm1 = -P["nose_len"]
    xm0 = xm1 - P["cruise_motor_l"]
    m["cruise_motor"] = cyl_x(xm0, xm1, 0, zt, P["cruise_motor_d"])
    spinner = cyl_x(xm0 - 12, xm0, 0, zt, 36)
    blades = box(xm0 - 9, xm0 - 3, -14, 14, zt - P["cruise_prop_d"] / 2, zt + P["cruise_prop_d"] / 2)
    m["cruise_prop"] = spinner + blades

    # 15 tail boom, 16 tail mount, 17 stabiliser, 18 fin
    tx0, tx1 = P["tail_boom_x"]
    m["tail_boom"] = tube_x(tx0, tx1, 0, tz, P["tail_boom_od"], P["tail_boom_id"])
    sx0 = P["stab_le"]
    sc = P["stab_chord"]
    ss = P["stab_span"]
    sz = P["stab_z"]
    s_l = _airfoil_face(sc, sx0, -ss / 2, sz, t=0.10, m=0.0)
    s_r = _airfoil_face(sc, sx0, ss / 2, sz, t=0.10, m=0.0)
    stab = loft([s_l, s_r], ruled=True)
    fx_root = sx0 + sc - P["fin_root"]
    fx_tip = sx0 + sc - P["fin_tip"]
    f0 = _vert_airfoil_face(P["fin_root"], fx_root, sz)
    f1 = _vert_airfoil_face(P["fin_tip"], fx_tip, sz + 0.05 * sc + P["fin_h"])
    fin = loft([f0, f1], ruled=True) - stab
    mount = box(1360, tx1, -22, 22, tz - 15, sz + 2) - stab - fin - cyl_x(1300, tx1 + 5, 0, tz, P["tail_boom_od"])
    m["stab"] = stab
    m["fin"] = fin
    m["tail_mount"] = mount

    # bought and Kitewright Core parts in the bays (envelopes)
    pl, pw_, ph = P["pack"]
    zp = [z0 + t, z0 + t + P["core_deck"][1]]           # the rear pack sits on the Core deck doubler (10A)
    packs = [box(px, px + pl, -pw_ / 2, pw_ / 2, zz, zz + ph) for px, zz in zip(P["pack_x"], zp)]
    m["packs"] = Compound(packs)
    # Kitewright Core (Core repo), turned so its rail points aft: the payload slides in from the tail
    zc = D["core_z"]
    turn = lambda sh: Pos(xc, 0, zc) * Rot(0, 0, 180) * sh   # noqa: E731
    m["core"] = turn(CE.core_body())
    m["mount_plate"] = turn(CE.core_rail() + CE.core_pins() + CE.core_plug())
    al, aw, ah = P["payload"]
    sb = D["shoe_bot"]
    xs = xc - (CE.CORE["shoe"][0] + CE.CORE["shoe"][1]) / 2          # shoe centre (the Core is turned 180 deg)
    m["payload"] = turn(CE.shoe()) + box(xs - al / 2, xs + al / 2, -aw / 2, aw / 2, sb - ah, sb)
    zh = z1 + P["hatch_t"]
    m["gnss"] = cyl_z(z1 - 2, zh + P["gnss_mast"], P["gnss_x"], 0, 8.0) + cyl_z(zh + P["gnss_mast"], zh + P["gnss_mast"] + 16, P["gnss_x"], 0, 60)
    m["pitot"] = cyl_x(pit_x0, pit_x1, pit_y, pit_z, 6.0)
    return m


# Build order and BOM lines: key -> (BOM line, name). Grouped keys share one BOM line.
BOM = {
    "fus": (1, "Fuselage box"),
    "hatch": (2, "Hatch"),
    "nose": (3, "Nose cone and cruise motor mount"),
    "socket": (4, "Tail boom socket"),
    "wing_l": (5, "Wing panel, left"), "wing_r": (5, "Wing panel, right"),
    "spar_l": (6, "Wing spar, left"), "spar_r": (6, "Wing spar, right"),
    "ail_l": (5, "Aileron, left"), "ail_r": (5, "Aileron, right"),
    "joiner": (7, "Wing joiner tube"),
    "wing_bolts": (8, "Wing bolts"),
    "pylon_l": (9, "Boom pylon, left"), "pylon_r": (9, "Boom pylon, right"),
    "pbolts_l": (10, "Pylon bolts, left"), "pbolts_r": (10, "Pylon bolts, right"),
    "caps_l": (11, "Boom clamp caps, left"), "caps_r": (11, "Boom clamp caps, right"),
    "boom_l": (12, "Lift boom, left"), "boom_r": (12, "Lift boom, right"),
    "legclamps_l": (13, "Leg clamps, left"), "legclamps_r": (13, "Leg clamps, right"),
    "legrods_l": (13, "Leg rods, left"), "legrods_r": (13, "Leg rods, right"),
    "feet_l": (13, "Landing feet, left"), "feet_r": (13, "Landing feet, right"),
    "legfair_l": (13, "Leg fairings, left"), "legfair_r": (13, "Leg fairings, right"),
    "tail_boom": (14, "Tail boom"),
    "tail_mount": (15, "Tail mount"),
    "stab": (16, "Horizontal stabiliser with elevator"),
    "fin": (17, "Fin with rudder"),
    "mounts_l": (18, "Lift motor mounts, left"), "mounts_r": (18, "Lift motor mounts, right"),
    "escs_l": (19, "Lift ESCs, left"), "escs_r": (19, "Lift ESCs, right"),
    "motors_l": (20, "Lift motors, left"), "motors_r": (20, "Lift motors, right"),
    "props_l": (21, "Lift propellers, left"), "props_r": (21, "Lift propellers, right"),
    "cruise_motor": (22, "Cruise motor"),
    "cruise_prop": (23, "Cruise folding propeller"),
    "pitot": (25, "Heated pitot probe"),
    "core_deck": (1, "Core deck doubler"),
    "core": (26, "Kitewright Core (plate, spacers, lid)"),
    "gnss": (26, "GNSS mast on the hatch (Kitewright Core receiver)"),
    "mount_plate": (27, "Core rail, locking pins and pigtail (Kitewright Core)"),
    "packs": (28, "ColdCell packs"),
    "payload": (None, "Payload, 1 kg, on its payload shoe (LakeWatch envelope)"),
}

# How each part is made: key -> (process, material)
MAKE = {
    "fus": ("cut, glue", "3 mm poplar lite-ply, 6 mm birch aircraft plywood, glass cloth outside"),
    "hatch": ("cut", "3 mm poplar lite-ply"),
    "nose": ("print", "ASA, 4 perimeters, 25 % gyroid infill"),
    "socket": ("print", "ASA, 6 perimeters, 40 % infill"),
    "wing": ("hot-wire cut, bond, laminate", "XPS foam 30 kg/m3, 80 g/m2 glass cloth, epoxy"),
    "spar": ("cut", "pultruded carbon tube 22 x 20 mm"),
    "joiner": ("cut", "roll-wrapped carbon tube 20 x 16 mm"),
    "pylon": ("print", "ASA, 6 perimeters, 40 % infill"),
    "caps": ("print", "ASA, 100 % infill"),
    "boom": ("cut, drill", "roll-wrapped carbon tube 25 x 23 mm"),
    "legs": ("cut, print", "carbon rod 12 mm; printed ASA clamps and TPU feet"),
    "tail_boom": ("cut, drill", "pultruded carbon tube 20 x 17 mm"),
    "tail_mount": ("print", "ASA, 6 perimeters, 40 % infill"),
    "tail": ("hot-wire cut, laminate", "XPS foam, 80 g/m2 glass cloth, epoxy"),
}

# Masses of bought parts and Kitewright Core items (kg), per unit
BOUGHT_MASS = {
    "mounts": 0.035, "escs": 0.045, "motors": 0.285, "props": 0.055, "cruise_motor": 0.195,
    "cruise_prop": 0.045, "pitot": 0.030, "core": 0.990, "gnss": 0.030, "mount_plate": 0.0,   # Core 0.99 kg with rail and pins (Core R9, 10A)
    "packs": 1.400, "payload": 1.000, "wing_bolts": 0.004, "pbolts": 0.012, "servos": 0.035,
    "harness": 0.300, "cruise_esc": 0.060,
    "core_leads": 0.124,   # four 8 AWG leads with AS150 plugs, now supplied by the frame (Core decision 33B)
    "ant_leads": 0.030,    # three SMA extension leads: the Core's antennas to the hatch (decision 10A)
}


def assembly(P=PARAMS, with_payload=True):
    m = build_parts(P)
    return Compound([s for k, s in m.items() if with_payload or k != "payload"])


def _solids(s):
    return list(s.solids()) if hasattr(s, "solids") else [s]


def check(P=PARAMS, verbose=True):
    """Constructability checks with build123d: no two parts overlap, no part floats, design-around and
    transport rules hold. Returns a list of problems (empty when the design passes)."""
    m = build_parts(P)
    D = derived(P)
    keys = list(m)
    flat = [(k, i, s) for k in keys for i, s in enumerate(_solids(m[k]))]
    problems = []
    bbs = [s.bounding_box() for _, _, s in flat]
    for a in range(len(flat)):
        for b in range(a + 1, len(flat)):
            if flat[a][0] == flat[b][0]:
                continue
            A, B = bbs[a], bbs[b]
            if (A.min.X > B.max.X or B.min.X > A.max.X or A.min.Y > B.max.Y or B.min.Y > A.max.Y
                    or A.min.Z > B.max.Z or B.min.Z > A.max.Z):
                continue
            try:
                v = (flat[a][2] & flat[b][2]).volume
            except Exception:
                v = 0.0
            if v > 1.0:
                problems.append(f"overlap {flat[a][0]}[{flat[a][1]}] / {flat[b][0]}[{flat[b][1]}]: {v:.1f} mm3")
    # floating: every solid must be within 0.6 mm of some solid of another part
    for a, (k, i, s) in enumerate(flat):
        near = False
        for b, (k2, i2, s2) in enumerate(flat):
            if k2 == k:
                continue
            A, B = bbs[a], bbs[b]
            if (A.min.X - 1 > B.max.X or B.min.X - 1 > A.max.X or A.min.Y - 1 > B.max.Y or B.min.Y - 1 > A.max.Y
                    or A.min.Z - 1 > B.max.Z or B.min.Z - 1 > A.max.Z):
                continue
            if s.distance_to(s2) < 0.6:
                near = True
                break
        if not near and k not in ("payload",):
            problems.append(f"floating {k}[{i}]")
    if D["disc_below_wing_top"] < P["disc_clear_min"]:
        problems.append(f"rotor disc only {D['disc_below_wing_top']:.0f} mm below the wing-top plane")
    if D["lift_to_cruise_disc_y"] < 20:
        problems.append("lift and cruise propeller discs too close")
    if D["rear_disc_to_te"] < 30 or D["front_disc_to_le"] < 30:
        problems.append("lift propeller disc over the wing")
    # 22 in propellers (KWR-DDR-003): the larger discs must still clear the fuselage side and the stabiliser
    if D["lift_disc_to_fus"] < 50:
        problems.append(f"lift disc only {D['lift_disc_to_fus']:.0f} mm from the fuselage side")
    if D["rear_disc_to_stab"] < 50:
        problems.append(f"rear lift disc only {D['rear_disc_to_stab']:.0f} mm from the stabiliser")
    if P["lift_motor_d"] > 64.0:
        problems.append("lift motor wider than the 64 mm motor mount top plate")
    lengths = {"wing panel": P["panel_span"] + 25, "lift boom": D["boom_len"],
               "tail boom with tail": P["tail_boom_x"][1] - P["tail_boom_x"][0] + 20,
               "fuselage with nose": P["fus_len"] + P["nose_len"] + P["cruise_motor_l"] + 12}
    for n, ln in lengths.items():
        if ln > P["case_len"] - 50:
            problems.append(f"{n} {ln:.0f} mm does not fit a {P['case_len']:.0f} mm case")
    if verbose:
        print(f"checked {len(flat)} solids in {len(keys)} parts")
        for p in problems:
            print("  PROBLEM", p)
        if not problems:
            print("  no overlaps, nothing floating, design-around and transport rules hold")
    return problems


def export(P=PARAMS):
    m = build_parts(P)
    (ROOT / "cad" / "step").mkdir(parents=True, exist_ok=True)
    (ROOT / "cad" / "stl").mkdir(parents=True, exist_ok=True)
    asm = Compound([s for k, s in m.items() if k != "payload"])
    export_step(asm, str(ROOT / "cad" / "step" / "kitewright-range-assembly.step"))
    groups = {
        "fuselage": ["fus", "hatch", "nose", "socket"],
        "wing-panel-right": ["wing_r", "ail_r", "spar_r"],
        "boom-pylon-right": ["pylon_r", "caps_r"],
        "landing-leg-parts": ["legclamps_r", "feet_r"],
        "tail": ["tail_mount", "stab", "fin"],
    }
    for name, ks in groups.items():
        c = Compound([m[k] for k in ks])
        export_step(c, str(ROOT / "cad" / "step" / f"kitewright-range-{name}.step"))
    for name, k in {"nose-cone": "nose", "tail-boom-socket": "socket", "boom-pylon-right": "pylon_r",
                    "boom-clamp-caps": "caps_r", "leg-clamps": "legclamps_r", "landing-feet": "feet_r", "leg-fairings": "legfair_r",
                    "tail-mount": "tail_mount"}.items():
        export_stl(m[k], str(ROOT / "cad" / "stl" / f"kitewright-range-{name}.stl"), tolerance=0.2, angular_tolerance=0.3)
    print("exported STEP and STL")


if __name__ == "__main__":
    D = derived()
    for k in ("span", "wing_area_m2", "mac", "x_cg", "aspect_ratio", "motor_x", "boom_len", "disc_below_wing_top",
              "front_disc_to_le", "rear_disc_to_te", "lift_to_cruise_disc_y", "rear_disc_to_stab", "lift_disc_to_fus", "tail_arm", "vh", "vv",
              "overall_len", "ground_to_payload", "ground_to_cruise_tip"):
        v = D[k]
        print(f"{k:24s} {v if isinstance(v, tuple) else round(v, 3)}")
    probs = check()
    if "--no-export" not in sys.argv:
        export()
    sys.exit(1 if probs else 0)
