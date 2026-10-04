---
doc_id: KWR-DEC-001
title: Kitewright Range design decisions register
project: Kitewright Range
doc_type: Design decisions register
version: "0.3"
status: Draft
date: '2026-10-04'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Register opened at TRL 3; decisions made under the 2026-10-03 pre-approval; four requirement decisions proposed, awaiting Amish
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: 'O1 to O4 decided by Amish on 2026-10-03 ("i agree with all the 46 recommendations you provided. please proceed."; 36B, 37A, 38A) and moved to Decisions made (KWR-DDR-003); Core power leads taken on under Core decision 33B'
- version: "0.3"
  date: '2026-10-04'
  author: Amish Chadha
  change: 'Round-3 decision 10A (Amish, 2026-10-04: "For round 3, I agree with all your proposed recommendations") recorded in Decisions made (KWR-DDR-004)'
---

# Kitewright Range design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/`, and the open ones in `docs/REVIEW.md` (TRL 3, Decisions for Amish); this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list open decisions.

## Open decisions

None. Amish decided O1 to O4 on 2026-10-03 (KWR-DDR-003) and the Kitewright family reconciliation on 2026-10-04 (KWR-DDR-004); the design and build plan carry those decisions. R2 (30.6 min) and R7 (11.35 kg) remain not met, as accepted for the first prototype. Nothing in carrying out 10A needs Amish.

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | 5215-class lift motor thrust with a 22 x 7 in propeller at 0.736 kg/m3, measured in AltiRig | R1 rests on maker-class figures scaled by density; the 52.0 % margin allows about 14 % less thrust | KWR-CAL-001 C, KWR-DDR-003 |
| 2 | Cold ratings of the ESCs, servos, cruise motor ESC and pitot heater to -20 °C, or a cold soak test | R5 is met only by specification | KWR-REQ-001 |
| 3 | The joiner slides into both spar bores without play | The wing joint depends on it | KWR-DDR-002, C6 |
| 4 | The cruise motor's bolt circle and shaft length | They set the nose cone inserts and the propeller position | KWR-DDR-002, C5 |
| 5 | Kitewright Core avionics envelope (180 x 110 x 60 mm) and mass (0.78 kg with the mast); Core's own figure after its decision 33B is about 0.99 kg including the payload mount (Range carries 0.90 kg for the same items) | They set the front bay and the balance | Cross-repo assumption; `docs/REVIEW.md` cross-repo actions |
| 6 | ColdCell pack size (138 x 75 x 82 mm), mass (1.40 kg) with 5.0 Ah high-rate 21700 cells, and its lead (XT90 here, AS150 in the Core) | They set the battery bays, the energy and the balance | Cross-repo assumption, KWR-DDR-003 |
| 9 | Kitewright Core pad positions and grommets for the four 8 AWG power leads Range now supplies | Lead lengths and the solder joints at integration | Core decision 33B, KWR-DDR-003 |
| 7 | Payload mount plate (160 x 80 x 12 mm) and its four M4 holes | They set the floor inserts | Cross-repo assumption |
| 8 | Transport cases with at least 1,250 mm inside | The wing panel is 1,205 mm with its root fittings | KWR-CAL-001 F |

## Value engineering

Value-engineering target: USD 5,000 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 4,293 (USD 707 under the target). Main cost drivers and savings worth trying:

- The largest lines are the Kitewright Core avionics share (USD 900, assumed), the two ColdCell packs of 5.0 Ah cells (USD 700), the four 5215-class lift motors (USD 600), the two transport cases (USD 360) and the four lift ESCs (USD 180).
- The 2026-10-03 decisions added USD 348: motors USD 120, propellers USD 40, cells USD 120, boom tubes USD 8 and the Core power leads USD 60 (moved from the Core's bill).
- Savings worth trying: soft padded bags in place of hard cases for vehicle transport (about USD 200); four-in-one ESC boards are lighter but would move power wiring into the fuselage, so they are not recommended.

## Decisions made

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | TRL 2 review decisions D1 to D10: PX4; 2.5 m two-piece wing; one 20 in propeller set; winch on Lift; nose tractor and tail boom; two ColdCell 6S3P packs; foam, ply and printed build; Sikkim State Disaster Management Authority as first co-design candidate (not agreed); staged powered tests; conservative failsafes | Amish: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and "Proceed with the remaining 15 scaffolds" | KWR-DDR-001 |
| 2026-10-03 | Design for construction C1 to C13: tail boom, pylons, boom spacing, motors on the centre of gravity, nose tractor, joiner and wing bolts, fuselage bays, landing legs, wing conduits, payload mount, tail joint, hatch, pitot | Amish, same pre-approval | KWR-DDR-002 |
| 2026-10-03 | O1 (36B), R1: 22 in propellers on 5215-class motors, booms 50 mm longer and 20 mm further out; hover margin 52.0 % | Amish: "i agree with all the 46 recommendations you provided. please proceed." | KWR-DDR-003 |
| 2026-10-03 | O2 and O3 (37A), R2 and R3: 5.0 Ah cells in the same two 6S3P packs; 32.9 min and 44.3 km with O1-B | Amish, same words | KWR-DDR-003 |
| 2026-10-03 | O4 (38A), R7: keep the foam, glass and lite-ply airframe and weigh it at TRL 4; 11.07 kg | Amish, same words | KWR-DDR-003 |
| 2026-10-03 | Range supplies the four Kitewright Core power leads with AS150 plugs (Core decision 33B) | Amish, same words (Core decision 33B) | KWR-DDR-003 |
| 2026-10-04 | Round-3 decision 10A: AS150 plugs on the packs (XT90 before); the Kitewright Core to the one family mounting envelope, the Core's drawing the reference: hung under the floor at the centre of gravity on four M4 (220 x 130 mm) in a 6 mm birch doubler, lid up through a 200 x 112 mm opening, fuselage 156 mm wide (150 inside), packs moved to the nose bay and behind the lid, rear bulkhead at 645 mm, GNSS and antennas on the hatch; Range recomputed with the 0.99 kg Core (30.6 min, 41.5 km, 48.3 %); the Kitewright interface table in `docs/REVIEW.md` | Amish: "For round 3, I agree with all your proposed recommendations" | KWR-DDR-004 |
