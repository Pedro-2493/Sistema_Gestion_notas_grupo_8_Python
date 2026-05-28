import pandas as pd
import os

ruta_entrada = os.path.join("data", "raw", "notas.csv")
df = pd.read_csv(ruta_entrada)

print("=" * 50)
print("DETECCION DE PROBLEMAS EN EL DATASET")
print("=" * 50)

print(f"\nForma del DataFrame: {df.shape[0]} filas x {df.shape[1]} columnas")
print("\nTipos de datos:")
print(df.dtypes)
print(f"\nDuplicados encontrados: {df.duplicated().sum()}")
print("\nValores nulos por columna:")
print(df.isnull().sum())

df = df.drop_duplicates()
print(f"\nDuplicados eliminados. Filas restantes: {len(df)}")

df["observacion"] = df["observacion"].fillna("Sin observacion")
print(f"Nulos en 'observacion' rellenados: {df['observacion'].isnull().sum()} nulos restantes")

df["fecha_registro"] = pd.to_datetime(df["fecha_registro"])
print(f"'fecha_registro' convertida a: {df['fecha_registro'].dtype}")

ruta_salida = os.path.join("data", "processed", "datos_limpios.csv")
os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
df.to_csv(ruta_salida, index=False)

print("\n" + "=" * 50)
print(f"Archivo guardado en: {ruta_salida}")
print(f"Dataset final: {df.shape[0]} filas x {df.shape[1]} columnas")
print("Limpieza completada sin errores.")
print("=" * 50)
