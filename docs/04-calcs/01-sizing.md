---
doc_id: KWR-CAL-001
title: Kitewright Range sizing calculations
project: Kitewright Range
doc_type: Calculation
version: "0.2"
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
---

# Kitewright Range sizing calculations

On paper, Kitewright Range takes off and lands vertically at 5,000 m with a 31.8 % thrust margin and flies 31 min and 40.9 km on the wing with a 1 kg payload and a 20 % reserve, at a take-off mass of 10.6 kg. Seven requirements are met on paper or by design; endurance (R2) and take-off mass (R7) are not met, and hover thrust margin (R1) and survey range (R3) are met with margins too thin to rely on before the motors and propellers are measured. The estimated cost is USD 3,945 against the USD 5,000 value-engineering target (USD 1,055 under). Options for each requirement not met or at risk are worked out in section H and set out as decisions for Amish in `docs/REVIEW.md`.

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
| Lift thrust per motor at sea level | 56.9 N (5.8 kgf) | Maker class figure for a 5212-class 340 KV motor with a 20 x 6.5 in propeller on 6S; to be measured |
| Thrust at altitude | Sea-level thrust x density ratio (0.601) | Conservative: ignores the higher rpm a lighter load gives |
| Hover figure of merit, drive efficiency | 0.65, 0.82 | Typical for 20 in carbon propellers and open ESCs |
| Cruise propeller and drive efficiency | 0.65 and 0.85 (0.55 combined) | 14 x 10 in folding propeller at 22 m/s |
| ColdCell packs | Two packs, 6S3P Li-ion 21700 cells of 4.5 Ah, 291.6 Wh and 1.40 kg each | Cross-repo assumption (ColdCell format) |
| Usable energy | 90 % depth of discharge x 95 % for cold, packs warmed before take-off | ColdCell heater keeps the cells above 15 °C |
| Reserve | 20 % of usable energy kept for landing | R2 |
| Systems power | 38 W: avionics 15, payload 10, pack heaters in flight 10, servos 3 | Estimate |
| Vertical phases | 125 s at hover power plus 20 % for transitions | Take-off, two transitions, landing |
| Climb | 400 m at 2.5 m/s on the wing | Launch site to survey height |
| Limit load factor | 2.5 g | Gusts and turns in valley wind |
| Carbon tube allowable bending stress | 600 MPa | Pultruded and roll-wrapped tube |
| Printed parts | ASA, 1,070 kg/m3, walls and infill per part | `sizing.py` |

## A. Mass and balance (R4, R7)

Take-off mass is 10.58 kg, of which the payload is 1.00 kg and the two ColdCell packs 2.80 kg. The largest made parts are the fuselage box (0.82 kg), the two wing panels with spars and ailerons (0.57 kg each) and the two boom pylons (0.14 kg each). The four lift motors weigh 0.82 kg and the Kitewright Core with its GNSS mast 0.78 kg.

The centre of gravity is 415 mm behind the firewall, at 28.4 % of the 281 mm mean chord, 1 mm behind the target. The payload mount, both packs and the lift motor pairs are centred on the target, so fitting or removing the 1 kg payload does not move the centre of gravity (R4).

## B. Aerodynamics and cruise (R2, R3, R6)

Table 2. Drag areas at cruise

| Item | CdA (m2) |
| --- | --- |
| Lift motors, mounts and ESCs (stopped) | 0.0118 |
| Wing | 0.0108 |
| Fuselage and nose | 0.0074 |
| Payload | 0.0036 |
| Leg fairings and feet | 0.0034 |
| Pylons | 0.0024 |
| Tail surfaces | 0.0023 |
| Booms, stopped propellers, mast, pitot and tail boom | 0.0056 |
| Total with 15 % interference | 0.0544 |

The zero-lift drag coefficient is 0.077, high for a clean aircraft but typical of a quadplane carrying its lift system and a payload outside. Wing loading is 147 N/m2 and the stall speed at 5,000 m is 17.6 m/s. The lowest-power speed above 1.25 times stall is 21.9 m/s at a lift coefficient of 0.83 and a lift-to-drag ratio of 7.5. The air needs 302 W, which is 585 W from the packs with the propeller, drive and 38 W of systems.

Wind (R6): cruise at 21.9 m/s is well above a 14 m/s gust. In hover the aircraft weathervanes nose into the wind; a 14 m/s side gust on about 0.23 m2 of side area gives about 17 N, which needs a tilt of about 9 degrees, inside the authority left by the hover margin.

## C. Hover at 5,000 m (R1)

The four 20 in rotors sweep 0.811 m2, a disc loading of 128 N/m2. Ideal hover power at 0.736 kg/m3 is 968 W and the packs supply 1,815 W (84 A at 21.6 V, 14 A per cell, inside the cells' rating). Maximum thrust at altitude is 4 x 56.9 N x 0.601 = 136.7 N against a weight of 103.8 N: a **31.8 % thrust margin**. At sea level the same rotors hover at 46 % of maximum thrust, so one propeller set serves every altitude band.

## D. Energy, endurance and range (R2, R3)

Table 3. Energy per flight at 5,000 m

| Stage | Wh |
| --- | --- |
| Two packs, nominal | 583 |
| Usable with packs warmed | 499 |
| Kept as 20 % reserve | 100 |
| Hover, transitions | 76 |
| Climb 400 m | 21 |
| Left for cruise | 302 |

At 585 W the cruise energy gives **31.0 min** on the wing and **40.9 km** of survey track at 21.9 m/s.

## E. Structure

Table 4. Bending checks at limit load

| Item | Load case | Moment | Safety factor on 600 MPa |
| --- | --- | --- | --- |
| Wing spar 22 x 20 at the root | 2.5 g, lift centroid at 45 % of the panel | 68.9 N m | 2.9 |
| Joiner 20 x 16 inside the spars | Same | 68.9 N m | 4.0 |
| Lift boom 25 x 23 at the pylon edge | One motor at sea-level full thrust | 24.2 N m | 10.8 |
| Tail boom 20 x 17 | Stabiliser load of 15 % of weight at 2.5 g | | 6.0 |
| Pylon bolts, two M5 per pylon | Both motors at full thrust plus one motor alone | 345 N | 12.5 on 4.3 kN proof |

All margins are above 2. The wing spar is the tightest and is checked again with a proof load at TRL 4.

## F. Geometry rules (R8, R9)

The rotor discs sit 81 mm below the wing-top plane (the rule is at least 70 mm), the front discs clear the leading edge by 171 mm and the rear discs the trailing edge by 44 mm, and the lift discs clear the cruise propeller disc by 38 mm. Motors are fixed and do not tilt, there is one wing, and the aircraft is not a tail-sitter. The longest part is a wing panel at 1,205 mm with its root fittings, then the lift boom at 1,092 mm; all fit 1.3 m cases. Tail volume coefficients are 0.53 (horizontal) and 0.025 (vertical).

## G. Cost (R10)

Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 3,945 (USD 1,055 under the target), including one Kitewright Core avionics set (USD 900, assumed), two ColdCell packs (USD 580) and two transport cases (USD 360), excluding the payload.

## H. Options for the requirements not met or at risk

Table 5. Options worked out with the same script (changes from the design as it stands)

| Option | Take-off mass | Hover margin | Endurance | Range | Cost change |
| --- | --- | --- | --- | --- | --- |
| Design as it stands | 10.58 kg | 31.8 % | 31.0 min | 40.9 km | USD 0 |
| Two 6S3P packs of 5.0 Ah cells | 10.58 kg | 31.8 % | 35.6 min | 46.8 km | +USD 120 |
| Two 6S4P packs | 11.46 kg | 21.7 % | 38.9 min | 53.3 km | +USD 190 |
| One 6S3P pack | 9.18 kg | 51.9 % | 15.0 min | 18.4 km | -USD 290 |
| Moulded carbon wing, tail and fuselage | 9.89 kg | 40.9 % | 35.1 min | 44.6 km | +USD 1,200 |
| Moulded airframe and two 6S4P packs | 10.77 kg | 29.4 % | 43.3 min | 57.5 km | +USD 1,390 |
| 22 in propellers on 5215-class motors | 10.98 kg | 53.3 % | 29.3 min | 39.2 km | +USD 160 |
| 22 in propellers and 5.0 Ah cells | 10.98 kg | 53.3 % | 33.5 min | 45.0 km | +USD 280 |

## L. Results against every requirement

Table 6. Results

| ID | Result | Status |
| --- | --- | --- |
| R1 | 31.8 % thrust margin at 0.736 kg/m3 and 10.58 kg, on maker-class thrust | **At risk:** 1.8 points above the line, on unmeasured thrust |
| R2 | 31.0 min on the wing at 5,000 m with 1 kg and 20 % reserve | **Not met** |
| R3 | 40.9 km of survey track | **At risk:** 2 % above the line |
| R4 | 1 kg on the Core mount centred on the CG; CG 28.4 % of the mean chord with or without it | Met by design |
| R5 | All electronics and servos specified to -20 °C or tested cold; packs heated | Met on paper; to confirm when parts are bought |
| R6 | 21.9 m/s cruise against 14 m/s gusts; about 9 degrees of tilt to hold a side gust in hover | Met on paper |
| R7 | 10.58 kg take-off mass | **Not met** |
| R8 | Longest part 1,205 mm; two cases about 9 kg and 12 kg | Met by design |
| R9 | Fixed motors, one wing, discs 81 mm below the wing-top plane | Met by design |
| R10 | USD 3,945; every part bought or made with hobby tools | Met on paper; USD 1,055 under the value-engineering target |

## Checks against the TRL 2 figures

The precis estimated a take-off mass near 8 kg and the problem statement assumed hover time near 47 % of sea level at 5,000 m. The constructable design is 2.6 kg heavier than that estimate: the ColdCell packs alone are 2.8 kg for 583 Wh, and the 20 in lift system with its mounts is 1.3 kg. That is why R2 and R7 are missed together: more energy costs mass, and less mass costs energy.
