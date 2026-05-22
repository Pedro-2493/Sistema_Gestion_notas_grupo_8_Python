"""
Semana 12 - Momento 2
Autor: Mariana (Grupo 8)
Tarea : Transformaciones con groupby() y columnas calculadas
Archivo: src/analisis/03_transformacion_groupby.py
 
"""
import pandas as pd
import os
 
# ── CONFIGURACIÓN ──────────────────────────────────────────────────────────────
USAR_DATOS_LIMPIOS = False   # ← False: usa datos_limpios.csv + estudiantes/materias del raw
 
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RAW  = os.path.join(ROOT, 'data', 'raw')
OUT  = os.path.join(ROOT, 'data', 'processed')
os.makedirs(OUT, exist_ok=True)
 
 
# ── 1. CARGAR DATOS ────────────────────────────────────────────────────────────
if USAR_DATOS_LIMPIOS:
    df = pd.read_csv(os.path.join(OUT, 'datos_limpios.csv'))
else:
    estudiantes = pd.read_csv(os.path.join(RAW, 'estudiantes.csv'))
    materias    = pd.read_csv(os.path.join(RAW, 'materias.csv'))
    
    # ← AQUÍ está el cambio clave: leer datos_limpios en vez de notas.csv
    notas = pd.read_csv(os.path.join(OUT, 'datos_limpios.csv'))

    notas = notas.drop_duplicates(subset='id_nota')

    estudiantes = estudiantes.rename(columns={'nombre': 'nombre_estudiante'})
    materias    = materias.rename(columns={'nombre': 'nombre_materia'})

    df = (notas
          .merge(estudiantes[['id_estudiante', 'nombre_estudiante', 'apellido', 'grupo']],
                 on='id_estudiante', how='left')
          .merge(materias[['id_materia', 'nombre_materia', 'creditos']],
                 on='id_materia', how='left'))
 
    print("✅ Cargado desde data/raw/ (3 tablas unidas)")
 
print(f"   Filas    : {len(df)}")
print(f"   Columnas : {list(df.columns)}\n")
 
 
# ── 2. COLUMNAS CALCULADAS ─────────────────────────────────────────────────────
 
# 2a. Promedio ponderado  (nota1 30% | nota2 30% | nota3 40%)
df['promedio_ponderado'] = (
    df['nota1'] * 0.30 +
    df['nota2'] * 0.30 +
    df['nota3'] * 0.40
).round(2)
 
# 2b. Nota final (promedio simple)
df['nota_final'] = df[['nota1', 'nota2', 'nota3']].mean(axis=1).round(2)
 
# 2c. Aprobado (umbral colombiano: 3.0)
df['aprobado'] = df['nota_final'] >= 3.0
 
# 2d. Clasificación de rendimiento
def clasificar_rendimiento(nota):
    if nota >= 4.5:
        return 'Sobresaliente'
    elif nota >= 4.0:
        return 'Excelente'
    elif nota >= 3.0:
        return 'Aprobado'
    else:
        return 'Reprobado'
 
df['rendimiento'] = df['nota_final'].apply(clasificar_rendimiento)
 
print("─" * 60)
print("COLUMNAS CALCULADAS — primeras 5 filas")
print("─" * 60)
cols_muestra = ['nombre_estudiante', 'nombre_materia', 'nota1', 'nota2',
                'nota3', 'promedio_ponderado', 'nota_final',
                'aprobado', 'rendimiento']
print(df[cols_muestra].head().to_string(index=False))
print()
 
 
 
 # ── 3. AGRUPACIONES (groupby) ──────────────────────────────────────────────────
 
# 3a. Promedio de nota_final por materia
promedio_por_materia = (
    df.groupby('nombre_materia')['nota_final']
    .agg(promedio='mean', minimo='min', maximo='max', total_registros='count')
    .round(2)
    .reset_index()
    .sort_values('promedio', ascending=False)
)
 
print("─" * 60)
print("PROMEDIO POR MATERIA")
print("─" * 60)
print(promedio_por_materia.to_string(index=False))
print()
 
# 3c. Tasa de aprobación por materia y periodo
aprobacion_materia_periodo = (
    df.groupby(['nombre_materia', 'periodo'])['aprobado']
    .agg(total='count', aprobados='sum')
    .assign(tasa_aprobacion=lambda x: (x['aprobados'] / x['total'] * 100).round(1))
    .reset_index()
    .sort_values(['nombre_materia', 'periodo'])
)
 
print("─" * 60)
print("TASA DE APROBACIÓN POR MATERIA Y PERIODO (%)")
print("─" * 60)
print(aprobacion_materia_periodo.to_string(index=False))
print()
 

# 3e. Ranking de estudiantes por promedio general
ranking_estudiantes = (
    df.groupby(['id_estudiante', 'nombre_estudiante', 'apellido'])['nota_final']
    .mean()
    .round(2)
    .reset_index()
    .rename(columns={'nota_final': 'promedio_general'})
    .sort_values('promedio_general', ascending=False)
    .reset_index(drop=True)
)
ranking_estudiantes.index += 1
ranking_estudiantes.index.name = 'puesto'
 
print("─" * 60)
print("TOP 10 ESTUDIANTES POR PROMEDIO GENERAL")
print("─" * 60)
print(ranking_estudiantes.head(10).to_string())
print()
 
# ── 4. GUARDAR RESULTADOS ──────────────────────────────────────────────────────
df.to_csv(os.path.join(OUT, 'datos_con_columnas.csv'), index=False)
promedio_por_materia.to_csv(os.path.join(OUT, 'promedio_por_materia.csv'), index=False)
aprobacion_materia_periodo.to_csv(os.path.join(OUT, 'aprobacion_materia_periodo.csv'), index=False)
ranking_estudiantes.to_csv(os.path.join(OUT, 'ranking_estudiantes.csv'))

print("✅ Archivos guardados en data/processed/")
print("   • datos_con_columnas.csv")
print("   • promedio_por_materia.csv")
print("   • aprobacion_materia_periodo.csv")
print("   • ranking_estudiantes.csv")