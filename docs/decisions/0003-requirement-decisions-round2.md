---
doc_id: KWR-DDR-003
title: Kitewright Range requirement decisions, round 2
project: Kitewright Range
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Decisions O1 to O4 on the requirements not met or at risk, decided by Amish on 2026-10-03 and carried into the model, calculations, BOM and build plan
---

# 0003: Requirement decisions, round 2

- **Date:** 2026-10-03
- **Status:** Decided. Decided by Amish Chadha, 2026-10-03: "i approve all of the 47 recommendations provided by you. Execute them." Each decision below is the recommendation as worded in `docs/06-design-decisions.md` (KWR-DEC-001 v0.1), including its conditions.

## Context

KWR-CAL-001 v0.2 left four requirements not met or at risk on the constructable design: hover thrust margin (R1, 31.8 % on unmeasured maker-class thrust), endurance (R2, 31.0 min), survey range (R3, 40.9 km, a 2 % margin) and take-off mass (R7, 10.58 kg). They were set out as O1 to O4, Proposed, awaiting Amish, with options and a recommendation each. O3 was linked to the others: its recommendation was A, decided together with O2, and B if O1-B was chosen.

## Decision

Table 1. Decisions

| # | Requirement | Option chosen | Effect on the design (KWR-CAL-001 v0.3) | Condition |
| --- | --- | --- | --- | --- |
| O1 | R1, hover thrust margin | **B:** 22 in propellers on 5215-class motors | Booms 20 mm further out (490 mm from the centre line) and 50 mm longer (1,142 mm); motors 531 mm ahead of and behind the centre of gravity; margin 31.8 % to 53.4 %; +0.39 kg; +USD 160 (motors, propellers, longer boom tubes) | Thrust is a maker-class estimate (7.0 kgf at sea level) until AltiRig measures it at 0.736 kg/m3 (TRL 4) |
| O2 | R2, endurance | **A:** two 6S3P packs of 5.0 Ah high-rate 21700 cells | Pack energy 583 Wh to 648 Wh, pack mass unchanged; +USD 120. With O1-B the endurance is 33.6 min (35.6 min with O2-A alone) | R2 is still not met; C (moulded carbon airframe with 6S4P packs) was named as the path for a second prototype once the first one's drag and mass are measured |
| O3 | R3, survey range | **B**, the combined effect: the recommendation was A, decided together with O2, becoming B because O1-B is chosen | 45.0 km (the option stated about 45.0 km); +USD 280 and +0.40 kg combined with O1-B and O2-A (calculated: +USD 280, +0.39 kg). No change of its own: it is the result of O1-B with O2-A | None beyond those of O1 and O2 |
| O4 | R7, take-off mass | **A:** keep the foam, glass and lite-ply airframe | No change to the airframe. Take-off mass is now 10.97 kg (10.58 kg before O1-B) | The first prototype is weighed at TRL 4; R7 stays not met. If the 8 kg target reflects a regulatory class at the first site, that site's rules set the target before the second prototype |

## Consequences

- Requirement status (KWR-REQ-001 v0.4): R1 at risk to met on paper; R2 not met (31.0 to 33.6 min); R3 at risk to met on paper (45.0 km, a 12 % margin); R7 not met (10.58 to 10.97 kg), kept by decision. No requirement was restated.
- Estimated cost: USD 3,945 to USD 4,225 against the USD 5,000 value-engineering target (USD 775 under). `budget_usd` in `project.yaml` is the value-engineering target and stays at USD 5,000.
- The wing spar's safety factor falls from 2.9 to 2.8 at 2.5 g with the heavier aircraft; the lift boom's from 10.8 to 8.4 and the pylon bolts' from 12.5 to 9.9 with the larger thrust. All stay above 2.
- Geometry: rotor discs 78 mm below the wing-top plane (rule 70 mm), lift discs 33 mm clear of the cruise propeller disc, rear discs 110 mm ahead of the stabiliser. The model's constructability checks pass (72 solids in 48 parts).
- Regenerated from the changed model: STEP and STL, general arrangement KWR-DWG-001 Rev P3, making sketches KWR-DWG-105, 106, 108 and 109 at Rev P2, the build plan pictures, the concept media with blueprint KWR-DWG-010 Rev P3, and `media/model.glb`.
- The remaining endurance shortfall (R2) is a new open decision, O5, in `docs/06-design-decisions.md`.
- Cross-repo: ColdCell needs the 5.0 Ah cell variant of its 6S3P pack; AltiRig's first job is now the 5215-class motor with a 22 in propeller.
- Following Kitewright Core decision 17 B (not a decision of this record), the Core's four 8 AWG power leads with AS150 plugs (two pack inputs, two frame outputs) are now part of Range's harness, BOM line 29: +USD 60 and +0.124 kg, priced as on Kitewright Lift. With them the take-off mass is 11.09 kg (R7 not met), hover margin 51.7 %, endurance 32.9 min, range 44.4 km and the estimated cost USD 4,285 (KWR-CAL-001 v0.4).
