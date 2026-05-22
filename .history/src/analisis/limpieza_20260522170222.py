# Semana 12 - Momento 2
# Autor: Pedro Zamora (Líder Grupo 8)
# Descripción: Limpieza del dataset de notas consumido desde la API

import pandas as pd
import os

ruta_entrada = os.path.join("data", "raw", "notas.csv")
df = pd.read_csv(ruta_entrada)

print("=" * 50)
print("DETECCIÓN DE PROBLEMAS EN EL DATASET")
print("=" * 50)

print(f"\nForma del DataFrame: {df.shape[0]} filas x {df.shape[1]} columnas")
print("\nTipos de datos:")
print(df.dtypes)
print(f"\nDuplicados encontrados: {df.duplicated().sum()}")
print("\nValores nulos por columna:")
print(df.isnull().sum())

# 1. Eliminar duplicados
df = df.drop_duplicates(subset='id_nota')
print(f"\nDuplicados eliminados. Filas restantes: {len(df)}")

# 2. Convertir fecha a datetime
df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])
print(f"'fecha_registro' convertida a: {df['fecha_registro'].dtype}")

# 3. Detectar columna de nota y validar rango
if 'nota' in df.columns:
    antes = len(df)
    df = df[df['nota'].between(1.0, 5.0)]
    print(f"Registros con nota fuera de rango eliminados: {antes - len(df)}")
    df['nota'] = df['nota'].astype(float)

elif 'nota1' in df.columns:
    print("⚠️  Columnas nota1/2/3 detectadas — consolidando en columna 'nota'")
    df['nota'] = df[['nota1', 'nota2', 'nota3']].mean(axis=1).round(2)
    df = df.drop(columns=['nota1', 'nota2', 'nota3'])
    antes = len(df)
    df = df[df['nota'].between(1.0, 5.0)]
    print(f"Registros con nota fuera de rango eliminados: {antes - len(df)}")

# 4. Eliminar filas sin id_estudiante o id_materia
antes = len(df)
df = df.dropna(subset=['id_estudiante', 'id_materia'])
print(f"Filas sin estudiante o materia eliminadas: {antes - len(df)}")

# 5. Asegurar tipos correctos

ruta_salida = os.path.join("data", "processed", "datos_limpios.csv")
os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
df.to_csv(ruta_salida, index=False)

print("\n" + "=" * 50)
print(f"Archivo guardado en: {ruta_salida}")
print(f"Dataset final: {df.shape[0]} filas x {df.shape[1]} columnas")
print("Limpieza completada sin errores.")
print("=" * 50)