---
doc_id: KWR-CAL-001
title: Kitewright Range sizing calculations
project: Kitewright Range
doc_type: Calculation
version: "0.4"
status: Draft
date: '2026-10-04'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First issue for TRL 3 (mass and balance, aerodynamics, hover at 5,000 m, energy and endurance, structure, design-around geometry, transport, cost)
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: Design for construction (KWR-DDR-002) applied; masses from the constructable model; options for the requirements not met
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: 'Amish''s 2026-10-03 decisions applied (KWR-DDR-003; Amish: "i agree with all the 46 recommendations you provided. please proceed."): 22 in propellers on 5215-class motors, booms 50 mm longer and 20 mm further out, 5.0 Ah cells in the same two packs, airframe kept, Kitewright Core power leads now supplied by Range'
- version: "0.4"
  date: '2026-10-04'
  author: Amish Chadha
  change: 'Amish''s round-3 decision 10A applied (KWR-DDR-004; Amish: "For round 3, I agree with all your proposed recommendations"): the Kitewright Core to the family envelope under the fuselage floor at the centre of gravity (0.99 kg), fuselage 156 mm wide, Core deck doubler, packs moved, AS150 on the packs; every section re-run'
---

# Kitewright Range sizing calculations

On paper, Kitewright Range takes off and lands vertically at 5,000 m with a 48.3 % thrust margin and flies 30.6 min and 41.5 km on the wing with a 1 kg payload and a 20 % reserve, at a take-off mass of 11.35 kg. This version carries Amish's round-3 decision 10A of 2026-10-04 (KWR-DDR-004: "For round 3, I agree with all your proposed recommendations"): Range is recomputed with the 0.99 kg Kitewright Core, hung under the fuselage floor at the centre of gravity to the family mounting envelope (the Core's drawing is the reference), with AS150 plugs on the packs. The 2026-10-03 decisions (KWR-DDR-003) stand. Eight requirements are met on paper or by design; endurance (R2, 30.6 min against 45 min) and take-off mass (R7, 11.35 kg against 8 kg) are not met, as Amish accepted for the first prototype. The estimated cost is USD 4,314 against the USD 5,000 value-engineering target (USD 686 under).

## Scope and method

The script `docs/04-calcs/sizing.py` reads the constructable geometry from `cad/src/model.py`, takes the mass of every made part from its modelled volume and surface area, adds the bought parts, and works out balance, drag, cruise and hover power, energy per flight, structural margins and cost. It writes `docs/04-calcs/results.csv`. All figures are first-order estimates for TRL 3; motor and propeller data must be measured in AltiRig at 5,000 m air density before any flight.

## Assumptions

Table 1. Assumptions

| Quantity | Value | Basis |
| --- | --- | --- |
| Air density at 5,000 m | 0.736 kg/m3 | ISA (R1 uses 0.74 kg/m3) |
| Wing | NACA 2412, 0.704 m2, span 2.50 m, aspect ratio 8.9 | Model |
| Maximum lift coefficient | 1.30 | Plain ailerons, Reynolds number about 3 x 10^5 |
| Oswald factor | 0.75 | Booms and pylons disturb the span loading |
| Skin friction, form factors | Cf 0.006; wing 1.25, tail 1.20; interference 1.15 | Hand-book build-up |
| Lift thrust per motor at sea level | 68.7 N (7.0 kgf) | Maker class figure for a 5215-class motor with a 22 x 7 in propeller on 6S (KWR-DDR-003); to be measured |
| Thrust at altitude | Sea-level thrust x density ratio (0.601) | Conservative: ignores the higher rpm a lighter load gives |
| Hover figure of merit, drive efficiency | 0.65, 0.82 | Typical for 20 to 22 in carbon propellers and open ESCs |
| Cruise propeller and drive efficiency | 0.65 and 0.85 (0.55 combined) | 14 x 10 in folding propeller at 22 m/s |
| ColdCell packs | Two packs, 6S3P Li-ion high-rate 21700 cells of 5.0 Ah, 324.0 Wh and 1.40 kg each, AS150 leads | Range's figure in the Kitewright interface table (ColdCell has not yet drawn this pack); 5.0 Ah cells per KWR-DDR-003 |
| Usable energy | 90 % depth of discharge x 95 % for cold, packs warmed before take-off | ColdCell heater keeps the cells above 15 °C |
| Reserve | 20 % of usable energy kept for landing | R2 |
| Kitewright Core | 0.99 kg with its rail and pins, at the centre of gravity under the floor; its GNSS receiver on the hatch mast (0.03 kg) and antennas on extension leads (0.03 kg) | Core R9; the Kitewright interface table of 2026-10-04 (decision 10A) |
| Kitewright Core power leads | 0.124 kg at the rear of the Core | Core decision 33B moves them to the frame; Core BOM line 21 |
| Systems power | 38 W: avionics 15, payload 10, pack heaters in flight 10, servos 3 | Estimate |
| Vertical phases | 125 s at hover power plus 20 % for transitions | Take-off, two transitions, landing |
| Climb | 400 m at 2.5 m/s on the wing | Launch site to survey height |
| Limit load factor | 2.5 g | Gusts and turns in valley wind |
| Carbon tube allowable bending stress | 600 MPa | Pultruded and roll-wrapped tube |
| Printed parts | ASA, 1,070 kg/m3, walls and infill per part | `sizing.py` |

## A. Mass and balance (R4, R7)

Take-off mass is 11.35 kg, of which the payload is 1.00 kg and the two ColdCell packs 2.80 kg. The largest made parts are the fuselage box (0.83 kg), the two wing panels with spars and ailerons (0.57 kg each) and the two boom pylons (0.14 kg each). The four 5215-class lift motors weigh 1.14 kg and the lift system with propellers, mounts and ESCs 1.68 kg. The Kitewright Core weighs 0.99 kg with its rail and pins; the Core power leads add 0.12 kg.

Against v0.3 (11.07 kg) the reconciliation adds 0.28 kg: the Core, GNSS and payload mount 0.15 kg (0.99 kg of Core, 0.03 kg of hatch mast and 0.03 kg of antenna leads against the 0.70, 0.08 and 0.12 kg assumed before), the 6 mm birch Core deck doubler 0.09 kg, and the fuselage 16 mm wider 0.04 kg.

The Core hangs under the floor at the centre of gravity, so the payload on its shoe sits there too, and fitting or removing the 1 kg payload does not move the centre of gravity (R4). To balance the Core's move from the front bay, the front pack now sits in the nose bay (60 to 198 mm behind the firewall) and the rear pack on the doubler behind the Core's lid (506 to 644 mm), with the rear bulkhead moved from 585 to 645 mm. The centre of gravity is 415 mm behind the firewall, at 28.3 % of the 281 mm mean chord, 1 mm behind the target.

## B. Aerodynamics and cruise (R2, R3, R6)

Table 2. Drag areas at cruise

| Item | CdA (m2) |
| --- | --- |
| Lift motors, mounts and ESCs (stopped) | 0.0129 |
| Wing | 0.0109 |
| Fuselage and nose, 156 x 150 mm | 0.0082 |
| Payload, 88 x 100 mm | 0.0035 |
| Leg fairings and feet | 0.0034 |
| Kitewright Core underside: plate, rail and shoe edge (0.150 x 0.024 m) and two pin knobs | 0.0027 |
| Pylons | 0.0024 |
| Tail surfaces | 0.0023 |
| Booms, stopped propellers, mast, pitot and tail boom | 0.0051 |
| Total with 15 % interference | 0.0591 |

The zero-lift drag coefficient is 0.083 (0.079 in v0.3): the Core hung under the floor and the wider fuselage add 0.0033 m2. Wing loading is 157 N/m2 and the stall speed at 5,000 m is 18.1 m/s. The lowest-power speed above 1.25 times stall is 22.6 m/s at a lift coefficient of 0.83 and a lift-to-drag ratio of 7.2. The air needs 353 W, which is 676 W from the packs with the propeller, drive and 38 W of systems.

Wind (R6): cruise at 22.6 m/s is well above a 14 m/s gust. In hover a 14 m/s side gust needs a tilt of about 9 degrees, inside the authority left by the hover margin.

## C. Hover at 5,000 m (R1)

The four 22 in rotors sweep 0.981 m2, a disc loading of 114 N/m2. The packs supply 1,835 W in hover (85 A at 21.6 V, 14.2 A per cell, inside the high-rate cells' rating). Maximum thrust at altitude is 4 x 68.7 N x 0.601 = 165.1 N against a weight of 111.3 N: a **48.3 % thrust margin**. At sea level the same rotors hover at 41 % of maximum thrust.

## D. Energy, endurance and range (R2, R3)

Table 3. Energy per flight at 5,000 m

| Stage | Wh |
| --- | --- |
| Two packs, nominal | 648 |
| Usable with packs warmed | 554 |
| Kept as 20 % reserve | 111 |
| Hover, transitions | 76 |
| Climb 400 m | 22 |
| Left for cruise | 344 |

At 676 W the cruise energy gives **30.6 min** on the wing and **41.5 km** of survey track at 22.6 m/s. Against v0.3 (32.9 min) the 0.99 kg Core's extra mass alone costs about 0.5 min, the doubler, wider fuselage and leads about 1.0 min, and the drag of the Core under the floor and the wider fuselage about 1.2 min. LakeWatch plans its surveys on this figure (its R5, restated on 2026-10-04).

## E. Structure

Table 4. Bending checks at limit load

| Item | Load case | Moment | Safety factor on 600 MPa |
| --- | --- | --- | --- |
| Wing spar 22 x 20 at the root | 2.5 g, lift centroid at 45 % of the panel | 73.9 N m | 2.7 |
| Joiner 20 x 16 inside the spars | Same | 73.9 N m | 3.8 |
| Lift boom 25 x 23 at the pylon edge | One 5215-class motor at sea-level full thrust (68.7 N) | 31.0 N m | 8.4 |
| Tail boom 20 x 17 | Stabiliser load of 15 % of weight at 2.5 g | 40.5 N m | 5.6 |
| Pylon bolts, two M5 per pylon | Both motors at full thrust plus one motor alone | 434 N | 9.9 on 4.3 kN proof |

All margins are above 2. The wing spar is the tightest and is checked again with a proof load at TRL 4.

## F. Geometry rules (R8, R9)

With the booms at 490 mm from the centre line and the motors 531 mm ahead of and behind the centre of gravity, the 22 in rotor discs sit 77 mm below the wing-top plane (the rule is at least 70 mm), the front discs clear the leading edge by 171 mm and the rear discs the trailing edge by 44 mm, the lift discs clear the cruise propeller disc by 33 mm (the model's rule is 20 mm), the fuselage side by 133 mm and the stabiliser by 110 mm. The Kitewright Core's pin knobs are 140 mm and the payload 80 mm above the ground on the landing feet. Motors are fixed and do not tilt, there is one wing, and the aircraft is not a tail-sitter. The longest part is a wing panel at 1,205 mm with its root fittings, then the lift boom at 1,142 mm; all fit 1.3 m cases. Tail volume coefficients are 0.53 (horizontal) and 0.025 (vertical).

## G. Cost (R10)

Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 4,314 (USD 686 under the target), including Range's share of the Kitewright Core (USD 900 and USD 60 for its rail), two ColdCell packs of 5.0 Ah cells (USD 700) and two transport cases (USD 360), excluding the payload. Decision 10A adds USD 21: the wider fuselage sheets USD 2, the doubler and T-nuts USD 4 and the antenna extension leads USD 15; the AS150 plugs cost the same class as the XT90s.

## H. Decisions taken and the options left

Amish decided the four options of KWR-CAL-001 v0.2 on 2026-10-03 ("i agree with all the 46 recommendations you provided. please proceed."): R1 option B (22 in propellers on 5215-class motors), R2 and R3 option A (5.0 Ah cells in the same packs), R7 option A (keep the airframe, weigh it at TRL 4). Table 5 gives the design as it now stands and the options that remain for R2 and R7 for a second prototype, worked out with the same script.

Table 5. Design as decided and the options left (changes from the design as it stands)

| Option | Take-off mass | Hover margin | Endurance | Range | Cost change |
| --- | --- | --- | --- | --- | --- |
| Design as decided (KWR-DDR-003, KWR-DDR-004) | 11.35 kg | 48.3 % | 30.6 min | 41.5 km | USD 0 |
| Two 6S4P packs of 5.0 Ah cells | 12.23 kg | 37.6 % | 38.4 min | 54.2 km | +USD 240 |
| Moulded carbon wing, tail and fuselage | 10.66 kg | 57.9 % | 34.2 min | 45.1 km | +USD 1,200 |
| Moulded airframe and two 6S4P packs | 11.54 kg | 45.9 % | 42.5 min | 58.2 km | +USD 1,440 |

With the reconciled Core no line meets R2 on paper any more; the last comes closest (42.5 min, USD 5,754 in all). It remains the second-prototype path once the first prototype's drag and mass are measured. Table 5 of v0.3 is superseded.

## L. Results against every requirement

Table 6. Results

| ID | Result | Status |
| --- | --- | --- |
| R1 | 48.3 % thrust margin at 0.736 kg/m3 and 11.35 kg, on maker-class thrust | Met on paper: 18 points above the line; to measure in AltiRig |
| R2 | 30.6 min on the wing at 5,000 m with 1 kg and 20 % reserve | **Not met** (accepted for the first prototype, KWR-DDR-003) |
| R3 | 41.5 km of survey track | Met on paper: 4 % above the line |
| R4 | 1 kg on the Core's payload shoe under the CG; CG 28.3 % of the mean chord with or without it | Met by design |
| R5 | All electronics and servos specified to -20 °C or tested cold; packs heated | Met on paper; to confirm when parts are bought |
| R6 | 22.4 m/s cruise against 14 m/s gusts; about 9 degrees of tilt to hold a side gust in hover | Met on paper |
| R7 | 11.35 kg take-off mass | **Not met** (airframe kept and weighed at TRL 4, KWR-DDR-003) |
| R8 | Longest part 1,205 mm; two cases about 9 kg and 12.5 kg | Met by design |
| R9 | Fixed motors, one wing, discs 77 mm below the wing-top plane | Met by design |
| R10 | USD 4,314; every part bought or made with hobby tools | Met on paper; USD 686 under the value-engineering target |

## Checks against the TRL 2 figures

The precis estimated a take-off mass near 8 kg and the problem statement assumed hover time near 47 % of sea level at 5,000 m. The constructable design is 3.4 kg heavier than that estimate: the ColdCell packs alone are 2.8 kg for 648 Wh, and the 22 in lift system with its mounts and ESCs is 1.7 kg. That is why R2 and R7 are missed together: more energy costs mass, and less mass costs energy.
