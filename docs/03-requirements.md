---
doc_id: KWR-REQ-001
title: Kitewright Range requirements
project: Kitewright Range
doc_type: Requirements
version: "0.5"
status: Draft
date: '2026-10-03'
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
  change: Status after the round 2 requirement decisions (KWR-DDR-003), from KWR-CAL-001 v0.3; targets unchanged
- version: "0.5"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Figures from KWR-CAL-001 v0.4, with the Core power leads in the harness (Kitewright Core decision 17 B); status unchanged"
---

# Kitewright Range requirements

Eight of the ten requirements are met on paper or by design after the round 2 requirement decisions Amish made on 2026-10-03 (KWR-DDR-003): hover thrust margin (R1) and survey range (R3) moved from at risk to met on paper. Endurance (R2) and take-off mass (R7) are still not met (KWR-CAL-001 v0.4, Table 6). The targets below are unchanged from the scaffold; none of the decisions restated a requirement. The remaining endurance shortfall is an open decision for Amish (`docs/06-design-decisions.md`); R7 stays not met by decision (O4-A).

Table 1. Requirements and status at TRL 3

| ID | Requirement | Target | Verification (TRL 3 or later) | Status (KWR-CAL-001) |
| --- | --- | --- | --- | --- |
| R1 | Vertical take-off and landing at high altitude | Hover with at least 30% thrust margin at 0.74 kg/m3 air density (5,000 m) at maximum take-off mass | Lift motor and propeller thrust measured in AltiRig at 5,000 m density; margin calculated for the as-built mass | Met on paper: 51.7 % on maker-class thrust (estimate) at 11.09 kg, with 22 in propellers on 5215-class motors (KWR-DDR-003) |
| R2 | Cruise endurance at altitude | At least 45 min wing-borne flight at 5,000 m and -20 C with a 1 kg payload and 20% reserve (target) | Energy model checked against bench power data, then timed flight at a high site | **Not met:** 32.9 min with 5.0 Ah cells and the Core power leads (31.0 min before KWR-DDR-003) |
| R3 | Survey range | At least 40 km of survey track per flight at 5,000 m (target) | Flight log distance on a mapped survey pattern | Met on paper: 44.4 km (11 % margin) |
| R4 | Payload capacity | 1.0 kg on the Kitewright mount within the centre of gravity range | Weigh and balance check; flight with a dummy payload | Met by design: mount centred on the CG, 28.4 % of the mean chord with or without the payload |
| R5 | Operating temperature | -20 to +40 C (-4 to +104 F) for all airframe electronics and servos | Cold chamber soak and function test of servos, motors and avionics | Met on paper by specification; cold ratings to confirm when parts are bought |
| R6 | Wind tolerance | Take off, transition and land in sustained wind of 10 m/s with gusts to 14 m/s | Flight tests with a logged anemometer at the launch site | Met on paper: cruise 22.5 m/s, stall 18.0 m/s, about 9 degrees of tilt holds a 14 m/s side gust in hover |
| R7 | Maximum take-off mass | No more than 8 kg including payload (target) | Weigh the complete aircraft | **Not met:** 11.09 kg; foam, glass and lite-ply airframe kept for the first prototype and weighed at TRL 4 (KWR-DDR-003, O4-A) |
| R8 | Transport | Packs into cases of no more than 1.3 m long; each carried load no more than 15 kg | Pack and measure; two-person carry trial | Met by design: longest part 1,205 mm, lift boom 1,142 mm; two cases of about 9 and 12.5 kg |
| R9 | Patent design-arounds held | Fixed motors, single wing, rotor discs clear of the wing-top plane in every revision | Design review checklist at each revision | Met by design: discs 78 mm below the wing-top plane, checked by the model |
| R10 | Open and buildable | All parts off the shelf or made with hobby tools; bill of materials at or below USD 5,000 | Costed BOM review; independent build by a second team | Met on paper: USD 4,285 against the USD 5,000 value-engineering target (USD 715 under) |

## Requirements not met

- R2 and R7 pull against each other: more pack energy adds mass, and a lighter aircraft carries less energy. The options for R2 on the decided design are worked out in KWR-CAL-001 v0.4 section H; only a moulded airframe with 6S4P packs reaches 45 min on paper.
- R7 is not met by decision for the first prototype (KWR-DDR-003, O4-A).
- R1 is met on maker-class thrust that has not been measured at 5,000 m density; AltiRig measures it before any flight.
- R3 follows R2; any change that lengthens endurance lengthens range.

## Assumptions

- Hover and cruise figures are at the ISA density for 5,000 m (0.736 kg/m3) with the ColdCell packs warmed before take-off.
- Stock PX4 quadplane firmware is enough; no custom flight control code is needed (KWR-DDR-001, D1).
- ColdCell packs deliver 95 % of their capacity at -20 °C once warmed (cross-repo assumption).
- Most survey missions can start from a site within 10 km of the target lake.
