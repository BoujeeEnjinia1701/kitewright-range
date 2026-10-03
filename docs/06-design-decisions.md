---
doc_id: KWR-DEC-001
title: Kitewright Range design decisions register
project: Kitewright Range
doc_type: Design decisions register
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Register opened at TRL 3; decisions made under the 2026-10-03 pre-approval; four requirement decisions proposed, awaiting Amish
---

# Kitewright Range design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/`, and the open ones in `docs/REVIEW.md` (TRL 3, Decisions for Amish); this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list open decisions.

## Open decisions

All four are about requirements the design does not meet or meets too thinly. They are **Proposed, awaiting Amish**; the design and build plan stay as they are until he decides. Figures are from KWR-CAL-001 v0.2, Table 5.

| # | Decision needed | Options | Recommendation | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| O1 | R1 hover thrust margin: 31.8 % on unmeasured maker-class thrust | A: keep 20 in propellers on 5212-class motors (31.8 %, no cost or mass change). B: 22 in propellers on 5215-class motors (53.3 %, +USD 160, +0.40 kg, endurance -1.7 min; booms 50 mm longer and 20 mm further out). C: keep A and change only if AltiRig measures under the target | **B**, the conservative choice: hover authority at 5,000 m is a safety margin | Lift motors, propellers, booms, pylon position | KWR-CAL-001 C, H |
| O2 | R2 endurance: 31.0 min | A: two 6S3P packs of 5.0 Ah cells (35.6 min, +USD 120, no mass change). B: two 6S4P packs (38.9 min, +USD 190, +0.88 kg; hover margin falls to 21.7 %). C: moulded carbon airframe with two 6S4P packs (43.3 min, +USD 1,390, +0.19 kg; margin 29.4 %) | **A** for the first prototype; C as the second-prototype path | ColdCell cell choice only | KWR-CAL-001 D, H |
| O3 | R3 survey range: 40.9 km | A: 5.0 Ah cells as O2-A (46.8 km, +USD 120). B: with O1-B as well (45.0 km, +USD 280, +0.40 kg). C: keep as is (40.9 km) | **A**, taken together with O2-A (and B if O1-B is chosen) | ColdCell cell choice only | KWR-CAL-001 D, H |
| O4 | R7 take-off mass: 10.58 kg | A: keep the foam, glass and lite-ply airframe (10.58 kg). B: moulded carbon wing, tail and fuselage (9.89 kg, +USD 1,200, endurance +4.1 min; USD 5,145 in all, USD 145 over the value-engineering target). C: fly one pack (9.18 kg; endurance 15.0 min) | **A** for the first prototype, weighed at TRL 4; no option inside the concept reaches the target without losing R2 | None for A | KWR-CAL-001 A, H |

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Lift motor and propeller thrust at 0.736 kg/m3, measured in AltiRig | R1 rests on maker-class figures scaled by density | KWR-CAL-001 C |
| 2 | Cold ratings of the ESCs, servos, cruise motor ESC and pitot heater to -20 °C, or a cold soak test | R5 is met only by specification | KWR-REQ-001 |
| 3 | The joiner slides into both spar bores without play | The wing joint depends on it | KWR-DDR-002, C6 |
| 4 | The cruise motor's bolt circle and shaft length | They set the nose cone inserts and the propeller position | KWR-DDR-002, C5 |
| 5 | Kitewright Core avionics envelope (180 x 110 x 60 mm) and mass (0.78 kg with the mast) | They set the front bay and the balance | Cross-repo assumption |
| 6 | ColdCell pack size (138 x 75 x 82 mm), mass (1.40 kg) and XT90 lead | They set the battery bays and the balance | Cross-repo assumption |
| 7 | Payload mount plate (160 x 80 x 12 mm) and its four M4 holes | They set the floor inserts | Cross-repo assumption |
| 8 | Transport cases with at least 1,250 mm inside | The wing panel is 1,205 mm with its root fittings | KWR-CAL-001 F |

## Value engineering

Value-engineering target: USD 5,000 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 3,945 (USD 1,055 under the target). Main cost drivers and savings worth trying:

- The largest lines are the Kitewright Core avionics share (USD 900, assumed), the two ColdCell packs (USD 580), the four lift motors (USD 480), the two transport cases (USD 360) and the four lift ESCs (USD 180).
- Savings worth trying: soft padded bags in place of hard cases for vehicle transport (about USD 200); four-in-one ESC boards are lighter but would move power wiring into the fuselage, so they are not recommended.
- The open decisions add at most USD 1,390 (O2-C); the recommended set (O1-B with O2-A) adds USD 280 and keeps the design under the target.

## Decisions made

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | TRL 2 review decisions D1 to D10: PX4; 2.5 m two-piece wing; one 20 in propeller set; winch on Lift; nose tractor and tail boom; two ColdCell 6S3P packs; foam, ply and printed build; Sikkim State Disaster Management Authority as first co-design candidate (not agreed); staged powered tests; conservative failsafes | Amish: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and "Proceed with the remaining 15 scaffolds" | KWR-DDR-001 |
| 2026-10-03 | Design for construction C1 to C13: tail boom, pylons, boom spacing, motors on the centre of gravity, nose tractor, joiner and wing bolts, fuselage bays, landing legs, wing conduits, payload mount, tail joint, hatch, pitot | Amish, same pre-approval | KWR-DDR-002 |
