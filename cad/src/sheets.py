"""Kitewright Range general arrangement sheet KWR-DWG-001, Rev P2 (TRL 3, constructable design KWR-DDR-002).

Run from the repo root:  python cad/src/sheets.py
Writes cad/drawings/KWR-DWG-001.svg, .pdf and .png from cad/src/model.py with .kit/drawing.py.
Every figure on the sheet comes from PARAMS and derived(). The concept blueprint is KWR-DWG-010.
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
from build123d import Compound  # noqa: E402
from drawing import Sheet, project_views, _t, M, INK  # noqa: E402
from model import PARAMS as P, build_parts, derived  # noqa: E402

DATE = "2026-10-03"


def main():
    D = derived(P)
    m = build_parts(P)
    asm = Compound([s for k, s in m.items() if k != "payload"])
    work = ROOT / "cad" / "drawings" / "_views_ga"
    views = project_views(asm, work)
    s = Sheet(project="Kitewright Range", title="All-electric quadplane survey frame: general arrangement",
              dwg_no="KWR-DWG-001", rev="P2", author="Amish Chadha", date=DATE, scale=0.04, theme="technical",
              material="Foam and glass wing and tail, lite-ply fuselage, carbon tubes, printed ASA fittings; "
                       "bought parts per bom/bom.csv. PRELIMINARY, NOT FOR FABRICATION",
              revisions=[("P1", "Preliminary GA for TRL 3 (KWR-CAL-001)", DATE, "AC"),
                         ("P2", "KWR-DDR-002: design for construction", DATE, "AC")])
    s.add_ortho(views)
    s.add_svg(views["iso"], 276, 36, 140, 84, label="Isometric view",
              sublabel="Not to scale; seen from the front right and above")
    s.add_notes("Main dimensions and interfaces (mm)", [
        f"Span {D['span']:,.0f}: two wing panels {P['panel_span']:,.0f} on a {P['joiner_od']:.0f} carbon joiner",
        f"Wing NACA 2412, chord {P['root_chord']:.0f} root to {P['tip_chord']:.0f} tip; spar {P['spar_od']:.0f} OD at 30 % chord",
        f"Fuselage {P['fus_len']:.0f} x {P['fus_w']:.0f} x {P['fus_h']:.0f}; nose to tail {D['overall_len']:,.0f}, {P['stab_le'] + P['stab_chord'] - (D['motor_x'][0] - P['lift_prop_d'] / 2):,.0f} over the lift propellers",
        f"Lift booms {P['boom_od']:.0f} OD x {D['boom_len']:,.0f} at y = +/-{P['boom_y']:.0f}, on pylons below the wing",
        f"Lift motors {2 * P['motor_half_span']:,.0f} apart along each boom, centred on the CG at x = {D['x_cg']:.0f}",
        f"Lift propellers 20 in ({P['lift_prop_d']:.0f}); discs {D['disc_below_wing_top']:.0f} below the wing-top plane",
        f"Cruise motor at the nose, 14 in folding propeller; {D['lift_to_cruise_disc_y']:.0f} gap to the lift discs",
        f"Tail on a {P['tail_boom_od']:.0f} carbon boom: stabiliser {P['stab_span']:.0f} x {P['stab_chord']:.0f}, fin {P['fin_h']:.0f} high",
        f"Payload mount under the fuselage at the CG; {D['ground_to_payload']:.0f} ground clearance under a 1 kg payload",
        f"Four landing legs, stance {2 * P['boom_y']:.0f} x {D['leg_x'][1] - D['leg_x'][0]:,.0f}",
        f"Longest part for transport: wing panel {P['panel_span'] + 25:,.0f}",
        "Third-angle; front view from -Y (left side); X aft from the firewall, Z up from the ground",
    ], x=276, y=132, width=146)
    out = s.save(ROOT / "cad" / "drawings" / "KWR-DWG-001")
    shutil.rmtree(work, ignore_errors=True)
    print("wrote", out)


if __name__ == "__main__":
    main()
