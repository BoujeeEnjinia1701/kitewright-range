"""Kitewright Range product appearance model (build123d), TRL 3, constructable design (KWR-DDR-002).

Finished-product look for photoreal renders: white glassed foam wing and tail with teal ailerons, a light
grey glassed fuselage with its hatch, teal printed nose cone, pylons, tail mount and clamps, charcoal
carbon booms, spars and tail boom, orange lift motors with aluminium tube mounts, tapered black
20 in lift propellers parked fore and aft, the folding cruise propeller at the nose, the GNSS mast,
the heated pitot on the left wing, faired landing legs with rubber feet and the 1 kg payload under
the fuselage. Inside (exploded view): the two ColdCell packs, the Kitewright Core avionics and the
wing joiner. Context: a 1.75 m standing mannequin beside the right wing tip, behind the aircraft as
seen from the hero camera (front left).

Every part and dimension comes from cad/src/model.py (build_parts, PARAMS, derived); the only
appearance additions are the tapered propeller blades in place of the model's flat blade envelopes
(recorded in docs/REVIEW.md). APPEARANCE MODEL ONLY. CONCEPT, NOT FOR FABRICATION.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / ".kit"))

from build123d import Compound, Polyline, Pos, extrude, make_face  # noqa: E402
from model import PARAMS, build_parts, derived  # noqa: E402

TITLE = "Kitewright Range: all-electric quadplane survey frame"

RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "context"], "explode": False, "el": 30, "az": -140,
     "note": "Product render from the front left and above (about 30 deg elevation): 2.5 m wing on the fuselage, "
             "four lift rotors on booms below the wing, folding cruise propeller at the nose, payload underneath; "
             "1.75 m person standing beyond the far (right) wing tip for scale"},
    {"name": "exploded", "groups": ["shell", "internal"], "explode": True, "el": 28, "az": -140,
     "note": "Exploded view from the front left and above (about 28 deg elevation): wing panels and booms out to the "
             "sides, hatch, packs and Kitewright Core lifted out of the fuselage, tail pulled aft, payload below"},
    # render with --focus on the left front lift motor and pylon (see docs/REVIEW.md)
    {"name": "detail", "groups": ["shell"], "explode": False, "el": 14, "az": -125,
     "note": "Detail from the front left, slightly above (about 14 deg elevation), close on the left boom: printed "
             "pylon under the wing, clamp caps, front lift motor on its tube mount, faired landing leg and foot"},
]

C_WHITE = "#F4F5F7"
C_GREY = "#D9DCE1"
C_TEAL = "#0F766E"
C_CARBON = "#23262B"
C_ALU = "#B9BEC5"
C_ORANGE = "#C2410C"
C_BLACK = "#16181C"


def _blades(cx, cy, z0, radius, hub_r=15.0, c_root=42.0, c_tip=16.0, t=6.0, along="x"):
    """Two tapered blades parked fore and aft (along X), or vertical (along Z for the cruise propeller)."""
    out = []
    for sgn in (1, -1):
        pts = [(sgn * hub_r, -c_root / 2), (sgn * radius, -c_tip / 2), (sgn * radius, c_tip / 2), (sgn * hub_r, c_root / 2)]
        blade = extrude(make_face(Polyline(*pts, close=True)), t)
        out.append(blade)
    s = Compound(out)
    if along == "x":
        return Pos(cx, cy, z0) * s
    from build123d import Rot
    return Pos(cx, cy, z0) * Rot(0, -90, 0) * s


def product_parts(P=PARAMS):
    D = derived(P)
    m = build_parts(P)
    out = []

    def add(name, shape, color, material, bom, group, explode=(0, 0, 0)):
        out.append({"name": name, "shape": shape, "color": color, "material": material, "bom": bom,
                    "group": group, "explode": tuple(float(v) for v in explode)})

    L, R = (0, -520, 160), (0, 520, 160)
    add("Fuselage, glassed", m["fus"], C_GREY, "painted", 1, "shell")
    add("Hatch", m["hatch"], C_GREY, "painted", 2, "shell", (0, 0, 420))
    add("Nose cone, printed", m["nose"], C_TEAL, "plastic", 3, "shell", (-260, 0, 0))
    add("Tail boom socket", m["socket"], C_TEAL, "plastic", 4, "internal")
    add("Wing panel, left", m["wing_l"], C_WHITE, "painted", 5, "shell", L)
    add("Wing panel, right", m["wing_r"], C_WHITE, "painted", 5, "shell", R)
    add("Aileron, left", m["ail_l"], C_TEAL, "painted", 5, "shell", L)
    add("Aileron, right", m["ail_r"], C_TEAL, "painted", 5, "shell", R)
    add("Wing spar, left", m["spar_l"], C_CARBON, "painted", 6, "internal", L)
    add("Wing spar, right", m["spar_r"], C_CARBON, "painted", 6, "internal", R)
    add("Wing joiner", m["joiner"], C_CARBON, "painted", 7, "internal", (0, 0, 260))
    add("Wing bolts", m["wing_bolts"], C_WHITE, "plastic", 8, "internal")
    for side, e in (("left", L), ("right", R)):
        k = side[0]
        eb = (e[0], e[1], -60)
        add(f"Boom pylon, {side}", m[f"pylon_{k}"], C_TEAL, "plastic", 9, "shell", e)
        add(f"Pylon bolts, {side}", m[f"pbolts_{k}"], C_ALU, "metal", 10, "shell", e)
        add(f"Clamp caps, {side}", m[f"caps_{k}"], C_TEAL, "plastic", 11, "shell", (e[0], e[1], -160))
        add(f"Lift boom, {side}", m[f"boom_{k}"], C_CARBON, "painted", 12, "shell", eb)
        add(f"Leg clamps, {side}", m[f"legclamps_{k}"], C_TEAL, "plastic", 13, "shell", (e[0], e[1], -260))
        add(f"Leg rods, {side}", m[f"legrods_{k}"], C_CARBON, "painted", 13, "shell", (e[0], e[1], -260))
        add(f"Leg fairings, {side}", m[f"legfair_{k}"], C_GREY, "plastic", 13, "shell", (e[0], e[1], -260))
        add(f"Landing feet, {side}", m[f"feet_{k}"], C_BLACK, "rubber", 13, "shell", (e[0], e[1], -260))
        add(f"Lift motor mounts, {side}", m[f"mounts_{k}"], C_ALU, "metal", 18, "shell", eb)
        add(f"Lift ESCs, {side}", m[f"escs_{k}"], C_BLACK, "plastic", 19, "shell", (e[0], e[1], -160))
        add(f"Lift motors, {side}", m[f"motors_{k}"], C_ORANGE, "metal", 20, "shell", (e[0], e[1], 60))
        y = (-1 if side == "left" else 1) * P["boom_y"]
        props = []
        for mx in D["motor_x"]:
            from build123d import Cylinder
            hub = Pos(mx, y, D["motor_top"] + 5) * Cylinder(15, 10)
            props.append(hub)
            props.append(_blades(mx, y, D["motor_top"] + 2, P["lift_prop_d"] / 2))
        add(f"Lift propellers, {side}", Compound(props), C_BLACK, "plastic", 21, "shell", (e[0], e[1], 200))
    add("Tail boom", m["tail_boom"], C_CARBON, "painted", 14, "shell", (300, 0, 0))
    add("Tail mount", m["tail_mount"], C_TEAL, "plastic", 15, "shell", (480, 0, 0))
    add("Horizontal stabiliser", m["stab"], C_WHITE, "painted", 16, "shell", (480, 0, 100))
    add("Fin", m["fin"], C_WHITE, "painted", 17, "shell", (480, 0, 200))
    add("Cruise motor", m["cruise_motor"], C_ORANGE, "metal", 22, "shell", (-420, 0, 0))
    xs = -P["nose_len"] - P["cruise_motor_l"]
    from build123d import Cylinder, Rot
    spinner = Pos(xs - 6, 0, P["thrust_line_z"]) * Rot(0, 90, 0) * Cylinder(18, 12)
    blades = _blades(xs - 9, 0, P["thrust_line_z"], P["cruise_prop_d"] / 2, hub_r=14, c_root=30, c_tip=14, t=6, along="z")
    add("Cruise folding propeller", Compound([spinner, blades]), C_BLACK, "plastic", 23, "shell", (-560, 0, 0))
    add("Heated pitot probe", m["pitot"], C_ALU, "metal", 25, "shell", (-200, -520, 160))
    add("Kitewright Core avionics", m["core"], "#16A34A", "plastic", 26, "internal", (0, 0, 520))
    add("GNSS mast", m["gnss"], C_BLACK, "plastic", 26, "shell", (0, 0, 640))
    add("Payload mount", m["mount_plate"], C_ALU, "metal", 27, "shell", (0, 0, -180))
    add("ColdCell packs", m["packs"], "#EA580C", "plastic", 28, "internal", (0, 0, 640))
    add("Payload, 1 kg", m["payload"], "#57534E", "plastic", None, "shell", (0, 0, -380))
    # context: a standing person beyond the right wing tip, on the far side of the aircraft from the hero camera
    from context_parts import mannequin
    person = Pos(0, P["fus_w"] / 2 + P["panel_span"] + 450, 0) * mannequin(1750, "stand")
    add("Person, 1.75 m (scale)", person, "#B8B2A7", "clay", None, "context")
    return out


if __name__ == "__main__":
    for p in product_parts():
        print(f"{p['name']:32s} {p['group']:9s} {p['material']}")
