# Semana 12 - Momento 2
# Autor: Grupo 8
# Descripción: Visualizaciones del análisis de notas

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np
import os

OUT = os.path.join("data", "processed")
RAW = os.path.join("data", "raw")

df           = pd.read_csv(os.path.join(OUT, 'datos_con_columnas.csv'))
promedio_mat = pd.read_csv(os.path.join(OUT, 'promedio_por_materia.csv'))
ranking      = pd.read_csv(os.path.join(OUT, 'ranking_estudiantes.csv'))

os.makedirs(OUT, exist_ok=True)

# Paleta vibrante
COLORES = ['#FF6B6B', '#FFD93D', '#6BCB77', '#4D96FF',
           '#C77DFF', '#FF9A3C', '#00C9A7', '#F72585']

# ── Gráfico 1: Violín — distribución de notas por materia ─────
fig, ax = plt.subplots(figsize=(13, 7))
fig.patch.set_facecolor('#0D0D0D')
ax.set_facecolor('#0D0D0D')

materias = df['nombre_materia'].dropna().unique()
datos_violin = [
    df[df['nombre_materia'] == m]['nota'].dropna().values
    for m in materias
]

partes = ax.violinplot(datos_violin, showmedians=True, showextrema=True)

for i, pc in enumerate(partes['bodies']):
    pc.set_facecolor(COLORES[i % len(COLORES)])
    pc.set_edgecolor('white')
    pc.set_alpha(0.85)

partes['cmedians'].set_color('white')
partes['cmedians'].set_linewidth(2)
partes['cbars'].set_color('white')
partes['cmaxes'].set_color('white')
partes['cmins'].set_color('white')

ax.set_xticks(range(1, len(materias) + 1))
ax.set_xticklabels(materias, rotation=30, ha='right',
                   color='white', fontsize=11)
ax.set_ylabel('Nota', color='white', fontsize=12)
ax.set_title('Distribución de Notas por Materia', color='white',
             fontsize=15, fontweight='bold', pad=20)
ax.tick_params(colors='white')
ax.spines[:].set_color('#333333')
ax.yaxis.grid(True, color='#333333', linestyle='--', alpha=0.5)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig(os.path.join(OUT, 'grafico_violin_notas.png'), dpi=150)
plt.show()
print("✅ Gráfico 1 guardado: grafico_violin_notas.png")


# ── Gráfico 2: Dispersión — nota vs id_estudiante por materia ──
fig, ax = plt.subplots(figsize=(13, 7))
fig.patch.set_facecolor('#0D0D0D')
ax.set_facecolor('#0D0D0D')

for i, materia in enumerate(materias):
    subset = df[df['nombre_materia'] == materia]
    ax.scatter(
        subset['id_estudiante'],
        subset['nota'],
        label=materia,
        color=COLORES[i % len(COLORES)],
        alpha=0.75,
        edgecolors='white',
        linewidths=0.4,
        s=80,
    )

# Línea de umbral de aprobación
ax.axhline(y=3.0, color='#FF6B6B', linestyle='--',
           linewidth=1.5, label='Umbral aprobación (3.0)')

ax.set_xlabel('ID Estudiante', color='white', fontsize=12)
ax.set_ylabel('Nota', color='white', fontsize=12)
ax.set_title('Dispersión de Notas por Estudiante y Materia',
             color='white', fontsize=15, fontweight='bold', pad=20)
ax.tick_params(colors='white')
ax.spines[:].set_color('#333333')
ax.yaxis.grid(True, color='#333333', linestyle='--', alpha=0.5)
ax.set_axisbelow(True)
ax.legend(facecolor='#1A1A1A', edgecolor='#444444',
          labelcolor='white', fontsize=9, loc='lower right')

plt.tight_layout()
plt.savefig(os.path.join(OUT, 'grafico_dispersion_notas.png'), dpi=150)
plt.show()
print("✅ Gráfico 2 guardado: grafico_dispersion_notas.png")


# ── Gráfico 3: Caja (boxplot) — nota por periodo ───────────────
fig, ax = plt.subplots(figsize=(10, 7))
fig.patch.set_facecolor('#0D0D0D')
ax.set_facecolor('#0D0D0D')

periodos = df['periodo'].dropna().unique()
datos_box = [df[df['periodo'] == p]['nota'].dropna().values for p in periodos]

bp = ax.boxplot(datos_box, patch_artist=True, notch=True,
                medianprops=dict(color='white', linewidth=2))

for i, patch in enumerate(bp['boxes']):
    patch.set_facecolor(COLORES[i % len(COLORES)])
    patch.set_alpha(0.85)

for element in ['whiskers', 'caps', 'fliers']:
    for item in bp[element]:
        item.set_color('white')
        item.set_alpha(0.6)

ax.set_xticks(range(1, len(periodos) + 1))
ax.set_xticklabels(periodos, color='white', fontsize=12)
ax.set_ylabel('Nota', color='white', fontsize=12)
ax.set_title('Distribución de Notas por Periodo Académico',
             color='white', fontsize=15, fontweight='bold', pad=20)
ax.tick_params(colors='white')
ax.spines[:].set_color('#333333')
ax.yaxis.grid(True, color='#333333', linestyle='--', alpha=0.5)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig(os.path.join(OUT, 'grafico_boxplot_periodos.png'), dpi=150)
plt.show()
print("✅ Gráfico 3 guardado: grafico_boxplot_periodos.png")