---
doc_id: KWR-CAL-001
title: Kitewright Range sizing calculations
project: Kitewright Range
doc_type: Calculation
version: "0.4"
status: Draft
date: '2026-10-03'
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
  change: Round 2 requirement decisions applied (KWR-DDR-003); 22 in propellers on 5215-class motors, booms 490 mm out and 1,142 mm long, 5.0 Ah cells; options for the endurance still not met
- version: "0.4"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Core power leads (8 AWG, four AS150 halves, 0.124 kg) added to the harness after Kitewright Core decision 17 B; all figures re-run"
---

# Kitewright Range sizing calculations

On paper, Kitewright Range takes off and lands vertically at 5,000 m with a 51.7 % thrust margin and flies 32.9 min and 44.4 km on the wing with a 1 kg payload and a 20 % reserve, at a take-off mass of 11.1 kg. This issue carries the round 2 requirement decisions Amish made on 2026-10-03 (KWR-DDR-003): 22 in propellers on 5215-class lift motors (O1-B), two ColdCell 6S3P packs of 5.0 Ah high-rate 21700 cells (O2-A), the combined range effect of both (O3, option B because O1-B was chosen) and the foam, glass and lite-ply airframe kept (O4-A). It also carries the Kitewright Core's four 8 AWG power leads with AS150 plugs, which Core decision 17 B moved into each frame's harness. Eight requirements are now met on paper or by design, including hover thrust margin (R1) and survey range (R3); endurance (R2) and take-off mass (R7) are still not met. The estimated cost is USD 4,285 against the USD 5,000 value-engineering target (USD 715 under). Options for the endurance still not met are worked out in section H.

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
| Lift thrust per motor at sea level | 68.7 N (7.0 kgf) | Maker-class figure for a 5215-class motor with a 22 in propeller on 6S (KWR-DDR-003); estimate, to be measured |
| Lift motor envelope and mass | 62 mm diameter, 35 mm high, about 285 g; 22 in propeller about 55 g | Estimates for the 5215 class; confirm when bought |
| Thrust at altitude | Sea-level thrust x density ratio (0.601) | Conservative: ignores the higher rpm a lighter load gives |
| Hover figure of merit, drive efficiency | 0.65, 0.82 | Typical for large carbon propellers and open ESCs |
| Cruise propeller and drive efficiency | 0.65 and 0.85 (0.55 combined) | 14 x 10 in folding propeller at 22 m/s |
| ColdCell packs | Two packs, 6S3P Li-ion high-rate 21700 cells of 5.0 Ah, 324 Wh and 1.40 kg each | Cross-repo assumption (ColdCell format, 5.0 Ah variant, KWR-DDR-003) |
| Usable energy | 90 % depth of discharge x 95 % for cold, packs warmed before take-off | ColdCell heater keeps the cells above 15 °C |
| Reserve | 20 % of usable energy kept for landing | R2 |
| Core power leads in the harness | 0.124 kg at the centre of gravity | Kitewright Core decision 17 B; as on Kitewright Lift |
| Systems power | 38 W: avionics 15, payload 10, pack heaters in flight 10, servos 3 | Estimate |
| Vertical phases | 125 s at hover power plus 20 % for transitions | Take-off, two transitions, landing |
| Climb | 400 m at 2.5 m/s on the wing | Launch site to survey height |
| Limit load factor | 2.5 g | Gusts and turns in valley wind |
| Carbon tube allowable bending stress | 600 MPa | Pultruded and roll-wrapped tube |
| Printed parts | ASA, 1,070 kg/m3, walls and infill per part | `sizing.py` |

## A. Mass and balance (R4, R7)

Take-off mass is 11.09 kg, of which the payload is 1.00 kg and the two ColdCell packs 2.80 kg. The Core power leads in the harness add 0.124 kg (Core decision 17 B). The round 2 decisions add 0.39 kg: the four 5215-class lift motors weigh 1.14 kg (0.82 kg before), the four 22 in propellers 0.22 kg and the booms, 50 mm longer, 0.27 kg for the pair. The 5.0 Ah cells do not change the pack mass. The largest made parts are the fuselage box (0.82 kg), the two wing panels with spars and ailerons (0.57 kg each) and the two boom pylons (0.14 kg each). The Kitewright Core with its GNSS mast weighs 0.78 kg.

The centre of gravity is 415 mm behind the firewall, at 28.4 % of the 281 mm mean chord, 1 mm behind the target. The payload mount, both packs and the lift motor pairs are centred on the target, so fitting or removing the 1 kg payload does not move the centre of gravity (R4).

## B. Aerodynamics and cruise (R2, R3, R6)

Table 2. Drag areas at cruise

| Item | CdA (m2) |
| --- | --- |
| Lift motors, mounts and ESCs (stopped) | 0.0127 |
| Wing | 0.0108 |
| Fuselage and nose | 0.0074 |
| Payload | 0.0036 |
| Leg fairings and feet | 0.0034 |
| Pylons | 0.0024 |
| Tail surfaces | 0.0023 |
| Booms, stopped propellers, mast, pitot and tail boom | 0.0057 |
| Total with 15 % interference | 0.0556 |

The zero-lift drag coefficient is 0.079, high for a clean aircraft but typical of a quadplane carrying its lift system and a payload outside; the larger lift motors add about 0.0009 m2. Wing loading is 155 N/m2 and the stall speed at 5,000 m is 18.0 m/s. The lowest-power speed above 1.25 times stall is 22.5 m/s at a lift coefficient of 0.83 and a lift-to-drag ratio of 7.4. The air needs 329 W, which is 634 W from the packs with the propeller, drive and 38 W of systems.

Wind (R6): cruise at 22.5 m/s is well above a 14 m/s gust. In hover the aircraft weathervanes nose into the wind; a 14 m/s side gust on about 0.23 m2 of side area gives about 17 N, which needs a tilt of about 9 degrees, well inside the authority left by the hover margin.

## C. Hover at 5,000 m (R1)

The four 22 in rotors sweep 0.981 m2, a disc loading of 111 N/m2. Ideal hover power at 0.736 kg/m3 is 945 W and the packs supply 1,772 W (82 A at 21.6 V, 13.7 A per cell, inside the rating of high-rate 5.0 Ah cells). Maximum thrust at altitude is 4 x 68.7 N x 0.601 = 165.1 N against a weight of 108.8 N: a **51.7 % thrust margin**. At sea level the same rotors hover at 40 % of maximum thrust, so one propeller set still serves every altitude band. The margin rests on a maker-class thrust figure (an estimate); AltiRig measures it before any flight.

## D. Energy, endurance and range (R2, R3)

Table 3. Energy per flight at 5,000 m

| Stage | Wh |
| --- | --- |
| Two packs, nominal | 648 |
| Usable with packs warmed | 554 |
| Kept as 20 % reserve | 111 |
| Hover, transitions | 74 |
| Climb 400 m | 22 |
| Left for cruise | 348 |

At 634 W the cruise energy gives **32.9 min** on the wing and **44.4 km** of survey track at 22.5 m/s.

## E. Structure

Table 4. Bending checks at limit load

| Item | Load case | Moment | Safety factor on 600 MPa |
| --- | --- | --- | --- |
| Wing spar 22 x 20 at the root | 2.5 g, lift centroid at 45 % of the panel | 72.2 N m | 2.8 |
| Joiner 20 x 16 inside the spars | Same | 72.2 N m | 3.9 |
| Lift boom 25 x 23 at the pylon edge | One motor at sea-level full thrust | 31.0 N m | 8.4 |
| Tail boom 20 x 17 | Stabiliser load of 15 % of weight at 2.5 g | | 5.7 |
| Pylon bolts, two M5 per pylon | Both motors at full thrust plus one motor alone | 434 N | 9.9 on 4.3 kN proof |

All margins are above 2. The wing spar is the tightest (2.75, down from 2.9 with the heavier aircraft) and is checked again with a proof load at TRL 4.

## F. Geometry rules (R8, R9)

The booms sit 490 mm either side of the centre line and the lift motors 531 mm ahead of and behind the centre of gravity. The rotor discs sit 78 mm below the wing-top plane (the rule is at least 70 mm), the front discs clear the leading edge by 171 mm and the rear discs the trailing edge by 44 mm, the lift discs clear the cruise propeller disc by 33 mm and the rear discs clear the stabiliser by 110 mm. Motors are fixed and do not tilt, there is one wing, and the aircraft is not a tail-sitter. The longest part is a wing panel at 1,205 mm with its root fittings, then the lift boom at 1,142 mm; all fit 1.3 m cases. Tail volume coefficients are 0.53 (horizontal) and 0.025 (vertical).

## G. Cost (R10)

Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 4,285 (USD 715 under the target), including one Kitewright Core avionics set (USD 900, assumed), two ColdCell packs of 5.0 Ah cells (USD 700) and two transport cases (USD 360), excluding the payload. The round 2 decisions add USD 280: the lift motors USD 112, the propellers USD 40, the longer boom tubes USD 8 and the 5.0 Ah cells USD 120 (all estimates). The Core power leads add USD 60 to the harness line, priced as on Kitewright Lift.

## H. Options for the requirement still not met (R2)

Table 5. Options worked out with the same script, on the design as decided (changes from it)

| Option | Take-off mass | Hover margin | Endurance | Range | Cost change |
| --- | --- | --- | --- | --- | --- |
| A: design as decided | 11.09 kg | 51.7 % | 32.9 min | 44.4 km | USD 0 |
| B: two 6S4P packs of 5.0 Ah cells | 11.97 kg | 40.6 % | 41.2 min | 57.7 km | +USD 233 |
| C: moulded carbon wing, tail and fuselage | 10.41 kg | 61.7 % | 36.8 min | 48.1 km | +USD 1,200 |
| D: moulded airframe and two 6S4P packs of 5.0 Ah cells | 11.29 kg | 49.1 % | 45.6 min | 61.9 km | +USD 1,433 |

With the larger propellers, heavier packs no longer break R1: option B keeps a 40.6 % margin. Only option D reaches the 45 min of R2 on paper, by 0.6 min, at USD 5,718 in all (USD 718 over the value-engineering target). The 6S4P pack is a larger ColdCell format whose fit in the battery bays is not yet checked. The pre-decision options (KWR-CAL-001 v0.2, Table 5) are kept in that issue's PDF.

## L. Results against every requirement

Table 6. Results

| ID | Result | Status |
| --- | --- | --- |
| R1 | 51.7 % thrust margin at 0.736 kg/m3 and 11.09 kg, on maker-class thrust | Met on paper; thrust to be measured in AltiRig |
| R2 | 32.9 min on the wing at 5,000 m with 1 kg and 20 % reserve | **Not met** |
| R3 | 44.4 km of survey track | Met on paper (11 % margin) |
| R4 | 1 kg on the Core mount centred on the CG; CG 28.4 % of the mean chord with or without it | Met by design |
| R5 | All electronics and servos specified to -20 °C or tested cold; packs heated | Met on paper; to confirm when parts are bought |
| R6 | 22.5 m/s cruise against 14 m/s gusts; about 9 degrees of tilt to hold a side gust in hover | Met on paper |
| R7 | 11.09 kg take-off mass | **Not met** (airframe kept by decision, KWR-DDR-003 O4-A) |
| R8 | Longest part 1,205 mm; lift boom 1,142 mm; two cases about 9 kg and 12.5 kg | Met by design |
| R9 | Fixed motors, one wing, discs 78 mm below the wing-top plane | Met by design |
| R10 | USD 4,285; every part bought or made with hobby tools | Met on paper; USD 715 under the value-engineering target |

## Checks against the earlier figures

The precis estimated a take-off mass near 8 kg and the problem statement assumed hover time near 47 % of sea level at 5,000 m. The constructable design is 3.1 kg heavier than that estimate: the ColdCell packs alone are 2.8 kg for 648 Wh, and the 22 in lift system with its mounts is about 1.7 kg. Against KWR-CAL-001 v0.2 the round 2 decisions move the hover margin from 31.8 % to 53.4 %, endurance from 31.0 to 33.6 min and range from 40.9 to 45.0 km, matching the 45.0 km of option O3-B; the endurance gain from the 5.0 Ah cells (to 35.6 min alone) is partly spent on the heavier lift system (33.6 min together). The Core power leads then take the hover margin to 51.7 %, endurance to 32.9 min and range to 44.4 km.
