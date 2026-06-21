from pathlib import Path
import re
import vtk

# Ejecuta este script con pvpython dentro de la carpeta T01_timeseries:
#   "C:\Program Files\ParaView 5.xx.x\bin\pvpython.exe" convert_legacy_vtk_to_xml_pvd_auto.py
#
# Convierte TODOS los T01_field_XXX.vtk a .vts
# y TODOS los T01_SM_seeds_XXX.vtk a .vtp.
# Después crea los PVD XML con todos los instantes encontrados.

folder = Path.cwd()

def read_timesteps_from_pvd(pvd_name):
    """Devuelve diccionario {filename: timestep} leyendo el PVD legacy si existe."""
    pvd_path = folder / pvd_name
    timesteps = {}

    if not pvd_path.exists():
        return timesteps

    text = pvd_path.read_text(encoding="utf-8", errors="ignore")
    pattern = r'<DataSet\s+[^>]*timestep="([^"]+)"[^>]*file="([^"]+)"'
    for timestep, filename in re.findall(pattern, text):
        timesteps[Path(filename).name] = float(timestep)

    return timesteps

def collect_files(prefix):
    """Busca archivos tipo prefix_000.vtk, prefix_001.vtk, etc."""
    files = sorted(folder.glob(f"{prefix}_*.vtk"))
    if not files:
        raise FileNotFoundError(f"No se han encontrado archivos {prefix}_*.vtk en {folder}")
    return files

def write_pvd(pvd_name, xml_entries):
    """xml_entries = lista de tuplas (timestep, filename_xml)."""
    with open(folder / pvd_name, "w", encoding="utf-8", newline="\n") as f:
        f.write('<?xml version="1.0"?>\n')
        f.write('<VTKFile type="Collection" version="0.1" byte_order="LittleEndian">\n')
        f.write('  <Collection>\n')
        for timestep, name in xml_entries:
            f.write(f'    <DataSet timestep="{timestep}" group="" part="0" file="{name}"/>\n')
        f.write('  </Collection>\n')
        f.write('</VTKFile>\n')

def convert_field(vtk_path, vts_name):
    reader = vtk.vtkStructuredGridReader()
    reader.SetFileName(str(vtk_path))
    reader.Update()

    data = reader.GetOutput()
    if data is None or data.GetNumberOfPoints() == 0:
        raise RuntimeError(f"No se ha podido leer el campo: {vtk_path.name}")

    writer = vtk.vtkXMLStructuredGridWriter()
    writer.SetFileName(str(folder / vts_name))
    writer.SetInputData(data)
    writer.SetDataModeToAscii()
    writer.Write()

    print(f"Campo convertido: {vtk_path.name} -> {vts_name}")

def convert_seeds(vtk_path, vtp_name):
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(str(vtk_path))
    reader.Update()

    data = reader.GetOutput()
    if data is None or data.GetNumberOfPoints() == 0:
        raise RuntimeError(f"No se han podido leer las semillas: {vtk_path.name}")

    writer = vtk.vtkXMLPolyDataWriter()
    writer.SetFileName(str(folder / vtp_name))
    writer.SetInputData(data)
    writer.SetDataModeToAscii()
    writer.Write()

    print(f"Semillas convertidas: {vtk_path.name} -> {vtp_name}")

field_timesteps = read_timesteps_from_pvd("T01_field_timeseries_month.pvd")
seed_timesteps = read_timesteps_from_pvd("T01_SM_seeds_timeseries_month.pvd")

field_files = collect_files("T01_field")
seed_files = collect_files("T01_SM_seeds")

field_xml_entries = []
for i, vtk_path in enumerate(field_files):
    vts_name = vtk_path.with_suffix(".vts").name
    convert_field(vtk_path, vts_name)
    timestep = field_timesteps.get(vtk_path.name, float(i))
    field_xml_entries.append((timestep, vts_name))

seed_xml_entries = []
for i, vtk_path in enumerate(seed_files):
    vtp_name = vtk_path.with_suffix(".vtp").name
    convert_seeds(vtk_path, vtp_name)
    timestep = seed_timesteps.get(vtk_path.name, float(i))
    seed_xml_entries.append((timestep, vtp_name))

write_pvd("T01_field_timeseries_month_XML.pvd", field_xml_entries)
write_pvd("T01_SM_seeds_timeseries_month_XML.pvd", seed_xml_entries)

print("\nListo.")
print(f"Campos convertidos: {len(field_xml_entries)}")
print(f"Semillas convertidas: {len(seed_xml_entries)}")
print("Abre en ParaView:")
print("  T01_field_timeseries_month_XML.pvd")
print("  T01_SM_seeds_timeseries_month_XML.pvd")
