"""
HIVE LINK Rev.A v0.8 — Full placement application helper

Purpose
-------
Apply the reviewed placement coordinates for all schematic references AFTER
KiCad has performed "Update PCB from Schematic".

Required workflow
-----------------
1. Open HIVE_LINK_RevA.kicad_pro in KiCad.
2. Run schematic ERC and resolve issues.
3. In PCB Editor, run Tools -> Update PCB from Schematic (F8).
4. Save HIVE_LINK_RevA.kicad_pcb.
5. Run this script in a Python environment that can import KiCad's `pcbnew` module.
6. The script writes HIVE_LINK_RevA_Placed_v0.8.kicad_pcb, leaving the source PCB untouched.

This script places and flips footprints only. It does NOT route any tracks.
"""
from pathlib import Path
import csv

try:
    import pcbnew
except Exception as e:
    raise SystemExit(
        "pcbnew Python module is unavailable. Run this using KiCad's Python/scripting environment.\n"
        f"Import error: {e}"
    )

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SRC_BOARD = ROOT / "HIVE_LINK_RevA.kicad_pcb"
OUT_BOARD = ROOT / "HIVE_LINK_RevA_Placed_v0.8.kicad_pcb"
CSV_PATH = ROOT / "docs" / "HIVE_LINK_RevA_Full_Placement_v0.8.csv"

if not SRC_BOARD.exists():
    raise SystemExit(f"Missing source board: {SRC_BOARD}")
if not CSV_PATH.exists():
    raise SystemExit(f"Missing placement table: {CSV_PATH}")

board = pcbnew.LoadBoard(str(SRC_BOARD))

def mm(value):
    return pcbnew.FromMM(float(value))

def set_orientation(fp, degrees):
    d = float(degrees)
    try:
        fp.SetOrientationDegrees(d)
        return
    except Exception:
        pass
    try:
        fp.SetOrientation(pcbnew.EDA_ANGLE(d, pcbnew.DEGREES_T))
        return
    except Exception:
        pass
    fp.SetOrientation(int(round(d * 10)))

def is_back(fp):
    try:
        return fp.GetLayer() == pcbnew.B_Cu
    except Exception:
        return False

def set_side(fp, side):
    want_back = side.upper().startswith("B")
    if want_back != is_back(fp):
        fp.Flip(fp.GetPosition(), False)

LOCK_REFS = {
    "UCM1", "J1", "J2", "J3", "J4", "J6", "J7", "J8", "J9", "J10", "SW3"
}

rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8-sig", newline="")))
missing = []
placed = []
flipped = []
locked = []

for row in rows:
    ref = row["Reference"]
    fp = board.FindFootprintByReference(ref)
    if fp is None:
        missing.append(ref)
        continue

    pos = pcbnew.VECTOR2I(mm(row["X_mm"]), mm(row["Y_mm"]))
    fp.SetPosition(pos)
    before_back = is_back(fp)
    set_side(fp, row["Side"])
    if before_back != is_back(fp):
        flipped.append(ref)
    fp.SetPosition(pos)
    set_orientation(fp, row["Rotation_deg"])

    if ref in LOCK_REFS:
        try:
            fp.SetLocked(True)
            locked.append(ref)
        except Exception:
            pass
    placed.append(ref)

if missing:
    print("ERROR: references missing from PCB after schematic update:")
    print("  " + ", ".join(sorted(missing)))
    print("Run Update PCB from Schematic and ensure all footprints are present, then retry.")
    raise SystemExit(3)

pcbnew.SaveBoard(str(OUT_BOARD), board)

print(f"KiCad version: {getattr(pcbnew, 'GetBuildVersion', lambda: 'unknown')()}")
print(f"Placed: {len(placed)} / {len(rows)}")
print(f"Flipped to opposite side: {len(flipped)}")
print(f"Locked mechanical references: {len(locked)}")
print(f"Saved: {OUT_BOARD}")
print("Next: refill zones if any, inspect courtyards/3D, then route in the v0.7 routing order.")
