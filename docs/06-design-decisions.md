---
doc_id: KWR-DEC-001
title: Kitewright Range design decisions register
project: Kitewright Range
doc_type: Design decisions register
version: "0.3"
status: Draft
date: '2026-10-03'
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
  change: O1 to O4 decided by Amish on 2026-10-03 (KWR-DDR-003) and moved to decisions made; new open decision O5 on the endurance still not met; items to confirm and value engineering updated
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: "O5 figures and value engineering brought to KWR-CAL-001 v0.4, with the Core power leads in the harness (Kitewright Core decision 17 B)"
---

# Kitewright Range design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/`, and the open ones in `docs/REVIEW.md` (TRL 3, Decisions for Amish); this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list open decisions.

## Open decisions

O1 to O4 were decided by Amish on 2026-10-03 and are under Decisions made (KWR-DDR-003). One new decision is **Proposed, awaiting Amish**; the design and build plan stay as they are until he decides. Figures are from KWR-CAL-001 v0.4, Table 5.

| # | Decision needed | Options | Recommendation | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| O5 | R2 endurance: 32.9 min on the decided design (22 in propellers, 5.0 Ah cells, Core power leads in the harness), against 45 min | A: keep the decided design for the first prototype (32.9 min, no change) and measure drag, mass and pack energy at TRL 4. B: two 6S4P packs of 5.0 Ah cells (41.2 min, +USD 233, +0.88 kg, hover margin 40.6 %, R7 worse at 11.97 kg; a larger ColdCell format whose fit in the bays is unchecked). C: moulded carbon wing, tail and fuselage (36.8 min, +USD 1,200, -0.69 kg). D: moulded airframe and two 6S4P packs of 5.0 Ah cells (45.6 min, R2 met on paper by 0.6 min, +USD 1,433, USD 5,718 in all, USD 718 over the value-engineering target) | **A** for the first prototype; D is the path for a second prototype once the first one's drag and mass are measured, with B as the cheaper step if the measured drag is lower than estimated | None for A | KWR-CAL-001 v0.4 H; KWR-DDR-003 |

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Lift motor and propeller thrust at 0.736 kg/m3 for the 5215-class motor with a 22 in propeller, measured in AltiRig | R1 rests on a maker-class figure (7.0 kgf at sea level, an estimate) scaled by density | KWR-CAL-001 C; KWR-DDR-003 |
| 2 | Cold ratings of the ESCs, servos, cruise motor ESC and pitot heater to -20 °C, or a cold soak test | R5 is met only by specification | KWR-REQ-001 |
| 3 | The joiner slides into both spar bores without play | The wing joint depends on it | KWR-DDR-002, C6 |
| 4 | The cruise motor's bolt circle and shaft length | They set the nose cone inserts and the propeller position | KWR-DDR-002, C5 |
| 5 | Kitewright Core avionics envelope (180 x 110 x 60 mm) and mass (0.78 kg with the mast) | They set the front bay and the balance | Cross-repo assumption |
| 6 | ColdCell pack size (138 x 75 x 82 mm), mass (1.40 kg) and XT90 lead with 5.0 Ah high-rate cells, and the cells' continuous rating at least 14 A each when warmed | They set the battery bays, the balance and the hover current | Cross-repo assumption; KWR-DDR-003 |
| 7 | Payload mount plate (160 x 80 x 12 mm) and its four M4 holes | They set the floor inserts | Cross-repo assumption |
| 8 | Transport cases with at least 1,250 mm inside | The wing panel is 1,205 mm with its root fittings; the lift boom is 1,142 mm | KWR-CAL-001 F |
| 9 | The 5215-class motor's envelope (62 mm across, 35 mm high, estimate), mass (about 285 g) and bolt pattern on the tube clamp mount | They set the rotor disc height (78 mm below the wing-top plane against the 70 mm rule) and the mass | KWR-DDR-003 |

## Value engineering

Value-engineering target: USD 5,000 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 4,285 (USD 715 under the target), including the USD 280 of the round 2 decisions and USD 60 for the Core power leads now in the harness (Core decision 17 B). Main cost drivers and savings worth trying:

- The largest lines are the Kitewright Core avionics share (USD 900, assumed), the two ColdCell packs (USD 700), the four lift motors (USD 592), the two transport cases (USD 360) and the four lift ESCs (USD 180).
- Savings worth trying: soft padded bags in place of hard cases for vehicle transport (about USD 200); four-in-one ESC boards are lighter but would move power wiring into the fuselage, so they are not recommended.
- The round 2 decisions added USD 280 (O1-B with O2-A). The open decision O5 adds nothing for its recommendation A; its option D would take the estimate to USD 5,718, USD 718 over the target.

## Decisions made

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | TRL 2 review decisions D1 to D10: PX4; 2.5 m two-piece wing; one 20 in propeller set; winch on Lift; nose tractor and tail boom; two ColdCell 6S3P packs; foam, ply and printed build; Sikkim State Disaster Management Authority as first co-design candidate (not agreed); staged powered tests; conservative failsafes | Amish: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and "Proceed with the remaining 15 scaffolds" | KWR-DDR-001 |
| 2026-10-03 | Design for construction C1 to C13: tail boom, pylons, boom spacing, motors on the centre of gravity, nose tractor, joiner and wing bolts, fuselage bays, landing legs, wing conduits, payload mount, tail joint, hatch, pitot | Amish, same pre-approval | KWR-DDR-002 |
| 2026-10-03 | Round 2 requirement decisions: O1-B 22 in propellers on 5215-class motors (booms 490 mm out, 1,142 mm long); O2-A two 6S3P packs of 5.0 Ah high-rate 21700 cells; O3 taken as B, the combined effect of O1-B and O2-A (45.0 km, +USD 280, +0.40 kg); O4-A foam, glass and lite-ply airframe kept, weighed at TRL 4 | Amish: "i approve all of the 47 recommendations provided by you. Execute them." | KWR-DDR-003 |

## Change log

- 2026-10-03, v0.3: O5 figures and value engineering updated for the Core power leads in the harness (Kitewright Core decision 17 B).
- 2026-10-03, v0.2: O1 to O4 moved from Proposed, awaiting Amish to decided (KWR-DDR-003); O5 added as Proposed, awaiting Amish; items 1, 6, 8 and 9 to confirm and the value engineering figures updated.
