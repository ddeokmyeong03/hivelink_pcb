# HIVE LINK Core Rev.A — PCB

HIVE LINK is a detachable heterogeneous unmanned-system mission node developed by TRUE:D Labs.

This repository is the GitHub/KiCanvas working repository for **HIVE LINK Core Rev.A**.

## Open in KiCanvas

### Repository
https://kicanvas.org/?github=https://github.com/ddeokmyeong03/hivelink_pcb

### System schematic overview
https://kicanvas.org/?github=https://github.com/ddeokmyeong03/hivelink_pcb/blob/main/HIVE_LINK_RevA.kicad_sch

### PCB placement preview
https://kicanvas.org/?github=https://github.com/ddeokmyeong03/hivelink_pcb/blob/main/HIVE_LINK_RevA_KiCanvas_Placement_Preview.kicad_pcb

## Current engineering milestone

**Rev.A / v0.8 — electrical architecture + footprint freeze + physical placement planning**

Current GitHub root files are intentionally optimized so the project can be opened in KiCanvas now:

- `HIVE_LINK_RevA.kicad_pro` — project
- `HIVE_LINK_RevA.kicad_sch` — KiCanvas system-level overview
- `HIVE_LINK_RevA.kicad_pcb` — 100 × 70 mm PCB floorplan / placement guide
- `HIVE_LINK_RevA_KiCanvas_Placement_Preview.kicad_pcb` — clearer placement preview
- `HIVE_LINK_RevA.kicad_dru` — conservative custom DRC rules

> **Important:** the root schematic currently shown in KiCanvas is a system-level overview, not the fabrication-release detailed schematic. The detailed multi-sheet electrical capture is still under native KiCad verification and is being synchronized incrementally.

## Electrical design baseline

Completed in the engineering design baseline:

- 7–24 V protected power input
- TPS26632 eFuse / reverse-polarity protection
- INA226 power telemetry
- AP64501 5 V / 5 A system rail
- independent 3.3 V node-controller rail
- STM32G0B1 node controller
- Raspberry Pi CM4 carrier interface
- partial-power-down-safe STM32 ↔ CM4 isolation
- dual CAN-FD
- Pixhawk / PX4 TELEM interface
- Gigabit Ethernet
- USB Host + eMMC recovery path
- ATECC608C hardware-backed node identity
- universal adapter expansion interface

## Board baseline

- Board: **100 × 70 mm**
- Layers: **4**
- Nominal thickness: **1.6 mm**
- Baseline stack-up: **JLCPCB JLC04161H-7628**
- L2: continuous GND plane
- L3: power distribution
- Ethernet target: 100 Ω differential
- USB 2.0 target: 90 Ω differential

## Fabrication gate

This repository is **not fabrication-ready yet**.

Required before Gerber release:

1. Open in native KiCad
2. Run ERC
3. Update PCB from Schematic
4. Apply/verify physical placement
5. Route Power → Ethernet → USB → CAN → low-speed signals
6. Refill zones and verify return-current paths
7. Run DRC
8. Independent Gerber/drill review
9. Power-only bench bring-up without CM4 installed
10. Install CM4 only after rails and protection are verified

## KiCanvas note

KiCanvas is used here for browser-based review and sharing. Native KiCad remains the source of truth for ERC, PCB synchronization, routing and DRC.

## Status

Latest GitHub/KiCanvas synchronization baseline: **v0.8**
