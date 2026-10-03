"""Kitewright Range build plan pictures (KWR-BLD-001), generated from the constructable model.

Run from the repo root:  python cad/src/build_plan_media.py [overview|sheets|joints|steps]
Writes docs/05-build-plan/overview.png, joint-NN.png and step-NN.png, and the making sketches
cad/drawings/KWR-DWG-101 onward, with .kit/build_views.py. BUILD PLAN ILLUSTRATIONS, PLAN NOT YET BUILT.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
from build123d import Compound  # noqa: E402
from build_views import Part, overview, step, joint, component_sheet  # noqa: E402
from model import PARAMS as P, build_parts, derived, box, chord, le_x  # noqa: E402

DATE = "2026-10-03"
OUT = ROOT / "docs" / "05-build-plan"
D = derived(P)
m = build_parts(P)

COL = {"ply": "#D6B98C", "print": "#0F766E", "carbon": "#1F2937", "foam": "#F1F5F9", "metal": "#9CA3AF",
       "elec": "#C2410C", "core": "#16A34A", "pack": "#EA580C", "steel": "#D4A017", "tpu": "#111827"}


def part(key, name, color, explode=(0, 0, 0), shape=None):
    return Part(name, shape if shape is not None else m[key], color, None, explode)


def win(key, x0, x1, y0, y1, z0, z1):
    return m[key] & box(x0, x1, y0, y1, z0, z1)


def comp(*keys):
    return Compound([m[k] for k in keys])


yb, zb = P["boom_y"], P["boom_z"]
mx0, mx1 = D["motor_x"]
lx0, lx1 = D["leg_x"]

# ---------------------------------------------------------------- overview, in build order
GROUPS = [
    ("Fuselage box", comp("fus"), COL["ply"], (0, 0, 0)),
    ("Tail boom socket", comp("socket"), COL["print"], (0, 0, 120)),
    ("Nose cone and cruise motor mount", comp("nose"), COL["print"], (-200, 0, 0)),
    ("Cruise motor and folding propeller", comp("cruise_motor", "cruise_prop"), COL["elec"], (-420, 0, 0)),
    ("Kitewright Core avionics", comp("core"), COL["core"], (0, 0, 450)),
    ("Payload mount", comp("mount_plate"), COL["metal"], (0, 0, -160)),
    ("Tail boom", comp("tail_boom"), COL["carbon"], (250, 0, 0)),
    ("Tail mount", comp("tail_mount"), COL["print"], (420, 0, -60)),
    ("Stabiliser and fin", comp("stab", "fin"), COL["foam"], (420, 0, 160)),
    ("Wing panels with ailerons and spars", comp("wing_l", "wing_r", "ail_l", "ail_r", "spar_l", "spar_r"), COL["foam"], (0, 0, 420)),
    ("Boom pylons and pylon bolts", comp("pylon_l", "pylon_r", "pbolts_l", "pbolts_r"), COL["print"], (0, 0, 120)),
    ("Wing joiner and wing bolts", comp("joiner", "wing_bolts"), COL["carbon"], (0, 0, 620)),
    ("Lift booms and clamp caps", comp("boom_l", "boom_r", "caps_l", "caps_r"), COL["carbon"], (0, 0, -160)),
    ("Motor mounts, ESCs and lift motors", comp("mounts_l", "mounts_r", "escs_l", "escs_r", "motors_l", "motors_r"), COL["elec"], (0, 0, -60)),
    ("Landing legs", comp("legclamps_l", "legclamps_r", "legrods_l", "legrods_r", "legfair_l", "legfair_r", "feet_l", "feet_r"), COL["metal"], (0, 0, -330)),
    ("ColdCell packs", comp("packs"), COL["pack"], (0, 0, 330)),
    ("Hatch and GNSS mast", comp("hatch", "gnss"), COL["ply"], (0, 0, 560)),
    ("Lift propellers", comp("props_l", "props_r"), "#374151", (0, 0, 120)),
    ("Heated pitot probe", comp("pitot"), COL["steel"], (-200, 0, 0)),
    ("Payload (1 kg, from the payload's own design)", comp("payload"), "#A8A29E", (300, 0, -480)),
]


def do_overview():
    parts = [Part(n, s, c, None, e) for n, s, c, e in GROUPS]
    overview(parts, OUT / "overview.png", "Kitewright Range: every component, pulled apart and numbered in build order",
             key=True, size=(11, 7))


# ---------------------------------------------------------------- making sketches
def do_sheets():
    fus_nb = [part("hatch", "", "#ccc"), part("nose", "", "#ccc"), part("joiner", "", "#ccc"), part("socket", "", "#ccc")]
    S = [
        ("KWR-DWG-101", "fus", "Fuselage box", "3 mm poplar lite-ply sides, floor and bulkheads; 6 mm birch ply firewall, rear wall and doublers; glass cloth outside", [
            f"Box {P['fus_len']:.0f} long, {P['fus_w']:.0f} wide, {P['fus_h']:.0f} high, open on top for the hatch.",
            "Cut two sides and the floor from 3 mm lite-ply; firewall and rear wall from 6 mm birch ply.",
            f"Two 3 mm bulkheads {P['bulkheads'][0]:.0f} and {P['bulkheads'][1]:.0f} back from the firewall face.",
            f"6 mm doublers inside each side, {P['doubler_x'][1] - P['doubler_x'][0]:.0f} x {P['doubler_z'][1] - P['doubler_z'][0]:.0f}, top edge 3 below the rim.",
            f"Drill the joiner hole 20.5 through side and doubler, centre {P['spar_x']:.0f} back and {P['fus_z0'] + P['fus_h'] - P['spar_z']:.0f} down from the rim.",
            f"Drill the wing bolt hole 5.5, centre {P['wing_bolt_x']:.0f} back and {P['fus_z0'] + P['fus_h'] - P['wing_bolt_z']:.0f} down; same on both sides.",
            f"Drill the rear wall 20.5 for the tail boom, {P['fus_z0'] + P['fus_h'] - P['tail_z']:.0f} down from the rim, on the centre line.",
            "Glue on a flat board with a square; check both joiner holes line up with a straight 20 mm rod.",
            "Glass the outside with 80 g/m2 cloth; four M4 inserts in the floor for the payload mount.",
        ], fus_nb),
        ("KWR-DWG-102", "hatch", "Hatch", "3 mm poplar lite-ply", [
            f"Plate {P['fus_len']:.0f} x {P['fus_w']:.0f} x 3; sits on the side walls and bulkheads.",
            "Glue a 20 mm tongue under the front edge that slides under a lip on the firewall.",
            "One M4 nylon thumb screw at the back into a captive nut on the rear wall.",
            f"8.5 mm hole for the GNSS mast, {P['gnss_x']:.0f} back from the front edge, on the centre line.",
            "Cut a slot for the lockable arming switch next to the mast (see the harness plan).",
        ], [part("fus", "", "#ccc"), part("gnss", "", "#ccc")]),
        ("KWR-DWG-103", "nose", "Nose cone and cruise motor mount", "Printed ASA, 4 perimeters, 10 to 25 % gyroid infill", [
            f"Lofted from the {P['fus_w']:.0f} x {P['fus_h']:.0f} fuselage face to a {P['nose_tip_d']:.0f} round motor face, {P['nose_len']:.0f} long.",
            "Print nose down with the motor face on the bed; no supports needed.",
            "Four M3 heat-set inserts in the motor face on the bolt circle of the motor bought.",
            "Four M4 bolts and epoxy hold it to the firewall; the thrust line is the fuselage centre line.",
            "Leave a 15 mm hole through the motor face for cooling air and the motor wires.",
        ], [part("fus", "", "#ccc"), part("cruise_motor", "", "#ccc")]),
        ("KWR-DWG-104", "socket", "Tail boom socket", "Printed ASA, 6 perimeters, 30 % infill", [
            "Block 94 long, 50 wide, 50 high with a 20 bore along its length.",
            "Glue to the rear wall and floor so the bore lines up with the rear wall hole.",
            "Saw a 2 mm slit along the top of the bore and fit one M4 x 30 clamp bolt across it.",
            "The tail boom slides in until it meets the rear wall's inside face plus 6.",
        ], [part("fus", "", "#ccc"), part("tail_boom", "", "#ccc")]),
        ("KWR-DWG-105", None, "Wing panel with aileron (make a left and a right)", "XPS foam 30 kg/m3, carbon spar tube 22 x 20, 80 g/m2 glass both sides, 3 mm ply root rib", [
            f"Hot-wire cut NACA 2412 cores: root chord {P['root_chord']:.0f}, tip chord {P['tip_chord']:.0f}, panel {P['panel_span']:,.0f} long.",
            "Keep the 30 % chord line straight: it is the spar line, square to the root rib.",
            f"Rout a 22 channel on the spar line and bond in the carbon spar, {P['panel_span'] - 20:,.0f} long, flush with the root.",
            "Set two 3 mm ply hardpoints in the lower skin over the boom pylon, 470 out from the centre line.",
            "Lay a 10 mm conduit from the pylon to the root for the boom wires; servo bay behind the spar.",
            "Glass both sides; glue the 3 mm ply root rib with the 20 joiner hole and an M5 insert at 70 % chord.",
            f"Cut the aileron free at 75 % chord from {P['aileron_y'][0]:.0f} to {P['aileron_y'][1]:.0f} out; hinge on tape.",
            "Make the left panel as a mirror image; the left panel also takes the pitot tube.",
        ], [part("fus", "", "#ccc"), part("joiner", "", "#ccc"), part("pylon_r", "", "#ccc")],
         Compound([m["wing_r"], m["ail_r"], m["spar_r"]])),
        ("KWR-DWG-106", "pylon_r", "Boom pylon (make 2)", "Printed ASA, 1.2 mm walls, 10 % gyroid infill", [
            f"Block {P['pylon_x'][1] - P['pylon_x'][0]:.0f} long, {P['pylon_w']:.0f} wide; top shaped to the wing lower skin at 470 out.",
            "Saddle on the bottom fits the 25 boom; the boom centre is 115 below the wing chord line.",
            f"Two 5.5 holes on the centre line, {P['pylon_bolts_x'][0] - P['pylon_x'][0]:.0f} and {P['pylon_bolts_x'][1] - P['pylon_x'][0]:.0f} from the front, with M5 nut pockets.",
            "Four M4 heat-set inserts in the underside for the clamp caps, 17 either side of the centre line.",
            "Print standing on its side; bond to the wing hardpoint with thickened epoxy, then fit the bolts.",
            "The pylon puts the rotor discs 81 below the wing-top plane: do not shorten it.",
        ], [part("wing_r", "", "#ccc"), part("boom_r", "", "#ccc")]),
        ("KWR-DWG-107", None, "Boom clamp cap (make 4)", "Printed ASA, solid", [
            f"Cap {P['clamp_x'][0][1] - P['clamp_x'][0][0]:.0f} long, {P['pylon_w']:.0f} wide, half-round 25 seat, 6 under the boom.",
            "Two 4.5 holes, 17 either side of the centre line, for M4 x 20 bolts into the pylon inserts.",
            "Line the seat with 1 mm rubber tape so the cap grips the boom without crushing it.",
        ], [part("boom_r", "", "#ccc"), part("pylon_r", "", "#ccc")], Compound(list(m["caps_r"].solids())[:1])),
        ("KWR-DWG-108", "boom_r", "Lift boom (make 2)", "Roll-wrapped carbon tube 25 x 23", [
            f"Cut to {D['boom_len']:,.0f} with a fine abrasive disc; seal the ends with thin epoxy.",
            f"Mark the motor centres {2 * P['motor_half_span']:,.0f} apart, {P['boom_overhang']:.0f} from each end.",
            "Mark the pylon centre half way between the motors; this is the balance point.",
            "Drill a 6 hole on the underside 150 inboard of each motor for the motor wires.",
            "Wrap the clamp areas with one turn of glass tape to spread the clamp load.",
        ], [part("pylon_r", "", "#ccc"), part("mounts_r", "", "#ccc")]),
        ("KWR-DWG-109", None, "Landing leg (make 4)", "Carbon rod 12 mm, printed ASA clamp and fairing, printed TPU foot", [
            f"Rod 12 mm, {zb - P['boom_od'] / 2 - 2 - 8:.0f} long; clamp grips the boom 70 inboard of each motor.",
            "Clamp: 30 long, 36 wide, split under the boom; two M3 bolts close it; 12 bore 20 deep for the rod.",
            "Fairing: elliptical 32 x 16, printed hollow, slides over the rod with its long axis fore and aft.",
            "Foot: 36 round, 10 thick, with a 20 deep socket for the rod; print in TPU.",
            "Glue the rod into the clamp and foot with epoxy; all four feet must touch a flat floor.",
        ], [part("boom_r", "", "#ccc")],
         Compound([list(m[k].solids())[0] for k in ("legclamps_r", "legrods_r", "legfair_r", "feet_r")])),
        ("KWR-DWG-110", "tail_boom", "Tail boom", "Pultruded carbon tube 20 x 17", [
            f"Cut to {P['tail_boom_x'][1] - P['tail_boom_x'][0]:.0f}; seal the ends.",
            "Front 94 goes into the socket; mark it and roughen it for grip.",
            "Rear 140 carries the tail mount; drill a 3 hole at its middle for the servo leads.",
            "Run the elevator and rudder leads inside the tube.",
        ], [part("socket", "", "#ccc"), part("tail_mount", "", "#ccc")]),
        ("KWR-DWG-111", "tail_mount", "Tail mount", "Printed ASA, 1.6 mm walls, 20 % infill", [
            "Block 140 long, 44 wide, bore 20 along the bottom, top shaped to the stabiliser's lower skin.",
            "A slot in the top takes the fin root through the stabiliser's centre.",
            "Split clamp under the bore with one M4 bolt; stabiliser and fin bond to it with epoxy.",
            "Square the stabiliser to the wing by eye from behind before the epoxy sets.",
        ], [part("tail_boom", "", "#ccc"), part("stab", "", "#ccc"), part("fin", "", "#ccc")]),
        ("KWR-DWG-112", "stab", "Horizontal stabiliser with elevator", "XPS foam, 80 g/m2 glass both sides", [
            f"NACA 0010 core, {P['stab_span']:.0f} span, {P['stab_chord']:.0f} chord, no taper.",
            "Glass both sides; cut the elevator free at 70 % chord, hinge on tape.",
            "Servo bay on the left of the centre; pushrod under the skin.",
        ], [part("tail_mount", "", "#ccc"), part("fin", "", "#ccc")]),
        ("KWR-DWG-113", "fin", "Fin with rudder", "XPS foam, 80 g/m2 glass both sides", [
            f"NACA 0010 core, root chord {P['fin_root']:.0f}, tip chord {P['fin_tip']:.0f}, {P['fin_h']:.0f} high; trailing edge straight.",
            "Root shaped to the top of the stabiliser; cut the rudder free at 70 % chord.",
            "Bond to the stabiliser and tail mount; check it is square to the stabiliser.",
        ], [part("stab", "", "#ccc"), part("tail_mount", "", "#ccc")]),
    ]
    for row in S:
        dwg, key, title, mat, notes, nb = row[:6]
        shape = row[6] if len(row) > 6 else m[key]
        pt = Part(title, shape, "#0F766E")
        component_sheet(pt, nb, "Kitewright Range", dwg, f"Kitewright Range: {title.lower()} making sketch", mat, notes, DATE)
        print("sheet", dwg)


# ---------------------------------------------------------------- joint close-ups
def do_joints():
    sx, sz = P["spar_x"], P["spar_z"]
    J = [
        ("joint-01.png", "Wing root: joiner, spar and wing bolt", "+Y", [
            Part("Fuselage side and doubler", win("fus", 300, 640, 0, 80, 280, 350), COL["ply"]),
            Part("Wing panel root", win("wing_r", 300, 640, 70, 200, 290, 350), COL["foam"]),
            Part("Spar", win("spar_r", 300, 640, 70, 200, 290, 350), COL["carbon"]),
            Part("Joiner tube", win("joiner", 300, 640, 0, 200, 290, 350), "#374151"),
            Part("Wing bolt", m["wing_bolts"] & box(500, 600, 0, 200, 300, 350), COL["steel"])]),
        ("joint-02.png", "Boom pylon: through-bolts and clamp caps", "+Y", [
            Part("Wing panel", win("wing_r", 320, 640, 420, 520, 290, 350), COL["foam"]),
            Part("Boom pylon", m["pylon_r"], COL["print"]),
            Part("Pylon bolts with washers", m["pbolts_r"], COL["steel"]),
            Part("Clamp caps", m["caps_r"], "#115E59"),
            Part("Lift boom", win("boom_r", 320, 540, 420, 520, 180, 230), COL["carbon"])]),
        ("joint-03.png", "Lift motor on the boom end", None, [
            Part("Lift boom", win("boom_r", mx0 - 45, mx0 + 170, 420, 520, 180, 230), COL["carbon"]),
            Part("Motor mount", m["mounts_r"] & box(mx0 - 30, mx0 + 30, 420, 520, 150, 260), COL["metal"]),
            Part("Lift motor", m["motors_r"] & box(mx0 - 40, mx0 + 40, 420, 520, 200, 300), COL["elec"]),
            Part("Propeller hub", m["props_r"] & box(mx0 - 60, mx0 + 60, 420, 520, 200, 300), "#374151"),
            Part("ESC under the boom", m["escs_r"] & box(mx0, mx0 + 200, 420, 520, 150, 200), "#7C3AED")]),
        ("joint-04.png", "Landing leg on the boom", "+Y", [
            Part("Lift boom", win("boom_r", lx0 - 40, lx0 + 40, 420, 520, 180, 230), COL["carbon"]),
            Part("Leg clamp", m["legclamps_r"] & box(lx0 - 20, lx0 + 20, 420, 520, 0, 240), COL["print"]),
            Part("Carbon rod", m["legrods_r"] & box(lx0 - 20, lx0 + 20, 420, 520, 0, 240), COL["carbon"]),
            Part("Fairing", m["legfair_r"] & box(lx0 - 20, lx0 + 20, 420, 520, 0, 240), COL["metal"]),
            Part("Foot", m["feet_r"] & box(lx0 - 20, lx0 + 20, 420, 520, 0, 240), COL["tpu"])]),
        ("joint-05.png", "Tail boom in its socket", "+Y", [
            Part("Fuselage rear", win("fus", 600, 760, -80, 80, 190, 350), COL["ply"]),
            Part("Tail boom socket", m["socket"], COL["print"]),
            Part("Tail boom", win("tail_boom", 640, 830, -20, 20, 280, 320), COL["carbon"])]),
        ("joint-06.png", "Tail mount, stabiliser and fin", None, [
            Part("Tail boom", win("tail_boom", 1300, 1510, -20, 20, 280, 320), COL["carbon"]),
            Part("Tail mount", m["tail_mount"], COL["print"]),
            Part("Stabiliser (centre)", win("stab", 1300, 1520, -160, 160, 300, 350), COL["foam"]),
            Part("Fin (root)", win("fin", 1300, 1520, -20, 20, 300, 450), "#E2E8F0")]),
        ("joint-07.png", "Nose cone and cruise motor", "+Y", [
            Part("Fuselage front", win("fus", -5, 120, -80, 80, 190, 350), COL["ply"]),
            Part("Nose cone", m["nose"], COL["print"]),
            Part("Cruise motor", m["cruise_motor"], COL["elec"]),
            Part("Folding propeller hub", m["cruise_prop"] & box(-130, -80, -40, 40, 230, 310), "#374151")]),
        ("joint-08.png", "Battery bays and Core avionics", "+Y", [
            Part("Fuselage (cut)", win("fus", 0, 600, -80, 80, 190, 350), COL["ply"]),
            Part("ColdCell packs", m["packs"], COL["pack"]),
            Part("Joiner tube", win("joiner", 380, 460, -70, 70, 300, 350), "#374151"),
            Part("Kitewright Core avionics", m["core"], COL["core"]),
            Part("Payload mount", m["mount_plate"], COL["metal"])]),
    ]
    for fn, title, cut, parts in J:
        joint(parts, OUT / fn, f"Kitewright Range: {title}", cut=cut)
        print("joint", fn)


# ---------------------------------------------------------------- assembly steps
def do_steps():
    G = lambda n, *keys, c="#0F766E", e=(0, 0, 0): Part(n, comp(*keys), c, None, e)  # noqa: E731
    fus = G("Fuselage box", "fus")
    sock = G("Tail boom socket", "socket", e=(0, 0, 200))
    nose = G("Nose cone", "nose", e=(-250, 0, 0))
    cru = G("Cruise motor and propeller", "cruise_motor", "cruise_prop", c=COL["elec"], e=(-300, 0, 0))
    core = G("Kitewright Core avionics", "core", c=COL["core"], e=(0, 0, 350))
    mnt = G("Payload mount", "mount_plate", c=COL["metal"], e=(0, 0, -200))
    tb = G("Tail boom", "tail_boom", c=COL["carbon"], e=(400, 0, 0))
    tail = G("Tail mount, stabiliser and fin", "tail_mount", "stab", "fin", c=COL["print"], e=(350, 0, 0))
    wr = G("Right wing panel", "wing_r", "ail_r", "spar_r", c="#CBD5E1")
    pyl = G("Boom pylon and two bolts", "pylon_r", "pbolts_r", e=(0, 0, -200))
    wings = G("Joiner, wing panels and wing bolts", "joiner", "wing_l", "wing_r", "ail_l", "ail_r", "spar_l", "spar_r",
              "wing_bolts", "pylon_l", "pylon_r", "pbolts_l", "pbolts_r", c="#0F766E", e=(0, 0, 400))
    joiner_n = G("Joiner and wing bolts", "joiner", "wing_bolts", c="#1F2937", e=(0, 0, 250))
    wl_n = G("Left wing panel with pylon", "wing_l", "ail_l", "spar_l", "pylon_l", "pbolts_l", c="#0F766E", e=(0, -450, 0))
    wr_n = G("Right wing panel with pylon", "wing_r", "ail_r", "spar_r", "pylon_r", "pbolts_r", c="#0F766E", e=(0, 450, 0))
    booms = G("Lift booms and clamp caps", "boom_l", "boom_r", "caps_l", "caps_r", c=COL["carbon"], e=(0, 0, -250))
    mot = G("Motor mounts, ESCs and lift motors", "mounts_l", "mounts_r", "escs_l", "escs_r", "motors_l", "motors_r",
            c=COL["elec"], e=(0, 0, 220))
    legs = G("Landing legs", "legclamps_l", "legclamps_r", "legrods_l", "legrods_r", "legfair_l", "legfair_r",
             "feet_l", "feet_r", c="#475569", e=(0, 0, -250))
    packs = G("ColdCell packs", "packs", c=COL["pack"], e=(0, 0, 350))
    hatch = G("Hatch and GNSS mast", "hatch", "gnss", c="#B45309", e=(0, 0, 350))
    props = G("Lift propellers and pitot", "props_l", "props_r", "pitot", c="#374151", e=(0, 0, 250))
    pay = G("Payload", "payload", c="#78716C", e=(0, 0, -250))
    S = [
        ("Tail boom socket into the fuselage", [fus], [sock]),
        ("Nose cone onto the firewall", [fus, sock], [nose]),
        ("Cruise motor and folding propeller onto the nose", [fus, sock, nose], [cru]),
        ("Kitewright Core avionics into the front bay", [fus, sock, nose, cru], [core]),
        ("Payload mount under the fuselage", [fus, sock, nose, cru, core], [mnt]),
        ("Tail boom into the socket", [fus, sock, nose, cru, core, mnt], [tb]),
        ("Tail mount, stabiliser and fin onto the boom", [fus, sock, nose, cru, core, mnt, tb], [tail]),
        ("Boom pylon onto each wing panel (right shown)", [wr], [pyl]),
        ("Joiner, then the wing panels slide on sideways", [fus, nose, cru, mnt, tb, tail], [joiner_n, wl_n, wr_n]),
        ("Lift booms into the pylons, clamp caps on", [fus, nose, cru, mnt, tb, tail, wings], [booms]),
        ("Motor mounts, ESCs and lift motors onto the booms", [fus, nose, cru, mnt, tb, tail, wings, booms], [mot]),
        ("Landing legs onto the booms", [fus, nose, cru, mnt, tb, tail, wings, booms, mot], [legs]),
        ("ColdCell packs into the bays", [fus, nose, cru, mnt, tb, tail, wings, booms, mot, legs], [packs]),
        ("Hatch and GNSS mast", [fus, nose, cru, mnt, tb, tail, wings, booms, mot, legs, packs], [hatch]),
        ("Lift propellers and pitot probe (at the propeller safety stop)", [fus, nose, cru, mnt, tb, tail, wings, booms, mot, legs, hatch], [props]),
        ("Payload onto the mount", [fus, nose, cru, tb, tail, wings, booms, mot, legs, hatch, props, mnt], [pay]),
    ]
    only = [int(a) for a in sys.argv[2:]] if len(sys.argv) > 2 else None
    for i, (title, done, new) in enumerate(S, 1):
        if only and i not in only:
            continue
        step(done, new, OUT / f"step-{i:02d}.png", f"Kitewright Range, step {i}: {title}", label_done=False)
        print("step", i)


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("overview", "all"):
        do_overview()
    if what in ("sheets", "all"):
        do_sheets()
    if what in ("joints", "all"):
        do_joints()
    if what in ("steps", "all"):
        do_steps()
