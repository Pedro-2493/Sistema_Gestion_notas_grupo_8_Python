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

# 2. Convertir fecha_registro a datetime
df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])
print(f"'fecha_registro' convertida a: {df['fecha_registro'].dtype}")

# 3. Validar rango de notas (1.0 - 5.0 escala colombiana)
antes = len(df)
df = df[df['nota'].between(1.0, 5.0)]
print(f"Registros con nota fuera de rango eliminados: {antes - len(df)}")

# 4. Eliminar filas sin id_estudiante o id_materia
df = df.dropna(subset=['id_estudiante', 'id_materia'])
print(f"Filas sin estudiante o materia eliminadas. Restantes: {len(df)}")

# 5. Asegurar tipos correctos
df['id_nota']       = df['id_nota'].astype(int)
df['id_estudiante'] = df['id_estudiante'].astype(int)
df['id_materia']    = df['id_materia'].astype(int)
df['nota']          = df['nota'].astype(float)

ruta_salida = os.path.join("data", "processed", "datos_limpios.csv")
os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
df.to_csv(ruta_salida, index=False)

print("\n" + "=" * 50)
print(f"Archivo guardado en: {ruta_salida}")
print(f"Dataset final: {df.shape[0]} filas x {df.shape[1]} columnas")
print("Limpieza completada sin errores.")
print("=" * 50)