"""
Semana 12 - Momento 2
Autor: Mariana (Grupo 8)
Tarea : Transformaciones con groupby() y columnas calculadas
Archivo: src/analisis/03_transformacion_groupby.py
 
"""

import pandas as pd
import os
 
# ── CONFIGURACIÓN ──────────────────────────────────────────────────────────────
USAR_DATOS_LIMPIOS = False   # <-- cambia a True cuando Kevin suba datos_limpios.csv
 
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RAW  = os.path.join(ROOT, 'data', 'raw')
OUT  = os.path.join(ROOT, 'data', 'processed')
os.makedirs(OUT, exist_ok=True)
 
 
# ── 1. CARGAR DATOS ────────────────────────────────────────────────────────────
if USAR_DATOS_LIMPIOS:
    df = pd.read_csv(os.path.join(OUT, 'datos_limpios.csv'))
    print("✅ Cargado: data/processed/datos_limpios.csv")
else:
    # Leer las tres tablas
    estudiantes = pd.read_csv(os.path.join(RAW, 'estudiantes.csv'))
    materias    = pd.read_csv(os.path.join(RAW, 'materias.csv'))
    notas       = pd.read_csv(os.path.join(RAW, 'notas.csv'))
 
    # Eliminar duplicados intencionales (misma id_nota repetida)
    notas = notas.drop_duplicates(subset='id_nota')
 
    # Renombrar 'nombre' ANTES del merge para evitar nombre_x / nombre_y
    estudiantes = estudiantes.rename(columns={'nombre': 'nombre_estudiante'})
    materias    = materias.rename(columns={'nombre': 'nombre_materia'})
 
    # Unir las tres tablas
    df = (notas
          .merge(estudiantes[['id_estudiante', 'nombre_estudiante', 'apellido', 'grupo']],
                 on='id_estudiante', how='left')
          .merge(materias[['id_materia', 'nombre_materia', 'creditos']],
                 on='id_materia', how='left'))
 
    print("✅ Cargado desde data/raw/ (3 tablas unidas)")
 
print(f"   Filas    : {len(df)}")
print(f"   Columnas : {list(df.columns)}\n")
 
 
