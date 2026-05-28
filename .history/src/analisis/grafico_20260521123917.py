# Semana 12 - Momento 2
# Autor: Grupo 8
# Descripción: Visualizaciones del análisis de notas

import matplotlib.pyplot as plt
import pandas as pd
import os

OUT = os.path.join("data", "processed")
RAW = os.path.join("data", "raw")

df          = pd.read_csv(os.path.join(OUT, 'datos_con_columnas.csv'))
promedio_mat = pd.read_csv(os.path.join(OUT, 'promedio_por_materia.csv'))
ranking      = pd.read_csv(os.path.join(OUT, 'ranking_estudiantes.csv'))

os.makedirs(OUT, exist_ok=True)

# ── Gráfico 1: Promedio por materia ───────────────────────────
plt.figure(figsize=(10, 6))
plt.bar(promedio_mat['nombre_materia'], promedio_mat['promedio'], color='steelblue')
plt.title('Promedio de Calificaciones por Materia', fontsize=14)
plt.xlabel('Materia')
plt.ylabel('Promedio')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(OUT, 'grafico_promedio_materias.png'))
plt.show()
print("✅ Gráfico 1 guardado: grafico_promedio_materias.png")

# ── Gráfico 2: Distribución de rendimiento ────────────────────
conteo = df['rendimiento'].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(conteo, labels=conteo.index, autopct='%1.1f%%',
        colors=['#2ecc71', '#3498db', '#f39c12', '#e74c3c'])
plt.title('Distribución de Rendimiento Académico', fontsize=14)
plt.tight_layout()
plt.savefig(os.path.join(OUT, 'grafico_rendimiento.png'))
plt.show()
print("✅ Gráfico 2 guardado: grafico_rendimiento.png")

# ── Gráfico 3: Top 10 estudiantes ────────────────────────────
top10 = ranking.head(10)
plt.figure(figsize=(10, 6))
plt.barh(top10['nombre_estudiante'], top10['promedio_general'], color='teal')
plt.title('Top 10 Estudiantes por Promedio General', fontsize=14)
plt.xlabel('Promedio')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(os.path.join(OUT, 'grafico_top10_estudiantes.png'))
plt.show()
print("✅ Gráfico 3 guardado: grafico_top10_estudiantes.png")