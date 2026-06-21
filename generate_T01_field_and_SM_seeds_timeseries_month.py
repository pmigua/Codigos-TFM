from __future__ import annotations

import subprocess
from pathlib import Path

# Put this script in the same folder as:
#   geopack-2008.for
#   t01_01.for
#   Test_T01_cartesian_time_v2.f90
#   Test_T01_SM_seeds_time.f90

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "T01_timeseries_month"
OUT.mkdir(exist_ok=True)

FIELD_EXE = ROOT / "Test_T01_cartesian_time_v2.exe"
SEEDS_EXE = ROOT / "Test_T01_SM_seeds_time.exe"

base_year = 1997
base_day = 1
base_hour = 0
base_minute = 0
base_second = 0

n_instants = 12
dt_days = 30

INSTANCES = []

for i in range(n_instants):
    day = base_day + i * dt_days

    INSTANCES.append(
        (float(i), base_year, day, base_hour, base_minute, base_second)
    )

def run(cmd: list[str]) -> None:
    print(" ".join(cmd))
    subprocess.run(cmd, check=True, cwd=ROOT)


def compile_programs() -> None:
    run([
        "gfortran",
        "geopack-2008.for",
        "t01_01.for",
        "Test_T01_cartesian_time_v2.f90",
        "-o",
        str(FIELD_EXE),
    ])
    run([
        "gfortran",
        "geopack-2008.for",
        "Test_T01_SM_seeds_time.f90",
        "-o",
        str(SEEDS_EXE),
    ])


def write_pvd(pvd_path: Path, files: list[tuple[float, Path]]) -> None:
    lines = [
        '<?xml version="1.0"?>',
        '<VTKFile type="Collection" version="0.1" byte_order="LittleEndian">',
        '  <Collection>',
    ]
    for t, f in files:
        rel = f.relative_to(pvd_path.parent).as_posix()
        lines.append(f'    <DataSet timestep="{t}" group="" part="0" file="{rel}"/>')
    lines += [
        '  </Collection>',
        '</VTKFile>',
        '',
    ]
    pvd_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    compile_programs()

    field_files: list[tuple[float, Path]] = []
    seed_files: list[tuple[float, Path]] = []

    for idx, (t, year, day, hour, minute, second) in enumerate(INSTANCES):
        field_file = OUT / f"T01_field_month_{idx:03d}.vtk"
        seed_file = OUT / f"T01_SM_seeds_month_{idx:03d}.vtk"

        common_args = [str(year), str(day), str(hour), str(minute), str(second)]

        run([str(FIELD_EXE), str(field_file), *common_args])
        run([str(SEEDS_EXE), str(seed_file), *common_args])

        field_files.append((t, field_file))
        seed_files.append((t, seed_file))

    write_pvd(OUT / "T01_field_timeseries_month.pvd", field_files)
    write_pvd(OUT / "T01_SM_seeds_timeseries_month.pvd", seed_files)

    print("\nGenerated:")
    print(OUT / "T01_field_timeseries_month.pvd")
    print(OUT / "T01_SM_seeds_timeseries_month.pvd")


if __name__ == "__main__":
    main()
