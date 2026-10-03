---
doc_id: KWR-REQ-001
title: Kitewright Range requirements
project: Kitewright Range
doc_type: Requirements
version: "0.3"
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
---

# Kitewright Range requirements

Six of the ten requirements are met on paper or by design. Endurance (R2) and take-off mass (R7) are not met, and hover thrust margin (R1) and survey range (R3) are met by margins too thin to rely on until the motors and propellers are measured (KWR-CAL-001 v0.2, Table 6). The targets below are unchanged from the scaffold; what to do about each shortfall is an open decision for Amish (`docs/06-design-decisions.md`).

Table 1. Requirements and status at TRL 3

| ID | Requirement | Target | Verification (TRL 3 or later) | Status (KWR-CAL-001) |
| --- | --- | --- | --- | --- |
| R1 | Vertical take-off and landing at high altitude | Hover with at least 30% thrust margin at 0.74 kg/m3 air density (5,000 m) at maximum take-off mass | Lift motor and propeller thrust measured in AltiRig at 5,000 m density; margin calculated for the as-built mass | **At risk:** 31.8 % on maker-class thrust at 10.58 kg |
| R2 | Cruise endurance at altitude | At least 45 min wing-borne flight at 5,000 m and -20 C with a 1 kg payload and 20% reserve (target) | Energy model checked against bench power data, then timed flight at a high site | **Not met:** 31.0 min |
| R3 | Survey range | At least 40 km of survey track per flight at 5,000 m (target) | Flight log distance on a mapped survey pattern | **At risk:** 40.9 km |
| R4 | Payload capacity | 1.0 kg on the Kitewright mount within the centre of gravity range | Weigh and balance check; flight with a dummy payload | Met by design: mount centred on the CG, 28.4 % of the mean chord with or without the payload |
| R5 | Operating temperature | -20 to +40 C (-4 to +104 F) for all airframe electronics and servos | Cold chamber soak and function test of servos, motors and avionics | Met on paper by specification; cold ratings to confirm when parts are bought |
| R6 | Wind tolerance | Take off, transition and land in sustained wind of 10 m/s with gusts to 14 m/s | Flight tests with a logged anemometer at the launch site | Met on paper: cruise 21.9 m/s, stall 17.6 m/s, about 9 degrees of tilt holds a 14 m/s side gust in hover |
| R7 | Maximum take-off mass | No more than 8 kg including payload (target) | Weigh the complete aircraft | **Not met:** 10.58 kg |
| R8 | Transport | Packs into cases of no more than 1.3 m long; each carried load no more than 15 kg | Pack and measure; two-person carry trial | Met by design: longest part 1,205 mm; two cases of about 9 and 12 kg |
| R9 | Patent design-arounds held | Fixed motors, single wing, rotor discs clear of the wing-top plane in every revision | Design review checklist at each revision | Met by design: discs 81 mm below the wing-top plane, checked by the model |
| R10 | Open and buildable | All parts off the shelf or made with hobby tools; bill of materials at or below USD 5,000 | Costed BOM review; independent build by a second team | Met on paper: USD 3,945 against the USD 5,000 value-engineering target (USD 1,055 under) |

## Requirements at risk or not met

- R2 and R7 pull against each other: more pack energy adds mass, and a lighter aircraft carries less energy. The options are worked out in KWR-CAL-001 section H.
- R1 rests on maker-class thrust that has not been measured at 5,000 m density.
- R3 follows R2; any change that lengthens endurance lengthens range.

## Assumptions

- Hover and cruise figures are at the ISA density for 5,000 m (0.736 kg/m3) with the ColdCell packs warmed before take-off.
- Stock PX4 quadplane firmware is enough; no custom flight control code is needed (KWR-DDR-001, D1).
- ColdCell packs deliver 95 % of their capacity at -20 °C once warmed (cross-repo assumption).
- Most survey missions can start from a site within 10 km of the target lake.
