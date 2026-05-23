# Semana 12 - Momento 2
# Autor: Kevin Vélez / Didier Achury (Grupo 8)
# Descripción: Transformaciones con merge() y join()

import pandas as pd
import os

ruta_notas       = os.path.join("data", "processed", "datos_limpios.csv")
ruta_estudiantes = os.path.join("data", "raw", "estudiantes.csv")
ruta_materias    = os.path.join("data", "raw", "materias.csv")
ruta_asistencias = os.path.join("data", "raw", "asistencias.csv")

df_notas       = pd.read_csv(ruta_notas)
df_estudiantes = pd.read_csv(ruta_estudiantes)
df_materias    = pd.read_csv(ruta_materias)
df_asistencias = pd.read_csv(ruta_asistencias)

print("=" * 55)
print("TRANSFORMACIONES — merge() y join()")
print("=" * 55)

# ── 1. MERGE: notas + estudiantes ─────────────────────────────
# nombre_estudiante ya viene en notas desde la API
# solo agregamos email y documento que no están en notas
df_con_estudiante = pd.merge(
    df_notas,
    df_estudiantes[['id_estudiante', 'email', 'documento']],
    on='id_estudiante',
    how='left'
)
print(f"\n1. Notas + Estudiantes: {len(df_con_estudiante)} filas")
print(df_con_estudiante[['id_nota', 'nombre_estudiante', 'nombre_materia', 'nota', 'periodo']].head())

# ── 2. MERGE: resultado anterior + materias ────────────────────
# nombre_materia ya viene en notas desde la API
# solo agregamos descripcion que no está en notas
df_completo = pd.merge(
    df_con_estudiante,
    df_materias[['id_materia', 'descripcion']],
    on='id_materia',
    how='left'
)
print(f"\n2. + Materias: {len(df_completo)} filas")
print(df_completo[['nombre_estudiante', 'nombre_materia', 'descripcion', 'nota']].head())

# ── 3. JOIN: notas con asistencias por estudiante y materia ───
df_notas_idx       = df_notas.set_index(['id_estudiante', 'id_materia'])
df_asistencias_idx = df_asistencias.set_index(['id_estudiante', 'id_materia'])

resumen_asistencia = (
    df_asistencias_idx
    .groupby(['id_estudiante', 'id_materia'])['estado']
    .value_counts()
    .unstack(fill_value=0)
    .rename(columns={
        'PRESENTE':  'presencias',
        'AUSENTE':   'ausencias',
        'TARDANZA':  'tardanzas',
    })
)

df_join = df_notas_idx.join(resumen_asistencia, how='left').reset_index()
df_join[['presencias', 'ausencias', 'tardanzas']] = \
    df_join[['presencias', 'ausencias', 'tardanzas']].fillna(0).astype(int)

print(f"\n3. Notas + Asistencias (join): {len(df_join)} filas")
print(df_join[['id_estudiante', 'id_materia', 'nota', 'presencias', 'ausencias', 'tardanzas']].head())

# ── 4. GUARDAR ─────────────────────────────────────────────────
ruta_salida = os.path.join("data", "processed", "datos_transformados.csv")
df_completo.to_csv(ruta_salida, index=False)

ruta_join = os.path.join("data", "processed", "notas_con_asistencia.csv")
df_join.to_csv(ruta_join, index=False)

print("\n✅ Archivos guardados en data/processed/")
print("   • datos_transformados.csv")
print("   • notas_con_asistencia.csv")