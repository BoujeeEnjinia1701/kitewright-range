"""Kitewright Range concept media (TRL 3, constructable design KWR-DDR-002 and KWR-DDR-003), generated from the model.

Run from the repo root:  python cad/src/concept_media.py
Takes every part from cad/src/model.py and renders the media set with .kit/concept.py: hero with the
1.75 m figure, cutaway, exploded view with BOM numbers, blueprint sheet KWR-DWG-010, the glTF viewer
and the energy flow per flight. Figures come from docs/04-calcs/sizing.py (KWR-CAL-001).
CONCEPT, NOT FOR FABRICATION.
"""
import functools
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src"), str(ROOT / "docs" / "04-calcs")]
import concept as K  # noqa: E402
from concept import Part, render_all  # noqa: E402
from model import BOM, build_parts  # noqa: E402
import sizing  # noqa: E402

C = {  # colour, exploded offset (mm)
    "fus": ("#E5E7EB", (0, 0, 0)), "hatch": ("#F3F4F6", (0, 0, 260)), "nose": ("#9CA3AF", (-260, 0, 0)),
    "socket": ("#6B7280", (0, 0, 0)),
    "wing_l": ("#F8FAFC", (0, -420, 120)), "wing_r": ("#F8FAFC", (0, 420, 120)),
    "ail_l": ("#0F766E", (0, -420, 120)), "ail_r": ("#0F766E", (0, 420, 120)),
    "spar_l": ("#111827", (0, -420, 120)), "spar_r": ("#111827", (0, 420, 120)),
    "joiner": ("#111827", (0, 0, 120)), "wing_bolts": ("#D4A017", (0, 0, 0)),
    "pylon_l": ("#0F766E", (0, -420, 40)), "pylon_r": ("#0F766E", (0, 420, 40)),
    "pbolts_l": ("#9CA3AF", (0, -420, 120)), "pbolts_r": ("#9CA3AF", (0, 420, 120)),
    "caps_l": ("#0F766E", (0, -420, -160)), "caps_r": ("#0F766E", (0, 420, -160)),
    "boom_l": ("#1F2937", (0, -420, -100)), "boom_r": ("#1F2937", (0, 420, -100)),
    "legclamps_l": ("#374151", (0, -420, -220)), "legclamps_r": ("#374151", (0, 420, -220)),
    "legrods_l": ("#111827", (0, -420, -220)), "legrods_r": ("#111827", (0, 420, -220)),
    "legfair_l": ("#6B7280", (0, -420, -220)), "legfair_r": ("#6B7280", (0, 420, -220)),
    "feet_l": ("#111827", (0, -420, -220)), "feet_r": ("#111827", (0, 420, -220)),
    "tail_boom": ("#1F2937", (260, 0, 0)), "tail_mount": ("#0F766E", (420, 0, 0)),
    "stab": ("#F8FAFC", (420, 0, 120)), "fin": ("#F8FAFC", (420, 0, 240)),
    "mounts_l": ("#9CA3AF", (0, -420, -40)), "mounts_r": ("#9CA3AF", (0, 420, -40)),
    "escs_l": ("#7C3AED", (0, -420, -160)), "escs_r": ("#7C3AED", (0, 420, -160)),
    "motors_l": ("#C2410C", (0, -420, 60)), "motors_r": ("#C2410C", (0, 420, 60)),
    "props_l": ("#374151", (0, -420, 160)), "props_r": ("#374151", (0, 420, 160)),
    "cruise_motor": ("#C2410C", (-380, 0, 0)), "cruise_prop": ("#374151", (-500, 0, 0)),
    "pitot": ("#D4A017", (-200, -420, 120)), "core": ("#16A34A", (0, 0, 420)), "gnss": ("#16A34A", (0, 0, 560)),
    "mount_plate": ("#94A3B8", (0, 0, -140)), "packs": ("#C2410C", (0, 0, 520)),
    "payload": ("#A8A29E", (0, 0, -300)),
}


def web_model(parts, title):
    """Coarse glTF tessellation (1 mm chord, 0.35 rad) keeps media/model.glb a few MB."""
    import build123d as bd
    orig = bd.export_gltf
    bd.export_gltf = functools.partial(orig, linear_deflection=1.0, angular_deflection=0.35)
    K.export_gltf = bd.export_gltf
    try:
        return K.export_web_model(parts, "media", title=title)
    finally:
        bd.export_gltf = orig


LINE = {5: "Wing panels with ailerons", 6: "Wing spars", 9: "Boom pylons", 10: "Pylon bolts", 11: "Boom clamp caps",
        12: "Lift booms", 13: "Landing legs (clamp, rod, fairing, foot)", 18: "Lift motor mounts", 19: "Lift ESCs",
        20: "Lift motors", 21: "Lift propellers", 26: "Kitewright Core avionics and GNSS mast"}


def main():
    R, _, _ = sizing.main(verbose=False)
    m = build_parts()
    parts = []
    for k, s in m.items():
        num, name = BOM[k]
        col, off = C[k]
        parts.append(Part(LINE.get(num, name), s, col, num, off))
    if "--exploded-only" in sys.argv:
        K._render(parts, ROOT / "media" / "exploded.png", offsets=True, labels=True,
                  title="Kitewright Range: exploded view",
                  note="Seen from the front right and above, 24 deg elevation; numbers match bom/bom.csv")
        return
    title = "All-electric quadplane survey frame"
    render_all(
        parts, project="Kitewright Range", title=title, dwg_no="KWR-DWG-010", rev="P3",
        key_figures=[f"Span {R['span_m']:.2f} m, two 1.18 m wing panels; quadplane, fixed motors, not a tail-sitter",
                     f"Take-off mass {R['mtow_kg']:.1f} kg with 1 kg payload; four 22 in lift rotors",
                     f"Hover thrust margin {R['hover_margin'] * 100:.0f} % at 0.736 kg/m3 (5,000 m)",
                     f"Cruise {R['v_cruise_ms']:.0f} m/s, {R['p_cruise_elec_w']:.0f} W; {R['endurance_min']:.0f} min and "
                     f"{R['range_km']:.0f} km at 5,000 m with 20 % reserve",
                     f"Two ColdCell 6S packs, {R['nominal_wh']:.0f} Wh; rotor discs {R['disc_below_wing_top_mm']:.0f} mm "
                     "below the wing-top plane",
                     f"Estimated cost USD {R['cost_usd']:,.0f} against a USD 5,000 value-engineering target"],
        web_model=False, cut_exclude=("Wing panel, left", "Aileron, left", "Wing spar, left", "Boom pylon, left",
                                      "Pylon bolts, left"),
        flow={"title": "energy per survey flight at 5,000 m, Wh (KWR-CAL-001 estimates)", "unit": "Wh",
              "stages": [("ColdCell packs, nominal", round(R["nominal_wh"])),
                         ("Usable, packs warmed", round(R["usable_wh"])),
                         ("Mission energy", round(R["available_wh"])),
                         ("Cruise on the wing", round(R["cruise_wh"])),
                         ("Thrust power on the wing", round(R["cruise_wh"] * (R["p_cruise_aero_w"] / R["p_cruise_elec_w"])))],
              "losses": [(0, "Cold and voltage cut-off", round(R["nominal_wh"] - R["usable_wh"])),
                         (1, "20 % landing reserve", round(R["usable_wh"] - R["available_wh"])),
                         (2, "Hover, transition and climb", round(R["e_vtol_wh"] + R["e_climb_wh"])),
                         (3, "Motor, propeller and systems", round(R["cruise_wh"] * (1 - R["p_cruise_aero_w"] / R["p_cruise_elec_w"])))]},
    )
    web_model([p for p in parts if p.bom is not None], "Kitewright Range: " + title)
    import shutil
    for d in ("_views", "_views_fig"):
        shutil.rmtree(ROOT / "media" / d, ignore_errors=True)
    print("concept media written")


if __name__ == "__main__":
    main()
