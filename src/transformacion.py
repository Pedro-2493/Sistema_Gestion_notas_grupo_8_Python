import pandas as pd

df_notas = pd.read_csv("data/processed/datos_limpios.csv")
print(df_notas.head())

print(df_notas.columns.tolist())

df_informacion_estudiante = df_notas[['id_nota', 'id_estudiante', 'id_materia', 'periodo', 'fecha_registro', 'observacion']]
print(df_informacion_estudiante.head())

df_entrega_de_calificaciones = df_notas[['id_nota', 'nota1', 'nota2', 'nota3']]
print(df_entrega_de_calificaciones.head())
