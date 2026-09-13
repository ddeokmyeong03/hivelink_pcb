# HIVE LINK Rev.A — TL3301 footprint patch v0.11

This patch resolves the remaining SW1/SW2 footprint warnings without replacing the ERC-clean schematic currently being edited in KiCad.

## Footprint

`HIVE_LINK:E-Switch_TL3301_GullWing`

Manufacturer basis: E-Switch TL3301NF160QG drawing P010515 Rev F.

Recommended PCB layout used in the footprint:

- body: 6.00 x 6.00 mm
- four SMD pads
- pad size: 2.10 x 1.40 mm
- inner horizontal pad-edge gap: 7.00 mm
- overall horizontal pad-edge span: 11.20 mm
- vertical row center spacing: 4.50 mm

The physical switch has four terminals, but terminals 1+2 are internally common and terminals 3+4 are internally common. Therefore the 2-pin schematic symbol is mapped using duplicated pad numbers: two pad-1s and two pad-2s.

## Apply

1. Ensure `HIVE_LINK.pretty/E-Switch_TL3301_GullWing.kicad_mod` exists in the project.
2. In Assign Footprints select SW1 and assign `HIVE_LINK:E-Switch_TL3301_GullWing`.
3. Assign the same footprint to SW2.
4. Apply/save.
5. Re-run ERC. With U2 assigned to `Package_SO:TSSOP-10_3x3mm_P0.5mm`, expected ERC result is 0 errors / 0 warnings.
