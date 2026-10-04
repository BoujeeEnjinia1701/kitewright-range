---
doc_id: KWR-DDR-003
title: Kitewright Range requirement decisions (R1, R2, R3, R7) and Core power leads
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
  change: Amish's requirement decisions 36B, 37A and 38A carried out, with the Kitewright Core power leads taken on under Core decision 33B
---

# 0003: Requirement decisions on hover margin, endurance, range and mass

- **Date:** 2026-10-03
- **Status:** accepted
- **Decided by:** Amish Chadha, 2026-10-03, accepting every recommendation put to him in the second round of requirement decisions: "i agree with all the 46 recommendations you provided. please proceed." For Kitewright Range: 36B (R1, register O1), 37A (R2 and R3, register O2 and O3) and 38A (R7, register O4). Kitewright Core decision 33B, decided in the same words, moves the Core's power leads to each frame.

> **Safety:** The 22 in lift propellers are larger and the motors stronger: fit them only at the propeller safety stop of the build plan, with the arming plug out and the lockable switch locked, and hold the 15 m keep-out zone for tied first hovers (KWR-DDR-001, D9). The 5.0 Ah cells change nothing in the ColdCell pack's charging rules: charge between 0 and 45 °C pack temperature in a fire-resistant box. Soldering the 8 AWG Core power leads needs a 100 W iron; hold the wire with pliers, and check polarity and the opposite-gender plugs with a meter before any pack is connected.

## Context

At TRL 3 (KWR-CAL-001 v0.2) four requirements were at risk or not met: R1 hover thrust margin (31.8 % on unmeasured maker-class thrust), R2 endurance (31.0 min against 45 min), R3 survey range (40.9 km against 40 km) and R7 take-off mass (10.58 kg against 8 kg). Each was put to Amish in `docs/REVIEW.md` as state, options and a recommendation, and listed as O1 to O4 in `docs/06-design-decisions.md`.

In parallel, Kitewright Core decision 33B lightens the core by moving its four 8 AWG power leads and AS150 plugs out of the core and into each frame's harness, so Range now supplies its own.

## Options considered

- **R1 (decision 36, O1):** A: keep 20 in propellers on 5212-class motors. B (chosen): 22 in propellers on 5215-class motors, booms 50 mm longer and 20 mm further out. C: keep A and change only if AltiRig measures under the target.
- **R2 and R3 (decision 37, O2 and O3):** A (chosen): two 6S3P packs of 5.0 Ah cells. B: two 6S4P packs. C: moulded carbon airframe with two 6S4P packs. Range option A was the same cell change; with 36B it is the combination v0.2 listed as option B for R3.
- **R7 (decision 38, O4):** A (chosen): keep the foam, glass and lite-ply airframe and weigh it at TRL 4. B: moulded carbon wing, tail and fuselage. C: fly one pack.

## Decision

1. **36B.** Lift motors are 5215-class (about 285 g, 62 mm can, at least 7.0 kgf maker static thrust with a 22 x 7 in propeller on 6S, USD 150 each) on mounts with a top plate at least 64 mm across; lift propellers are 22 x 7 in carbon (about 55 g, USD 50 each). The booms move from 470 to 490 mm from the centre line and the motors from 506 to 531 mm ahead of and behind the centre of gravity, so each boom is 1,142 mm (cut from a 1,200 mm tube) in place of 1,092 mm.
2. **37A.** Both ColdCell packs stay 6S3P, 138 x 75 x 82 mm and 1.40 kg, with high-rate 21700 cells of 5.0 Ah: 324 Wh each (USD 350 each, USD 60 more).
3. **38A.** The airframe is unchanged. R7 stays not met for the first prototype; the aircraft is weighed at TRL 4 and the target is reviewed against the first site's rules before a second prototype.
4. **Core power leads (Core 33B).** Range supplies the four 8 AWG power leads with AS150 plugs (two pack inputs, two frame outputs, opposite genders), soldered to the Core's pads at integration: BOM line 33, about 124 g, USD 60 (the Core's former BOM line 21).

No requirement target is restated.

## Results (KWR-CAL-001 v0.3)

| Requirement | Before | After | Status |
| --- | --- | --- | --- |
| R1, hover thrust margin at 5,000 m (at least 30 %) | 31.8 % at 10.58 kg | 52.0 % at 11.07 kg | Met on paper; thrust to measure in AltiRig |
| R2, endurance (at least 45 min) | 31.0 min | 32.9 min | Not met; accepted for the first prototype |
| R3, survey range (at least 40 km) | 40.9 km | 44.3 km | Met on paper |
| R7, take-off mass (no more than 8 kg) | 10.58 kg | 11.07 kg | Not met; weighed at TRL 4 |
| R9, discs below the wing-top plane (at least 70 mm) | 81 mm | 77 mm | Met by design |
| R10, cost | USD 3,945 | USD 4,293 | Met on paper |

The recommendations quoted 53.3 % and 35.6 min, 46.8 km for the options taken one at a time. Taken together, and with the Core power leads (0.12 kg) and slightly more drag from the larger motors, the figures are 52.0 %, 32.9 min and 44.3 km.

Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 4,293 (USD 707 under the target). Take-off mass 11.07 kg with the 1 kg payload (0.49 kg more: motors and propellers 0.36 kg, booms 0.01 kg, Core power leads 0.12 kg).

## Consequences

- The model (`cad/src/model.py`) gained three checks for the larger discs: at least 50 mm from the fuselage side (141 mm), at least 50 mm from the stabiliser (110 mm), and a motor no wider than its mount plate. All 72 solids in 48 parts pass; the lift and cruise discs are 33 mm apart (rule 20 mm).
- STEP and STL, the general arrangement (KWR-DWG-001 Rev P3), the concept blueprint (KWR-DWG-010 Rev P3), the concept media, the making sketches of the wing panel, pylon and boom, and the build plan overview, joints and steps are regenerated.
- The R2 and R7 shortfalls remain. A moulded carbon airframe with two 6S4P packs meets R2 on paper (45.6 min, USD 5,733) and stays the second-prototype path.
- Cross-repo: the ColdCell pack format now uses 5.0 Ah cells; Kitewright Core no longer supplies the power leads.
