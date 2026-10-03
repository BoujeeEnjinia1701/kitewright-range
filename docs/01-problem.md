---
doc_id: KWR-PRB-001
title: Kitewright Range problem statement
project: Kitewright Range
doc_type: Problem statement
version: "0.2"
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
  change: Open questions answered by KWR-DDR-001; budget stated as a value-engineering target; co-design candidate named
---

# Kitewright Range problem statement

High-mountain hazards sit where people cannot easily go and where small drones struggle to fly. Lakes and glaciers above 4,500 m need regular, wide-area surveys, but the season is short, the air is thin and cold, and the tools that work are closed and costly.

## The problem

Glacial lakes are growing fast: their number rose 53% and their volume 48% between 1990 and 2020 ([Taylor et al., 2023](https://www.nature.com/articles/s41467-023-36033-x)). In India, work on 189 high-risk lakes is limited to four summer months because of elevation and weather ([ThePrint, 2024](https://theprint.in/india/govt-approves-rs-150-crore-for-glacial-lake-outburst-flood-risk-mitigation-programme-for-4-states/2232525/)). The South Lhonak lake in Sikkim, at 5,200 m, burst on 4 October 2023 after scientists had warned of it for years ([Nature India, 2023](https://www.nature.com/articles/d44151-023-00152-7)), and no early warning system was working there when it failed ([Mongabay India, 2023](http://india.mongabay.com/2023/10/no-early-warning-system-and-insufficient-dam-safety-turned-sikkim-flood-deadly/)).

Multirotors can fly high, as DJI showed with delivery tests between 5,300 m and 6,000 m on Everest in April 2024 ([DJI, 2024](https://www.dji.com/media-center/announcements/dji-completes-world-first-drone-delivery-tests-on-mount-everest-en)), but hovering is expensive in thin air and limits range. Fixed-wing VTOL drones solve the range problem; ArduPilot and PX4 already support the quadplane layout in open firmware ([ArduPilot](https://ardupilot.org/plane/docs/quadplane-overview.html)). What is missing is an open, documented airframe tuned for 5,000 m and -20 C, built around a shared payload mount and a cold-rated battery, at a cost a regional agency can replace after a crash.

## Users and context

| User | Need | Context |
| --- | --- | --- |
| State disaster management authorities and their field teams | Repeatable lake and moraine surveys without a long trek to each lake | Himalayan lakes at 4,500 to 5,500 m, short summer season, remote launch sites |
| University glaciology and hydrology groups | An airframe they can inspect, modify and fly with their own sensors | Field campaigns on glaciers and snow basins; data for peer-reviewed work |
| Mountain NGOs and community disaster committees | A drone they can maintain locally and afford to replace | Villages below known hazardous lakes in India, Nepal and Pakistan |
| Mountain rescue organisations | A wide-area first sweep before a multirotor narrows a search | Valleys, glaciers and high passes; daylight, variable wind |

## Operating environment

- Launch and landing on rough, sloping ground at up to 5,000 m, from a clearing of about 10 m by 10 m (estimate).
- Air temperature -20 to +25 C (-4 to +77 F); air density down to about 0.74 kg/m3 at 5,000 m in the standard atmosphere ([Engineering ToolBox](https://www.engineeringtoolbox.com/standard-atmosphere-d_604.html)).
- Valley winds and gusts; snow, sleet and strong ultraviolet light.
- No mains power at the launch site; charging from a generator, vehicle or solar kit at base camp.
- Beyond cellular coverage; line-of-sight radio link to a ground station.

## Constraints

- Value-engineering target USD 5,000 for the airframe with its share of core avionics, excluding payloads (a hypothetical control target, not a spending limit).
- All-electric only. The hybrid generator pack is shelved and not part of this design.
- Single fixed wing, fixed (non-tilting) lift and cruise motors, lift rotor discs clear of the wing-top plane, per the preliminary patent screen.
- Uses the Kitewright Core autopilot, power bus and payload mount unchanged; no frame-specific payload interface.
- Open design: hardware under CERN-OHL-S-2.0, software under an open licence compatible with PX4 (BSD 3-Clause) or ArduPilot (GPLv3).
- Civilian use only; transportable in a vehicle and carried by two people on a trail (target).

## Out of scope

- Tail-sitter, tilt-rotor and tilt-wing layouts.
- Hybrid, fuel-cell or combustion power.
- Aviation certification (FAA Part 107, EASA, India DGCA Drone Rules 2021) at this TRL; to be addressed if prototypes progress.
- Beyond-visual-line-of-sight approvals and satellite links in the first version.
- Any weapon, targeting or military payload.

## Prior work

| Prior work | What it does | Gap for these users | Source |
| --- | --- | --- | --- |
| Quantum Systems Trinity Pro | Commercial fixed-wing eVTOL mapping drone: 90 min flight time, 5.75 kg take-off mass, 5,500 m service ceiling, -12 to 50 C | Closed and about USD 23,790; ceiling and cold limit sit at the edge of Himalayan lake survey needs | [link](https://quantum-systems.com/trinity-pro/) |
| ArduPilot QuadPlane | Open flight control code for fixed wing aircraft with separate VTOL motors, including tilt and tail-sitter variants | Firmware only; no open, documented airframe tuned for 5,000 m and -20 C | [link](https://ardupilot.org/plane/docs/quadplane-overview.html) |
| US9120560B1, vertical take-off and landing aircraft (Vertical Autonomy) | Fixed wing with head and tail booms and four VTOL rotors in a plane even with the wing top surfaces; anticipated expiry 2033 | A live patent that constrains boom and rotor placement; Kitewright Range places the rotor discs clear of that plane | [link](https://patents.google.com/patent/US9120560B1/en) |
| DJI FlyCart 30 Everest delivery tests | Unmodified heavy-lift multirotor flew between 5,300 m and 6,000 m at -15 to 5 C in April 2024 | A multirotor built for short hauls, not long surveys; closed platform | [link](https://www.dji.com/media-center/announcements/dji-completes-world-first-drone-delivery-tests-on-mount-everest-en) |

## Co-design

A state disaster management authority or a university glaciology group already running Himalayan lake surveys, because they know the launch sites, flight distances and data formats the frame must meet, and can host early flight trials under their own permissions.

## Open questions

The scaffold's open questions were answered on 2026-10-03 under Amish's pre-approval (KWR-DDR-001):

- Reference firmware: PX4 quadplane, matching the Kitewright Core (D1).
- Wing: 2.50 m span in two 1.18 m panels, aspect ratio 8.9, set by the 1.3 m transport case (D2).
- Propellers: one set of 20 in propellers for every altitude band (D3).
- LakeWatch: 1 kg on Range; the sampling winch belongs on Kitewright Lift (D4).
- Co-design: the Sikkim State Disaster Management Authority is the first candidate to approach, a university glaciology group the second; neither is agreed (D8).

Requirements the design does not yet meet are open decisions for Amish in `docs/06-design-decisions.md`.

> **Safety:** Kitewright Range is a 10.6 kg aircraft with four 20 in lift propellers, a folding cruise propeller and about 580 Wh of lithium-ion cells. Propeller strikes, lithium fire after a crash or a cold charge, and a crash in remote terrain after loss of link are the main hazards; the precis (KWR-PRC-001) and the build plan's safety stops (KWR-BLD-001) set out the controls.
