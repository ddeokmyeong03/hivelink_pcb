# HIVE LINK Core Rev.A — Placement Review v0.8

## Result

The full Rev.A BOM has been assigned a preliminary PCB coordinate, layer, and rotation.

- References placed: **183 / 183**
- Top + bottom assembly: **yes**
- Estimated same-side rectangular courtyard conflicts: **0**
- Estimated board-boundary violations: **0**
- Board: **100 × 70 mm, 4 layers**
- CM4 top-side keepout used in the pre-placement audit: **x 95.5–135.5 mm, y 58.5–113.5 mm**

These numbers come from a conservative geometry pre-check, not KiCad native courtyard DRC.

## Floorplan

### Top

- Left edge: RJ45 MagJack
- Upper edge: CAN1 / CAN2 / Pixhawk TELEM / Expansion
- Upper-left/center: CAN transceivers and Ethernet ESD lane
- Mid-left: STM32 controller and status UI
- Lower-left: 7–24 V input, eFuse, shunt, 5 V buck, 3.3 V rail
- Center-right: Raspberry Pi CM4
- Right edge: USB-A Host and USB-C Recovery
- Lower-right: Recovery/NORMAL service switch

### Bottom

Bottom assembly is used for low-speed configuration and service circuitry:

- eFuse programming resistors
- buck feedback/compensation network
- CM4 reset/translator control network
- CAN termination/power-selection jumpers
- TELEM voltage-sense/test network
- USB CC/service support
- secure-element/test points
- factory/debug test-point matrix under the CM4 footprint

Critical decoupling, Ethernet/USB ESD, switcher hot-loop parts, CAN PHYs, and clocks stay on Top.

## Important electrical routing corridors preserved

### Ethernet corridor

`RJ45 -> Ethernet ESD -> CM4`

A horizontal corridor around the y≈75 mm region is kept substantially free of the STM32/power switcher.

### Power island

`XT30 -> TVS -> reverse NFET -> TPS26632 -> shunt -> AP64501 -> L1 -> 5 V`

The complete switch-mode power region is kept to the lower-left, away from Ethernet and USB.

### USB corridor

CM4 USB2 exits the right side toward the USB mux and external USB connectors without crossing the power island.

## Hard gate

The v0.8 coordinates must be applied **after** `Update PCB from Schematic` using `apply_full_placement_v0.8.py`.
Native KiCad checks are still mandatory:

1. ERC
2. Update PCB from Schematic
3. apply v0.8 placement
4. Courtyard inspection
5. 3D inspection
6. DRC

No routing or Gerber release is authorized by this placement review alone.
