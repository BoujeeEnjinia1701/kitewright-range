# Review note: Kitewright Range

## Session 2026-10-03: round 2 requirement decisions applied

Amish, 2026-10-03: "i approve all of the 47 recommendations provided by you. Execute them." For this repo that decides O1 to O4 as recommended, recorded in `docs/decisions/0003-requirement-decisions-round2.md` (KWR-DDR-003). O3's recommendation was "A, decided together with O2; B if O1-B is chosen"; O1-B is chosen, so O3 is applied as its option B, the combined effect of O1-B and O2-A (about 45.0 km, +USD 280, +0.40 kg combined). It needs no change of its own. TRL 3 scope only: nothing built, bought or tested.

### What was done

- `cad/src/model.py`: lift propellers 20 in to 22 in (558.8 mm) on 5215-class motors (envelope 62 x 35 mm and 285 g, estimates; propellers 55 g; mounts 40 g); booms 20 mm further out (490 mm from the centre line) and 50 mm longer (1,142 mm), motors 531 mm ahead of and behind the centre of gravity. Constructability checks pass: 72 solids in 48 parts, no overlaps, nothing floating, discs 78 mm below the wing-top plane (rule 70 mm), lift discs 33 mm clear of the cruise propeller disc, every part fits the 1.3 m case.
- `docs/04-calcs/sizing.py`: thrust 68.7 N (7.0 kgf, maker-class estimate), 5.0 Ah cells, lift motor drag from the model envelope; the options now cover the endurance still not met on the decided design. Re-run: `results.csv` and `01-sizing.md` (KWR-CAL-001 v0.3).
- `bom/bom.csv`: lines 12 (boom tube 1,200 mm, USD 52), 18 (mount for a 5215-class motor), 20 (5215-class motor, USD 148), 21 (22 in propeller, USD 50) and 28 (ColdCell pack of 5.0 Ah cells, 324 Wh, USD 350). All new prices are estimates derived from the lines they replace.
- Regenerated with the repo's scripts: STEP and STL (`cad/step/`, `cad/stl/`); general arrangement KWR-DWG-001 Rev P3 (`cad/src/sheets.py`); making sketches KWR-DWG-105, 106, 108 and 109 at Rev P2 and all other sketches, joint close-ups, steps and overview (`cad/src/build_plan_media.py`; the joint windows were widened for the booms at 490 mm); concept media hero, cutaway, exploded, flow and blueprint KWR-DWG-010 Rev P3 (`cad/src/concept_media.py`); `media/model.glb` (about 1 MB, linear deflection 1.0 mm, angular deflection 0.35 rad) and `media/viewer.html`.
- Documents: KWR-REQ-001 v0.4 (status only, targets unchanged), KWR-PRC-001 v0.4, KWR-PRB-001 v0.3 (propeller size and safety note), KWR-BLD-001 v0.2 (hardpoints 490 mm out, boom 1,142 mm, motor centres 1,062 mm apart, bought parts, safety note), KWR-DEC-001 v0.2 (O1 to O4 decided, O5 added, change log), README figures, `cad/src/product_model.py` docstring, `project.yaml` trl_evidence.
- Not regenerated: `media/render-hero.png` and the other photoreal renders, `media/card.png` and `media/social-preview.png` (made on Amish's Mac from the photoreal renders).

### Requirement status

| ID | Before (KWR-CAL-001 v0.2) | After (KWR-CAL-001 v0.3) |
| --- | --- | --- |
| R1 | At risk: 31.8 % | Met on paper: 53.4 % on maker-class thrust (estimate) |
| R2 | Not met: 31.0 min | Not met: 33.6 min |
| R3 | At risk: 40.9 km | Met on paper: 45.0 km (12 % margin) |
| R7 | Not met: 10.58 kg | Not met: 10.97 kg, airframe kept by decision (O4-A) |
| R9 | Met by design: discs 81 mm below the wing-top plane | Met by design: 78 mm |
| R10 | Met on paper: USD 3,945 | Met on paper: USD 4,225 |

Other figures: hover 1,743 W and 81 A at 5,000 m (13.4 A per cell); cruise 22.3 m/s, 624 W, L/D 7.4; spar safety factor 2.9 to 2.8, lift boom 10.8 to 8.4, pylon bolts 12.5 to 9.9.

### Cost

Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 4,225 (USD 775 under the target), up USD 280 from USD 3,945: lift motors +USD 112, propellers +USD 40, boom tubes +USD 8, 5.0 Ah cells +USD 120. `budget_usd` is the target and is unchanged.

### Decisions for Amish

**O5. R2 endurance, still not met.** **Proposed, awaiting Amish.** State: 33.6 min against 45 min on the decided design; cause: 648 Wh drives a 10.97 kg aircraft with a zero-lift drag coefficient of 0.079 at 624 W in cruise, and the heavier lift system takes back part of the 5.0 Ah cells' gain.
- A: keep the decided design for the first prototype and measure drag, mass and pack energy at TRL 4. 33.6 min; no change.
- B: two 6S4P packs of 5.0 Ah cells. 41.9 min; +USD 233; +0.88 kg; hover margin 42.0 % (R1 still met with the 22 in propellers); R7 worse at 11.85 kg; a larger ColdCell format whose fit in the bays is unchecked.
- C: moulded carbon wing, tail and fuselage. 37.6 min; +USD 1,200; -0.69 kg.
- D: moulded airframe and two 6S4P packs of 5.0 Ah cells. 46.4 min, R2 met on paper; +USD 1,433; USD 5,658 in all, USD 658 over the value-engineering target.
- **Recommendation: A** for the first prototype; D is the second-prototype path once the first one's drag and mass are measured, with B as the cheaper step if the measured drag is lower than estimated.

### Safety notes

- The lift propellers are now 22 in: the propeller safety stop, arming plug, lockable switch, tie-downs and 15 m keep-out zone (D9) apply unchanged; the lift discs pass 33 mm from the cruise propeller disc, so both sets of propellers stay off until that stop.
- The packs hold about 650 Wh (was about 580 Wh): the charging rules (0 to 45 °C, fire-resistant box, never unattended) and crash-pack isolation are unchanged and apply to the 5.0 Ah cells.
- The 53.4 % margin rests on a maker-class thrust estimate. The first free hover still waits for AltiRig thrust data at 0.736 kg/m3, ten logged tied hovers and the wing spar proof load (TRL 4 steps in the build plan's safety stop 4); the spar margin is now 2.8.

### Cross-repo actions (sibling repos not edited)

- ColdCell: a 6S3P pack of 5.0 Ah high-rate 21700 cells, same 138 x 75 x 82 mm and 1.40 kg, about 324 Wh, at least 14 A per cell continuous when warmed.
- AltiRig: first job is the 5215-class motor with a 22 in propeller at 0.736 kg/m3.
- Kitewright Core: the 6S bus now carries about 81 A in hover at 5,000 m (about 40 A per pack).
- ColdCell (follow-up for the ColdCell repo, **Proposed, awaiting Amish**): ColdCell needs a 6S3P pack configuration of 5.0 Ah high-rate 21700 cells to match decision 21 A (O2-A), at the same 138 x 75 x 82 mm and 1.40 kg if the cells allow.

### Core power leads (follows from Kitewright Core decision 17 B)

- Core decision 17 B moved the four 8 AWG pack and frame power leads with AS150 plugs out of the Core into each frame's harness. Range's harness, BOM line 29, now carries them: 8 AWG red and black 2 m and four AS150 halves, +USD 60 and +0.124 kg, priced as on Kitewright Lift; `docs/04-calcs/sizing.py` carries the 0.124 kg at the centre of gravity, and build plan step 4 and section 3.14 say where they solder.
- Re-run results (`results.csv`): take-off mass 10.97 to 11.09 kg, **R7 still not met**; hover margin 53.4 to 51.7 % (R1 still met on paper); endurance 33.6 to 32.9 min (R2 not met); range 45.0 to 44.4 km (R3 still met); estimated cost USD 4,225 to 4,285 (USD 715 under the value-engineering target).
- Open point: the Core's pack inputs are AS150 while the ColdCell packs are specified with XT90 leads; either the ColdCell packs for Range take AS150 pigtails or the harness carries adaptors. Proposed, awaiting Amish (with the ColdCell follow-up above).

### Re-render

The hero geometry changed visibly: lift propellers 10 % larger in diameter, booms 50 mm longer and 20 mm further out, larger lift motors. The photoreal hero, exploded and detail views and the cards should be re-rendered on the Mac from `cad/src/product_model.py`.

### Recommended next step

- Amish decides O5. Then re-render the photoreal views and cards on the Mac and run the release gate. The design is ready for TRL 4 parts purchase and the AltiRig thrust test of the 5215-class motor with a 22 in propeller; that is a recommendation only, not started.

## Session 2026-09-30: scaffolded

### What was done

- Repository created from kit 1.6.0 at TRL 1, target TRL 2.
- `docs/01-problem.md` (KWR-PRB-001 v0.1): problem with cited evidence, users, environment, constraints, prior work, open questions.
- `docs/02-concept.md` (KWR-PRC-001 v0.1): how it works, components, patent design-arounds, shared blocks, safety.
- `docs/03-requirements.md` (KWR-REQ-001 v0.1): 10 proposed requirements.
- `README.md` with concept rationale, burning platform, where it could be used, and what sparked the idea.

### Next

- Run `/populate` to bring the repo to a strong TRL 2 with concept media.

## Session 2026-10-03: TRL 2 (populate, under Amish's pre-approval)

Run as the first half of `/to-trl3` on kit 1.7.0, under Amish's 2026-10-03 instructions: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and, for Batch 2, "Proceed with the remaining 15 scaffolds".

### What was done

- Kit 1.7.0 installed (`.kit/`, `.claude/commands/`); root `CLAUDE.md` replaced from `.kit/CLAUDE.md`.
- `docs/01-problem.md` (KWR-PRB-001 v0.2): open questions answered, value-engineering wording, co-design candidate, safety note.
- `docs/03-requirements.md` (KWR-REQ-001 v0.2): concept status for each requirement (targets unchanged).
- `docs/02-concept.md` (KWR-PRC-001 v0.2): how it works, components, first-order numbers, design choices, safety.
- `docs/decisions/0001-trl2-review-decisions.md` (KWR-DDR-001): D1 to D10.
- Massing model, concept media and BOM, then carried straight into TRL 3 (below), so the TRL 2 media were superseded by the TRL 3 set in the same session.

### Results at TRL 2

- The TRL 2 concept was carried straight into the TRL 3 calculations in the same session; all figures are the TRL 3 figures below.

### Decisions made under the pre-approval (KWR-DDR-001)

- D1 PX4 quadplane firmware; D2 2.5 m two-piece wing; D3 one 20 in propeller set; D4 the LakeWatch winch belongs on Kitewright Lift; D5 nose tractor and tail boom; D6 two ColdCell 6S3P Li-ion packs; D7 foam, glass, lite-ply and printed build; D8 Sikkim State Disaster Management Authority as the first co-design candidate to approach (not agreed), a university glaciology group second; D9 staged powered tests with tie-downs, keep-out zone, arming plug and lockable switch (conservative; relax the tie-down only after 10 logged tied hovers with no fault); D10 return to launch and land vertically on loss of link or low battery, land in place at the reserve, geofence.

### Safety concerns

- Large propellers, lithium-ion packs and a crash in remote terrain; covered in the precis safety section and D9, D10.

## Session 2026-10-03: TRL 3 (advance, design for construction, build plan)

### What was done

- `docs/04-calcs/01-sizing.md` (KWR-CAL-001 v0.2) with `docs/04-calcs/sizing.py` and `results.csv`: mass and balance from the model, drag build-up, hover at 5,000 m, energy, structure, geometry rules, cost, options for every shortfall, and a results table against every requirement.
- `cad/src/model.py`: parametric build123d model of the constructable design with constructability checks (72 solids in 48 parts: no overlaps, nothing floating, rotor discs at least 70 mm below the wing-top plane, lift and cruise discs apart, every part shorter than a 1.3 m case). STEP in `cad/step/` (assembly, fuselage, right wing panel, right boom pylon, landing leg parts, tail) and STL of the printed parts in `cad/stl/`.
- `cad/src/sheets.py`: general arrangement KWR-DWG-001 at Rev P2 (P1 preliminary GA, P2 design for construction).
- `bom/bom.csv`: 32 lines, every one priced, with a supplier type.
- `cad/src/concept_media.py`: hero, cutaway, exploded view with BOM numbers, blueprint KWR-DWG-010 Rev P2, glTF viewer (`media/model.glb`, about 1 MB, coarse tessellation) and energy flow per flight.
- `docs/decisions/0002-design-for-construction.md` (KWR-DDR-002): changes C1 to C13.
- `cad/src/build_plan_media.py`: overview, 13 making sketches (KWR-DWG-101 to 113), 8 joint close-ups, 16 assembly steps.
- `docs/05-build-plan.md` (KWR-BLD-001), `docs/06-design-decisions.md` (KWR-DEC-001).
- `cad/src/product_model.py` (appearance model, hero, exploded and detail views) and render scenes exported to `/home/claude/renders/kitewright-range/` for the photoreal renders on Amish's Mac.
- `docs/02-concept.md` v0.3 and `docs/03-requirements.md` v0.3 brought to the TRL 3 figures; `project.yaml` at TRL 3, target 3, `design_state: constructable`; README leads with `media/render-hero.png` (made on the Mac) and has the build plan link and "Building the prototype".

### Results (KWR-CAL-001 v0.2)

| Quantity | Value |
| --- | --- |
| Take-off mass with 1 kg payload | 10.58 kg (packs 2.80 kg) |
| Centre of gravity | 28.4 % of the mean chord, unchanged by the payload |
| Hover at 5,000 m | 1,815 W; thrust margin 31.8 % |
| Cruise | 21.9 m/s, L/D 7.5, 585 W |
| Endurance and range on the wing | 31.0 min, 40.9 km with a 20 % reserve |
| Lowest structural safety factor | 2.9, wing spar at 2.5 g |
| Cost | Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 3,945 (USD 1,055 under the target) |

### Requirements not met or at risk

- R1 hover thrust margin: at risk (31.8 %, on maker-class thrust not yet measured).
- R2 endurance: not met (31.0 min).
- R3 survey range: at risk (40.9 km).
- R7 take-off mass: not met (10.58 kg).
- All others met on paper or by design; R5 depends on cold ratings to confirm when parts are bought.

### Decisions for Amish

Each item is **Proposed, awaiting Amish**, and is listed in `docs/06-design-decisions.md` under Open decisions. Figures are from KWR-CAL-001 v0.2, Table 5; the design stays as it is until Amish decides.

**O1. R1 hover thrust margin.** State: 31.8 % at 10.58 kg and 0.736 kg/m3, against the requirement's margin; cause: it rests on a maker-class 5.8 kgf sea-level thrust scaled by density, with no measured data, so a few percent of thrust shortfall or mass growth erases it.
- A: keep 20 in propellers on 5212-class motors. Margin 31.8 %; no cost or mass change.
- B: 22 in propellers on 5215-class motors. Margin 53.3 %; +USD 160; +0.40 kg; endurance -1.7 min, range -1.7 km; booms 50 mm longer and 20 mm further out to keep the disc clearances.
- C: keep A now and switch to B only if AltiRig measures less than the requirement. No change now; the risk moves to the test.
- **Recommendation: B.** Hover authority at 5,000 m is the aircraft's safety margin in gusts, so the conservative choice applies; the cost is small and combined with O2-A the endurance still improves on today's design.

**O2. R2 endurance.** State: 31.0 min against the requirement; cause: 583 Wh in 2.80 kg of packs drives a 10.6 kg aircraft with a zero-lift drag coefficient of 0.077 (stopped lift motors and an external payload), needing 585 W in cruise.
- A: two 6S3P packs of 5.0 Ah high-rate 21700 cells. 35.6 min; +USD 120; no mass change; hover margin unchanged.
- B: two 6S4P packs. 38.9 min; +USD 190; +0.88 kg; hover margin falls to 21.7 % (R1 then fails).
- C: moulded carbon wing, tail and fuselage with two 6S4P packs. 43.3 min; +USD 1,390; +0.19 kg; margin 29.4 %; USD 5,335 in all.
- **Recommendation: A** for the first prototype; C is the path for a second prototype once the first one's drag and mass are measured.

**O3. R3 survey range.** State: 40.9 km against the requirement, a 2 % margin; cause: range follows endurance at 21.9 m/s.
- A: 5.0 Ah cells as O2-A. 46.8 km; +USD 120; no mass change.
- B: A together with O1-B. 45.0 km; +USD 280; +0.40 kg.
- C: keep as is. 40.9 km; no change.
- **Recommendation: A**, decided together with O2 (B if O1-B is chosen).

**O4. R7 take-off mass.** State: 10.58 kg against the requirement; cause: ColdCell packs 2.80 kg, lift system with mounts 1.32 kg, payload 1.00 kg and Core avionics 0.78 kg leave 4.7 kg for an airframe built with hobby methods.
- A: keep the foam, glass and lite-ply airframe. 10.58 kg; no change.
- B: moulded carbon wing, tail and fuselage. 9.89 kg; +USD 1,200 (USD 5,145 in all, USD 145 over the value-engineering target); endurance +4.1 min.
- C: fly with one pack. 9.18 kg; endurance 15.0 min, which fails R2 and R3 by far.
- **Recommendation: A** for the first prototype, weighed at TRL 4. No option inside the concept reaches the target without giving up endurance; if the target reflects a regulatory class at the first site, that site's rules should set the target before the second prototype.

### Decisions made under the pre-approval

- KWR-DDR-001 D1 to D10 (TRL 2 review) and KWR-DDR-002 C1 to C13 (design for construction), both dated 2026-10-03 and recorded in `docs/06-design-decisions.md` with Amish's words.

### Design changes made for construction (KWR-DDR-002)

- C1 tail on its own carbon tail boom, not on the lift booms.
- C2 lift booms on printed pylons through-bolted under the wing with clamp caps; rotor discs 81 mm below the wing-top plane.
- C3 booms 470 mm out, 38 mm clear of the cruise propeller disc.
- C4 lift motors 506 mm ahead of and behind the centre of gravity.
- C5 tractor cruise motor at the nose on a printed cone, folding propeller.
- C6 two wing panels on a carbon joiner, nylon wing bolts, straight spar at 30 % chord.
- C7 lite-ply fuselage box with packs either side of the joiner and Core avionics in front.
- C8 four faired landing legs.
- C9 wing wiring conduits and root plugs.
- C10 payload mount on the centre of gravity.
- C11 printed tail socket and tail mount.
- C12 hatch with GNSS mast and arming switch.
- C13 heated pitot in the left wing.

### Build plan findings

- The concept's booms could not carry the tail and still fit the 1.3 m case (C1).
- Without a pylon depth rule, the rotor discs would sit near the wing plane the design-around avoids; the model now checks the 70 mm rule on every run.
- The boom spacing first tried (450 mm) put the front lift discs within 18 mm of the cruise propeller disc; 470 mm gives 38 mm.
- Weighing every made part from the model raised the take-off mass from the TRL 2 estimate to 10.58 kg; printed parts are weighed as walls plus infill, and the pylons were shortened to 160 mm to save 0.2 kg.
- The tightest structural margin is the wing spar (2.9 at 2.5 g); the build plan's safety stop 4 requires a proof load before free flight (TRL 4).

### Appearance model (product_model.py)

- Every part comes from `model.py`. The only difference: the lift and cruise propellers are drawn as tapered blades in place of the model's flat blade envelopes of the same diameter. Proposed, awaiting Amish (appearance only).
- The detail view should be rendered with `--focus` on the left front lift motor and pylon.
- Hero framing: the 1.75 m person stands beyond the right wing tip, behind the aircraft as seen from the hero camera, so it never stands between the camera and the product.

### Safety concerns

- Four 20 in lift propellers and a 14 in cruise propeller: fitted only at the propeller safety stop, arming plug and lockable switch, tied first hovers in a 15 m keep-out zone (D9).
- About 580 Wh of Li-ion: charge between 0 and 45 °C pack temperature in a fire-resistant box; crash-damaged packs isolated outdoors.
- Loss of link or power in remote terrain: return on the wing and land vertically, land in place at the reserve, geofence (D10).
- Wing spar margin 2.9 at 2.5 g: proof-load before free flight.
- High-altitude sites may lie in restricted border or protected areas; fly only with the site partner's permissions.

### Cross-repo actions (sibling repos not edited)

Kitewright Core and Kitewright Lift are being done in parallel; these shared-interface assumptions are used here and should be confirmed in those repos:

1. **Kitewright Core, firmware:** PX4 (VTOL standard quadplane) as the family reference, with a Range parameter set at sea level, 3,000 m and 5,000 m.
2. **Kitewright Core, avionics envelope:** 180 x 110 x 60 mm, 0.70 kg, plus a GNSS mast of 0.08 kg through the hatch; USD 900 as Range's share in the BOM.
3. **Kitewright Core, payload mount:** a 160 x 80 x 12 mm plate with a rail, locking pin and DS-014 connector, 0.12 kg, fixed by four M4 bolts; payload envelope 150 x 90 x 100 mm and 1 kg with its centre of gravity under the mount centre; connector lead through the fuselage floor.
4. **Kitewright Core, power:** a 6S bus (21.6 V nominal Li-ion) taking two packs in parallel, carrying about 85 A in hover at 5,000 m (about 42 A per pack); an arming plug in the main lead and a lockable arming switch.
5. **ColdCell:** a 6S3P pack of 4.5 Ah 21700 cells, 291.6 Wh, 1.40 kg, 138 x 75 x 82 mm, XT90 lead, film heater and BMS thermostat holding the cells above 15 °C, 95 % usable at -20 °C ambient once warmed; a 5.0 Ah cell variant is proposed in O2.
6. **Kitewright Lift:** shares the 6S bus voltage, the Core mount and the ColdCell pack format; the LakeWatch sampling winch is assigned to Lift (D4).
7. **AltiRig:** first job is the thrust of a 5212-class motor with a 20 x 6.5 in propeller (and the 5215-class with 22 in, for O1) at 0.736 kg/m3.

### Recommended next step

- Amish decides O1 to O4. Then render the hero, exploded and detail views on the Mac from the exported scenes, make the cards, and run the release gate. The design is ready for TRL 4 parts purchase and AltiRig thrust tests once O1 is settled; that is a recommendation only, not started.

## 2026-10-03: photoreal renders

Rendered with Blender Cycles on Amish's Mac from `cad/src/product_model.py`; captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` made with `.kit/cards.py`. Views: hero, exploded, detail. image_qc passes and `render.py --check` has no FAIL.
