# HIVE LINK Core Rev.A — PCB

HIVE LINK is a detachable heterogeneous unmanned-system mission node developed by TRUE:D Labs.

This repository contains the **HIVE LINK Core Rev.A** KiCad hardware design.

## Open in KiCanvas

View the repository directly in KiCanvas:

https://kicanvas.org/?github=https://github.com/ddeokmyeong03/hivelink_pcb

Direct project files:
- `HIVE_LINK_RevA.kicad_pro`
- `HIVE_LINK_RevA.kicad_sch`
- `HIVE_LINK_RevA.kicad_pcb`

## Current engineering milestone

**Rev.A / v0.8 — Electrical capture + footprint freeze + placement planning**

Completed:
- 7–24 V protected power input
- 5 V / 5 A system rail
- independent 3.3 V node-controller rail
- STM32G0B1 node controller
- Raspberry Pi CM4 carrier interface
- partial-power-down-safe STM32↔CM4 GPIO isolation
- dual CAN-FD
- Pixhawk/PX4 TELEM interface
- Gigabit Ethernet
- USB Host + eMMC recovery path
- ATECC608C hardware node identity
- custom project footprints
- 100 × 70 mm Rev.A mechanical target
- full placement coordinate plan

Current hard gate before fabrication:
1. Open in native KiCad
2. Run ERC
3. Update PCB from Schematic
4. Apply placement plan
5. Route Power → Ethernet → USB → CAN → low-speed signals
6. Run DRC
7. Gerber / drill / BOM / CPL review
8. Bench bring-up without CM4 installed first

## Important

This repository is **not yet fabrication-ready**. The current files are an engineering MVP design under verification. Native KiCad ERC/DRC has not yet been run in the ChatGPT execution environment.

## Board baseline

- Board: 100 × 70 mm
- Layers: 4
- Baseline stack-up: JLCPCB JLC04161H-7628 / 1.6 mm
- L2: continuous GND plane
- L3: power distribution
- Ethernet target: 100 Ω differential
- USB 2.0 target: 90 Ω differential

## Project structure

```text
HIVE_LINK_RevA.kicad_pro
HIVE_LINK_RevA.kicad_sch
HIVE_LINK_RevA.kicad_pcb
HIVE_LINK_RevA.kicad_dru

01_POWER_INPUT.kicad_sch
02_POWER_5V.kicad_sch
03_CM4_CORE.kicad_sch
04_STM32_NODE_CTRL.kicad_sch
05_CAN_DUAL.kicad_sch
06_UART_FC.kicad_sch
07_USB.kicad_sch
08_ETHERNET.kicad_sch
09_IDENTITY_RTC.kicad_sch
10_EXPANSION_IO.kicad_sch
11_DEBUG_TEST.kicad_sch

HIVE_LINK.pretty/
docs/
tools/
```

## Status

Latest synchronized design baseline: **v0.8**
