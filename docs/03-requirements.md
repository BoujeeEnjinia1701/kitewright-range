---
doc_id: KWR-REQ-001
title: Kitewright Range requirements
project: Kitewright Range
doc_type: Requirements
version: "0.5"
status: Draft
date: '2026-10-04'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 2 concept status for every requirement
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 3 status from KWR-CAL-001 v0.2 on the constructable design; R10 cost stated against the value-engineering target
- version: "0.4"
  date: '2026-10-03'
  author: Amish Chadha
  change: 'Status from KWR-CAL-001 v0.3 after Amish''s 2026-10-03 decisions (KWR-DDR-003; Amish: "i agree with all the 46 recommendations you provided. please proceed."); targets unchanged; R2 and R7 shortfalls accepted for the first prototype'
- version: "0.5"
  date: '2026-10-04'
  author: Amish Chadha
  change: 'Status from KWR-CAL-001 v0.4 after Amish''s round-3 decision 10A (KWR-DDR-004; Amish: "For round 3, I agree with all your proposed recommendations"): the 0.99 kg Kitewright Core to the family envelope; targets unchanged'
---

# Kitewright Range requirements

Eight of the ten requirements are met on paper or by design (KWR-CAL-001 v0.4, Table 6). On 2026-10-04 Amish decided the Kitewright family reconciliation as recommended ("For round 3, I agree with all your proposed recommendations"; KWR-DDR-004): Range now carries the 0.99 kg Kitewright Core to the family mounting envelope, under the fuselage floor at the centre of gravity, with AS150 plugs on its packs. No requirement is restated. Endurance (R2) and take-off mass (R7) are not met. The targets below are unchanged. Amish decided the shortfalls on 2026-10-03 ("i agree with all the 46 recommendations you provided. please proceed."; KWR-DDR-003): 22 in propellers on 5215-class motors for R1, 5.0 Ah cells in the same two packs for R2 and R3, and the foam, glass and lite-ply airframe kept for the first prototype and weighed at TRL 4 for R7. No requirement is restated.

Table 1. Requirements and status at TRL 3

| ID | Requirement | Target | Verification (TRL 3 or later) | Status (KWR-CAL-001) |
| --- | --- | --- | --- | --- |
| R1 | Vertical take-off and landing at high altitude | Hover with at least 30% thrust margin at 0.74 kg/m3 air density (5,000 m) at maximum take-off mass | Lift motor and propeller thrust measured in AltiRig at 5,000 m density; margin calculated for the as-built mass | Met on paper: 48.3 % on maker-class thrust at 11.35 kg (22 in propellers, 5215-class motors); to measure in AltiRig |
| R2 | Cruise endurance at altitude | At least 45 min wing-borne flight at 5,000 m and -20 C with a 1 kg payload and 20% reserve (target) | Energy model checked against bench power data, then timed flight at a high site | **Not met:** 30.6 min with 5.0 Ah cells and the 0.99 kg Core under the floor; accepted for the first prototype (KWR-DDR-003) |
| R3 | Survey range | At least 40 km of survey track per flight at 5,000 m (target) | Flight log distance on a mapped survey pattern | Met on paper: 41.5 km |
| R4 | Payload capacity | 1.0 kg on the Kitewright mount within the centre of gravity range | Weigh and balance check; flight with a dummy payload | Met by design: the Core and its payload shoe under the CG, 28.3 % of the mean chord with or without the payload |
| R5 | Operating temperature | -20 to +40 C (-4 to +104 F) for all airframe electronics and servos | Cold chamber soak and function test of servos, motors and avionics | Met on paper by specification; cold ratings to confirm when parts are bought |
| R6 | Wind tolerance | Take off, transition and land in sustained wind of 10 m/s with gusts to 14 m/s | Flight tests with a logged anemometer at the launch site | Met on paper: cruise 22.6 m/s, stall 18.1 m/s, about 9 degrees of tilt holds a 14 m/s side gust in hover |
| R7 | Maximum take-off mass | No more than 8 kg including payload (target) | Weigh the complete aircraft | **Not met:** 11.35 kg; airframe kept and weighed at TRL 4 (KWR-DDR-003) |
| R8 | Transport | Packs into cases of no more than 1.3 m long; each carried load no more than 15 kg | Pack and measure; two-person carry trial | Met by design: longest part 1,205 mm; two cases of about 9 and 12.5 kg |
| R9 | Patent design-arounds held | Fixed motors, single wing, rotor discs clear of the wing-top plane in every revision | Design review checklist at each revision | Met by design: discs 77 mm below the wing-top plane, checked by the model |
| R10 | Open and buildable | All parts off the shelf or made with hobby tools; bill of materials at or below USD 5,000 | Costed BOM review; independent build by a second team | Met on paper: Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 4,314 (USD 686 under the target) |

## Requirements at risk or not met

- R2 and R7 pull against each other: more pack energy adds mass, and a lighter aircraft carries less energy. Amish accepted both shortfalls for the first prototype (KWR-DDR-003); with the reconciled Core no option inside the concept meets R2 on paper any more; a moulded carbon airframe with two 6S4P packs comes closest (42.5 min, USD 5,754) and is the second-prototype path (KWR-CAL-001 section H).
- R1 still rests on maker-class thrust that has not been measured at 5,000 m density; the 48.3 % margin leaves room for a thrust shortfall of about 12 % before the 30 % line.

## Assumptions

- Hover and cruise figures are at the ISA density for 5,000 m (0.736 kg/m3) with the ColdCell packs warmed before take-off.
- Stock PX4 quadplane firmware is enough; no custom flight control code is needed (KWR-DDR-001, D1).
- ColdCell packs deliver 95 % of their capacity at -20 °C once warmed (cross-repo assumption).
- Most survey missions can start from a site within 10 km of the target lake.
