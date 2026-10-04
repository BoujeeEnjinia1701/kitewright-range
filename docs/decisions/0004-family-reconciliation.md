---
doc_id: KWR-DDR-004
title: Kitewright Range round-3 decision, Kitewright family reconciliation
project: Kitewright Range
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-04'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-04'
  author: Amish Chadha
  change: Amish's round-3 decision 10A carried out for Range
---

# 0004: Kitewright family reconciliation (round 3)

- **Date:** 2026-10-04
- **Status:** accepted. Decided by Amish Chadha on 2026-10-04: "For round 3, I agree with all your proposed recommendations" (round 3, item 10A).

## Context

Range had assumed a 180 x 110 x 60 mm Core avionics box of 0.70 kg in its front bay, a separate 160 x 80 x 12 mm payload mount of 0.12 kg under the centre of gravity, a GNSS mast of 0.08 kg and XT90 leads on its packs. The Core, after its decision 33B, is a 240 x 150 mm plate with its own rail and pins that hangs under a frame's deck on a 220 x 130 mm M4 pattern, weighs 0.99 kg and takes AS150 plugs (KWR-CAL-001 v0.3 noted the gap and an estimate of 0.3 min less endurance from the mass alone).

## Decision

10A: AS150 plugs everywhere; one mounting envelope for the Core shared by Lift and Range, with the Core's drawing as the reference; Range recomputed with the 0.99 kg Core; the Kitewright interface table in each repository's review note.

## Carried out

| Item | Was | Now |
| --- | --- | --- |
| Kitewright Core | Avionics box in the front bay; separate payload mount plate under the CG | The Core hung under the floor at the CG to KWC-DWG-001 (`cad/src/core_envelope.py`, the same file as Lift's), its rail pointing aft so payloads slide in from the tail |
| Fuselage | 140 mm wide; rear bulkhead at 585 mm | 156 mm wide (150 mm inside, as the Core asks); floor cut with the 200 x 112 mm opening and four 4.3 mm holes; rear bulkhead at 645 mm |
| Core deck doubler (new) | None | 6 mm birch, 300 x 150 mm, with the opening, four holes and M4 T-nuts, on the floor |
| Packs | Either side of the joiner on the floor | Front pack in the nose bay (60 to 198 mm), rear pack on the doubler behind the lid (506 to 644 mm); the centre of gravity stays at 28.3 % of the mean chord |
| GNSS and antennas | GNSS mast on the hatch | The Core's GNSS receiver on the hatch mast and its three antennas on the hatch, on extension cables |
| Payload envelope | 150 x 90 x 100 mm under a mount plate | 140 x 88 x 100 mm under a 184 x 128 x 5 mm payload shoe, inside the Core's 88 mm neck and clear of its pigtail plug |
| Pack leads | XT90 | AS150 |

## Results (KWR-CAL-001 v0.4)

- Take-off mass 11.35 kg (0.28 kg more); hover margin 48.3 % (R1 met on paper); endurance 30.6 min (R2 not met, accepted); range 41.5 km (R3 met on paper, 4 % margin); centre of gravity 28.3 % of the mean chord (R4).
- Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 4,314 (USD 686 under the target).
- The endurance falls 2.4 min, not the 0.3 min the Core's mass alone would cost: the doubler, wider fuselage and leads cost about 1.0 min and the drag of the Core hung under the floor about 1.2 min. LakeWatch's R5 is restated on 30.6 min.

## Consequences

- No option in KWR-CAL-001 section H now meets R2 on paper; the moulded airframe with 6S4P packs comes closest (42.5 min).
- R3's margin is 4 %; a measured drag or thrust shortfall at TRL 4 could take it below 40 km.

> **Safety:** The Core's pin knobs hang 140 mm above the ground and the payload 80 mm; land only on the four feet on clear ground. The Core power leads are soldered with every pack disconnected and checked for polarity before the first pack goes on.
