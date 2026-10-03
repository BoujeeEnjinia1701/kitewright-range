---
doc_id: KWR-BLD-001
title: Kitewright Range prototype build plan
project: Kitewright Range
doc_type: Build plan
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First build plan; design made constructable (KWR-DDR-002)
---

# Kitewright Range prototype build plan

**Plan, not yet built.** How to build the first proof-of-concept prototype of the Kitewright Range quadplane, component by component. Building and testing to it is TRL 4 work. Decisions still to be made are kept in the design decisions register (`docs/06-design-decisions.md`), not here.

> **Safety:** This aircraft has four 20 in lift propellers, a 14 in cruise propeller and two lithium-ion packs of about 290 Wh each. Propellers go on only at the propeller safety stop (section 6), the arming plug stays out whenever anyone handles the aircraft, and packs are charged only between 0 and 45 °C in a fire-resistant box.

## 1. What you are building

![Figure 1. Every component, pulled apart and numbered in build order](05-build-plan/overview.png)

*Figure 1. Every component, pulled apart and numbered in build order.*

A 2.5 m span quadplane of about 10.6 kg with its 1 kg payload. Thirteen components are made: the fuselage box and hatch from plywood; the two wing panels, the stabiliser and the fin from hot-wire cut foam skinned in glass; the lift booms and tail boom cut from carbon tube; and the nose cone, tail socket, pylons, clamp caps, landing legs and tail mount printed in ASA. Everything else is bought: the lift and cruise motors with their ESCs and propellers, the servos, the pitot, the Kitewright Core avionics with its payload mount, and two ColdCell packs. The parts cost is estimated at USD 3,945 in the bill of materials.

## 2. What changed to make it buildable

| Component | The concept had | The buildable design has | Why |
| --- | --- | --- | --- |
| Tail | Carried on the lift booms | A conventional tail on its own carbon boom behind the fuselage | Booms stay short enough for the 1.3 m cases; the rear rotor wash stays off the tail |
| Lift booms | "Below the wing", no fixing | Printed pylons under the wing, through-bolted, with the booms held by clamp caps; booms 470 mm out from the centre line | The rotor discs sit 81 mm below the wing-top plane and 38 mm clear of the cruise propeller; the booms come off |
| Lift motors | Positions not set | 506 mm ahead of and behind the balance point on each boom | The rotors lift through the balance point and clear the wing |
| Cruise motor | Pusher or tractor | Tractor at the nose with a folding propeller | Nothing to clear behind; the blades fold for landing |
| Wing | Removable halves | Two panels on a carbon joiner through the fuselage, one nylon bolt each | A stock tube and a field-proven fixing |
| Fuselage | A pod | A plywood box with the packs either side of the joiner and the avionics in front | Packs lift out with the wing fitted; balance does not change with the payload |
| Landing gear | None | Four faired legs on the booms | Stands level on rough ground with 83 mm under the payload |
| Wiring | Not shown | A conduit in each wing to a plug at the root | Boom power disconnects with the wing |

Every change is argued in decision record KWR-DDR-002.

## 3. Making the components

### 3.1 Fuselage box

![Figure 2. Fuselage box making sketch](../cad/drawings/KWR-DWG-101.png)

*Figure 2. Fuselage box making sketch (KWR-DWG-101).*

**What it is and what it is made from.** An open-topped box 750 mm long, 140 mm wide and 150 mm high. The sides, floor and two inner bulkheads are 3 mm poplar lite-ply; the firewall, the rear wall and two wing-root doublers are 6 mm birch ply. The outside is skinned in 80 g/m2 glass cloth.

**How to make it.**

1. Cut the two sides 750 x 150 mm and the floor 738 x 134 mm from 3 mm lite-ply; the firewall and rear wall 140 x 150 mm from 6 mm birch ply; two bulkheads 134 x 147 mm from 3 mm lite-ply.
2. Cut two doublers 200 x 52 mm from 6 mm birch ply. Glue one inside each side, 380 mm back from the front edge, with its top 3 mm below the side's top edge.
3. Clamp the two sides together and drill through both: a 20.5 mm hole 420 mm back and 20 mm down from the top edge (the wing joiner), and a 5.5 mm hole 544 mm back and 21 mm down (the wing bolt).
4. Drill a 20.5 mm hole in the rear wall on its centre line, 45 mm down from the top edge, for the tail boom.
5. Glue the box together on a flat board against a square: firewall at the front, rear wall at the back, bulkheads 252 mm and 585 mm behind the front face of the firewall.
6. Push a straight 20 mm rod through both joiner holes before the glue sets; it must slide freely and sit square to the sides.
7. Glue four M4 threaded inserts into the floor under the balance point, 414 mm behind the firewall, on the hole pattern of the payload mount bought.
8. Sand the outside, lay 80 g/m2 glass cloth in epoxy, and glue a 3 mm lip inside the top of the firewall for the hatch tongue.

**How it fits the parts next to it.** The wing joiner runs through both sides and doublers (Figure 3). The nose cone glues and bolts to the firewall, the tail socket to the rear wall, and the hatch sits on the side walls and bulkheads.

![Figure 3. Wing root joint](05-build-plan/joint-01.png)

*Figure 3. The joiner passes through the fuselage side and doubler into the spar; the nylon wing bolt goes from inside the fuselage into the root rib.*

**Check before moving on.** The box sits flat on a table without rocking; the rod slides through both joiner holes; the diagonals of the top opening match within 2 mm.

### 3.2 Hatch

![Figure 4. Hatch making sketch](../cad/drawings/KWR-DWG-102.png)

*Figure 4. Hatch making sketch (KWR-DWG-102).*

**What it is and what it is made from.** A 750 x 140 mm lid of 3 mm lite-ply that carries the GNSS mast and the arming switch.

**How to make it.**

1. Cut the plate 750 x 140 mm. Glue a 20 x 120 mm tongue under the front edge so it projects 10 mm forward.
2. Drill an 8.5 mm hole on the centre line 660 mm back from the front edge for the GNSS mast.
3. Cut the opening for the lockable arming switch beside the mast, to the switch bought.
4. Drill the back for one M4 nylon thumb screw and glue a captive nut under the rear wall's top edge to match.

**How it fits the parts next to it.** The tongue slides under the lip on the firewall; the back is held by the thumb screw. The mast plugs through the hole into a socket on the Core avionics tray.

**Check before moving on.** The hatch sits flat on all walls and comes off with the thumb screw alone.

### 3.3 Nose cone and cruise motor mount

![Figure 5. Nose cone making sketch](../cad/drawings/KWR-DWG-103.png)

*Figure 5. Nose cone making sketch (KWR-DWG-103).*

**What it is and what it is made from.** A printed ASA cone 55 mm long that blends the 140 x 150 mm fuselage face into a 60 mm round motor face on the fuselage centre line.

**How to make it.**

1. Print with the motor face on the bed, four perimeters, 10 % gyroid infill; no supports.
2. Set four M3 heat-set inserts in the motor face on the bolt circle of the cruise motor bought, and open a 15 mm hole in the centre for air and wires.
3. Drill four 4.5 mm holes through the back flange to match four holes in the firewall.

**How it fits the parts next to it.** The back face glues to the firewall with epoxy and four M4 bolts (Figure 6). The cruise motor bolts to the front face.

![Figure 6. Nose joint](05-build-plan/joint-07.png)

*Figure 6. Nose cone on the firewall and the cruise motor on its face, cut along the centre line.*

**Check before moving on.** A straightedge along the fuselage top and the motor axis are parallel; the motor face is square to the fuselage.

### 3.4 Tail boom socket

![Figure 7. Tail boom socket making sketch](../cad/drawings/KWR-DWG-104.png)

*Figure 7. Tail boom socket making sketch (KWR-DWG-104).*

**What it is and what it is made from.** A printed ASA block 94 x 50 x 50 mm with a 20 mm bore that holds the tail boom inside the back of the fuselage.

**How to make it.**

1. Print standing on its end, six perimeters, 30 % infill.
2. Saw a 2 mm slit along the top of the bore; drill across it for one M4 x 30 bolt and a nut.

**How it fits the parts next to it.** It glues to the rear wall and the floor with its bore lined up on the rear wall hole (Figure 8). The boom slides through the rear wall into the bore and the bolt clamps it.

![Figure 8. Tail boom socket joint](05-build-plan/joint-05.png)

*Figure 8. Tail boom through the rear wall into the socket, cut along the centre line.*

**Check before moving on.** A 20 mm rod in the bore points straight back along the fuselage centre line, seen from above and from the side.

### 3.5 Wing panels (make a left and a right)

![Figure 9. Wing panel making sketch](../cad/drawings/KWR-DWG-105.png)

*Figure 9. Wing panel making sketch (KWR-DWG-105); the left panel is its mirror image.*

**What it is and what it is made from.** Each panel is 1,180 mm long, NACA 2412 section, 310 mm chord at the root and 250 mm at the tip. It is cut from 30 kg/m3 XPS foam, skinned both sides in 80 g/m2 glass, with a carbon spar 22 mm outside and 20 mm inside along the 30 % chord line, a 3 mm plywood root rib, two plywood hardpoints for the pylon and an aileron.

**How to make it.**

1. Hot-wire cut the core with root and tip templates, keeping the 30 % chord line straight and square to the root: it is the spar line.
2. Rout a 22 mm channel on the spar line and bond in the spar, cut to 1,160 mm, flush with the root.
3. Let two 3 mm plywood hardpoints, 60 x 50 mm, into the lower surface 470 mm from the aircraft centre line (400 mm from the root), one 40 mm ahead of the spar and one 60 mm behind it.
4. Lay a 10 mm conduit from the hardpoints to the root, and cut the aileron servo bay behind the spar.
5. Glass both sides in epoxy under vacuum or with peel ply.
6. Glue on the 3 mm plywood root rib, drilled 20.5 mm on the spar line and fitted with an M5 threaded insert at 70 % chord.
7. Cut the aileron free along the 75 % chord line from 700 mm to 1,230 mm out, and hinge it on tape.
8. For the left panel only: drill a 6 mm hole into the leading edge 800 mm out for the pitot tube.

**How it fits the parts next to it.** The joiner slides 250 mm into the spar; the root rib meets the fuselage side face to face, and the wing bolt pulls it tight (Figure 3). The boom pylon bolts under the hardpoints.

**Check before moving on.** Panel mass about 0.57 kg with spar and aileron; the spar bore takes the joiner; both panels have the same twist, checked with an incidence meter at root and tip.

### 3.6 Boom pylons (make 2)

![Figure 10. Boom pylon making sketch](../cad/drawings/KWR-DWG-106.png)

*Figure 10. Boom pylon making sketch (KWR-DWG-106).*

**What it is and what it is made from.** A printed ASA block 160 mm long and 44 mm wide whose top follows the wing's lower skin and whose bottom is a half-round saddle for the 25 mm boom. It holds the boom 115 mm below the wing chord line.

**How to make it.**

1. Print on its side, 1.2 mm walls, 10 % gyroid infill.
2. Set four M4 heat-set inserts in the underside, 17 mm either side of the centre line, under each clamp cap.
3. Open the two 5.5 mm bolt holes, 30 mm and 130 mm from the front, and press an M5 nut into each nut pocket.

**How it fits the parts next to it.** It bonds to the hardpoints with thickened epoxy, and two M5 x 90 bolts come down through the wing from large washers on the upper skin into its nuts (Figure 11). The boom sits in the saddle, held by two clamp caps.

![Figure 11. Pylon joint](05-build-plan/joint-02.png)

*Figure 11. Pylon under the wing with its two through-bolts, and the boom held by two clamp caps, cut along the boom.*

**Check before moving on.** Both pylons are at the same distance from the root and their saddles are parallel to the fuselage, checked with a straight rod in each.

### 3.7 Boom clamp caps (make 4)

![Figure 12. Clamp cap making sketch](../cad/drawings/KWR-DWG-107.png)

*Figure 12. Clamp cap making sketch (KWR-DWG-107).*

**What it is and what it is made from.** A solid printed ASA cap 26 mm long and 44 mm wide with a half-round 25 mm seat, 6 mm thick under the boom.

**How to make it.** Print flat, 100 % infill. Drill two 4.5 mm holes 17 mm either side of the centre line. Line the seat with 1 mm rubber tape.

**How it fits the parts next to it.** Two M4 x 20 bolts pull it up into the pylon inserts, squeezing the boom into the saddle (Figure 11). Tighten until the boom will not turn by hand; do not crush the tube.

**Check before moving on.** The cap closes with a gap of about 1 mm to the pylon, so it grips before it bottoms.

### 3.8 Lift booms (make 2)

![Figure 13. Lift boom making sketch](../cad/drawings/KWR-DWG-108.png)

*Figure 13. Lift boom making sketch (KWR-DWG-108).*

**What it is and what it is made from.** Roll-wrapped carbon tube 25 mm outside, 23 mm inside, 1,092 mm long.

**How to make it.**

1. Cut to 1,092 mm with a fine abrasive disc; seal the ends with thin epoxy.
2. Mark the two motor centres 1,012 mm apart, 40 mm in from each end, and the pylon centre half way between them.
3. Drill a 6 mm hole on the underside 150 mm inboard of each motor for the motor wires.
4. Wrap the two clamp areas with one turn of glass tape.

**How it fits the parts next to it.** The middle sits in the pylon saddle; the motor mounts clamp each end (Figure 14); the landing legs clamp 70 mm inboard of each motor.

![Figure 14. Lift motor joint](05-build-plan/joint-03.png)

*Figure 14. Lift motor on its tube clamp mount at the boom end, with the ESC strapped under the boom.*

**Check before moving on.** With the boom in the pylon, the motor marks are the same distance ahead of and behind the pylon centre within 2 mm.

### 3.9 Landing legs (make 4)

![Figure 15. Landing leg making sketch](../cad/drawings/KWR-DWG-109.png)

*Figure 15. Landing leg making sketch (KWR-DWG-109).*

**What it is and what it is made from.** A 12 mm carbon rod in a printed elliptical fairing 32 x 16 mm, with a printed ASA clamp on the boom and a printed TPU foot 36 mm across.

**How to make it.**

1. Cut the rod to 182 mm.
2. Print the clamp (split under the boom, two M3 bolts, 12 mm socket 20 mm deep), the hollow fairing and the TPU foot (20 mm socket).
3. Glue the rod into the clamp and foot with epoxy, with the fairing between them, its long axis fore and aft.

**How it fits the parts next to it.** The clamp closes round the boom 70 mm inboard of each motor (Figure 16).

![Figure 16. Landing leg joint](05-build-plan/joint-04.png)

*Figure 16. Landing leg clamp on the boom, rod inside its fairing, foot at the bottom; cut along the boom.*

**Check before moving on.** All four feet touch a flat floor at once; the aircraft does not rock.

### 3.10 Tail boom

![Figure 17. Tail boom making sketch](../cad/drawings/KWR-DWG-110.png)

*Figure 17. Tail boom making sketch (KWR-DWG-110).*

**What it is and what it is made from.** Pultruded carbon tube 20 mm outside, 17 mm inside, 850 mm long.

**How to make it.** Cut to length and seal the ends. Roughen the front 94 mm for the socket. Drill a 3 mm hole 70 mm from the back end for the servo leads, which run inside the tube.

**How it fits the parts next to it.** The front goes through the rear wall into the socket (Figure 8); the back carries the tail mount.

**Check before moving on.** The tube is straight: rolled on a flat table, it does not wobble.

### 3.11 Tail mount

![Figure 18. Tail mount making sketch](../cad/drawings/KWR-DWG-111.png)

*Figure 18. Tail mount making sketch (KWR-DWG-111).*

**What it is and what it is made from.** A printed ASA block 140 mm long and 44 mm wide with a 20 mm bore along its bottom; its top is shaped to the stabiliser's lower skin, with a slot for the fin root.

**How to make it.** Print on its side, 1.6 mm walls, 20 % infill. Saw a slit under the bore and drill for one M4 clamp bolt.

**How it fits the parts next to it.** It clamps the end of the tail boom; the stabiliser and fin bond to it with epoxy (Figure 19).

![Figure 19. Tail mount joint](05-build-plan/joint-06.png)

*Figure 19. Stabiliser and fin bonded to the tail mount on the end of the tail boom.*

**Check before moving on.** Seen from behind with the fuselage level, the mount's top is level.

### 3.12 Horizontal stabiliser with elevator

![Figure 20. Stabiliser making sketch](../cad/drawings/KWR-DWG-112.png)

*Figure 20. Stabiliser making sketch (KWR-DWG-112).*

**What it is and what it is made from.** A NACA 0010 foam core 640 x 170 mm, glass both sides, with an elevator.

**How to make it.** Hot-wire cut the core, cut the servo bay left of centre, glass both sides, cut the elevator free at 70 % chord and hinge it on tape.

**How it fits the parts next to it.** It bonds onto the tail mount, centred, square to the tail boom.

**Check before moving on.** Tip to tip it is level with the wing when viewed from behind.

### 3.13 Fin with rudder

![Figure 21. Fin making sketch](../cad/drawings/KWR-DWG-113.png)

*Figure 21. Fin making sketch (KWR-DWG-113).*

**What it is and what it is made from.** A NACA 0010 foam core 300 mm high, 170 mm chord at the root and 130 mm at the tip, glass both sides, with a rudder.

**How to make it.** Hot-wire cut the core with its root shaped to the stabiliser top, glass it, cut the rudder free at 70 % chord and hinge it on tape.

**How it fits the parts next to it.** It bonds through the slot onto the stabiliser and the tail mount (Figure 19).

**Check before moving on.** It is square to the stabiliser, checked with a set square.

### 3.14 Bought components

| Component | What to buy | What to do to it |
| --- | --- | --- |
| Wing spars and joiner | Pultruded carbon tube 22 x 20 mm; roll-wrapped carbon tube 20 x 16 mm, 640 mm | Cut the spars to 1,160 mm; check the joiner slides into the spars |
| Wing bolts, pylon bolts | M5 x 40 nylon cap screws; M5 x 90 stainless cap screws with 15 mm washers | None |
| Lift motor mounts | Aluminium mounts that clamp a 25 mm tube | Drill the top plate to the motor's bolt pattern |
| Lift ESCs | 60 A, 6S, open firmware, rated to -20 °C | Extend the leads to the boom root plug |
| Lift motors and propellers | 5212-class, 340 KV, 6S; 20 x 6.5 in carbon, two of each hand | Balance every propeller |
| Cruise motor, ESC and propeller | 4120-class, 400 KV with a 60 A ESC; 14 x 10 in folding blades on a 36 mm spinner | None |
| Servos | Metal-gear digital, 20 mm class, rated to -20 °C | Fit in the servo bays with pushrods |
| Heated pitot | 6 mm probe with heater and airspeed sensor | Glue the tube into the left wing hole |
| Kitewright Core avionics and payload mount | To the Kitewright Core design | None |
| ColdCell packs | Two 6S3P Li-ion packs, to the ColdCell design | None |
| Harness | 10 and 12 AWG silicone wire, XT90 and XT60, root plugs, arming plug | Make to the Core wiring diagram |

## 4. Putting it together

### Step 1: tail boom socket into the fuselage

![Step 1](05-build-plan/step-01.png)

*Figure 22. Step 1.* Glue the socket to the rear wall and floor with its bore on the rear wall hole. Hold the bore in line with a rod until the epoxy sets.

### Step 2: nose cone onto the firewall

![Step 2](05-build-plan/step-02.png)

*Figure 23. Step 2.* Epoxy and four M4 bolts through the firewall.

### Step 3: cruise motor and folding propeller

![Step 3](05-build-plan/step-03.png)

*Figure 24. Step 3.* Four M3 bolts with threadlock into the nose cone inserts. Fit the spinner and yoke; leave the blades off until the propeller safety stop.

### Step 4: Kitewright Core avionics into the front bay

![Step 4](05-build-plan/step-04.png)

*Figure 25. Step 4.* Fit the avionics tray between the firewall and the first bulkhead on soft mounts; run the harness to both battery bays, the wing root plugs and the tail.

### Step 5: payload mount under the fuselage

![Step 5](05-build-plan/step-05.png)

*Figure 26. Step 5.* Four M4 bolts into the floor inserts; the connector lead passes through the floor to the Core.

### Step 6: tail boom into the socket

![Step 6](05-build-plan/step-06.png)

*Figure 27. Step 6.* Slide the boom through the rear wall into the socket and tighten the clamp bolt, with the servo-lead hole facing up.

### Step 7: tail mount, stabiliser and fin

![Step 7](05-build-plan/step-07.png)

*Figure 28. Step 7.* Clamp the tail mount on the boom end and bond the stabiliser and fin to it. Hold point: from behind, the stabiliser is parallel to the fuselage floor and the fin is upright.

### Step 8: boom pylon onto each wing panel

![Step 8](05-build-plan/step-08.png)

*Figure 29. Step 8.* Bond each pylon to its hardpoints, then fit the two M5 bolts from the top with washers. Let the epoxy cure for 24 hours.

### Step 9: joiner, then the wing panels

![Step 9](05-build-plan/step-09.png)

*Figure 30. Step 9.* Slide the joiner through the fuselage, push each panel onto it until the root rib meets the fuselage side, and fit the nylon wing bolts from inside. Connect the boom root plugs.

### Step 10: lift booms into the pylons

![Step 10](05-build-plan/step-10.png)

*Figure 31. Step 10.* Lay each boom in its saddle with its centre mark on the pylon centre and fit the two clamp caps.

### Step 11: motor mounts, ESCs and lift motors

![Step 11](05-build-plan/step-11.png)

*Figure 32. Step 11.* Clamp the motor mounts at the marks with the top plates level, bolt on the motors (front left and rear right turn one way, the other two the other way, to the PX4 quadplane layout), strap the ESCs under the boom and run the wires through the 6 mm holes into the boom.

### Step 12: landing legs

![Step 12](05-build-plan/step-12.png)

*Figure 33. Step 12.* Clamp the legs 70 mm inboard of each motor with the fairings fore and aft.

### Step 13: ColdCell packs into the bays

![Step 13](05-build-plan/step-13.png)

*Figure 34. Step 13.* One pack in front of the joiner and one behind it, each held by a hook-and-loop strap through the floor. Leave the arming plug out.

### Step 14: hatch and GNSS mast

![Step 14](05-build-plan/step-14.png)

*Figure 35. Step 14.* Slide the hatch tongue under the firewall lip, fit the thumb screw and plug the GNSS mast through the hatch.

### Step 15: lift propellers and pitot probe

![Step 15](05-build-plan/step-15.png)

*Figure 36. Step 15.* Only at the propeller safety stop (section 6). Fit each propeller to the hand of its motor and the cruise blades to the yoke; glue the pitot tube into the left wing.

### Step 16: payload onto the mount

![Step 16](05-build-plan/step-16.png)

*Figure 37. Step 16.* Slide the payload onto the rail until the locking pin shows, and plug its connector.

## 5. First checks

| Check | Requirement | How | Pass when |
| --- | --- | --- | --- |
| Weigh and balance with and without the 1 kg payload | R4, R7 | Scales under the feet; balance point on the wing | Balance point within 26 % to 31 % of the mean chord both ways; mass recorded |
| Design-around geometry | R9 | Measure from a straightedge across the wing top to each propeller | Every rotor disc at least 70 mm below the wing-top plane |
| Pack and case | R8 | Pack the aircraft into its two cases | Every part fits; each case under the target mass |
| Control surface throws | R6 | Radio check with the arming plug out | Each surface moves the right way with no binding |
| Cold soak of servos and ESCs | R5 | Chamber soak at -20 °C, then function check, propellers off | Every servo and ESC works |
| Motor run, propellers off | R1 | Arm with the aircraft tied down and propellers off | Each motor turns the right way for its position |
| Tied hover thrust | R1 | AltiRig data at 5,000 m density, then a tied hover at the build site | Measured thrust margin recorded for the as-built mass |

These checks are listed here; a TRL 4 test report records them.

## 6. Safety stops

> **Safety:** Work stops at each point below until what is listed is true.

1. **Before the first power-up:** the arming plug is out, no propeller is fitted, a fire extinguisher for lithium fires and a fire-resistant box are at hand, and the packs have been charged between 0 and 45 °C pack temperature.
2. **Before any motor runs:** the aircraft is tied down to a bench, propellers off, the lockable arming switch works, and the PX4 failsafes (loss of link, low battery, geofence) are set and checked on the ground station.
3. **Propeller safety stop, before any propeller goes on:** every person is outside a 15 m keep-out zone during arming, the aircraft is tied to ground anchors, the motor directions are confirmed, and every propeller is balanced and checked for cracks.
4. **Before the first free hover:** ten logged tied hovers with no fault, the wing spar proof-loaded (TRL 4), the measured thrust margin known, and the site cleared with the landowner and local aviation rules.
5. **After any hard landing or crash:** remove the arming plug, move the packs outdoors to a safe area, and treat them as damaged until checked.

## 7. Tools, skills and workspace

- Hot-wire foam cutter with root and tip templates; vacuum bagging or peel ply for glassing; epoxy, scales and mixing gear.
- Fine-tooth saw, abrasive disc for carbon tube, drill press or guide, 20.5 mm and 5.5 mm drills, heat-set insert tip.
- 3D printer that prints ASA and TPU, with an enclosure.
- Soldering for 10 AWG wire and XT90 connectors; a multimeter.
- A 2.6 m flat bench, a well-ventilated room for epoxy and carbon dust (wear a dust mask), and an outdoor area for powered tests.
- Skills: model aircraft building, multirotor wiring, PX4 setup with a ground station.

## 8. Where the numbers come from

- Model and constructability checks: `cad/src/model.py`; STEP and STL in `cad/step/` and `cad/stl/`.
- General arrangement: `cad/drawings/KWR-DWG-001`; making sketches `cad/drawings/KWR-DWG-101` to `KWR-DWG-113`.
- Pictures: `cad/src/build_plan_media.py`, written to `docs/05-build-plan/`.
- Calculations: `docs/04-calcs/01-sizing.md` (KWR-CAL-001) and `docs/04-calcs/sizing.py`.
- Bill of materials: `bom/bom.csv`.
- Decisions: `docs/decisions/0001-trl2-review-decisions.md`, `docs/decisions/0002-design-for-construction.md` and `docs/06-design-decisions.md`.
