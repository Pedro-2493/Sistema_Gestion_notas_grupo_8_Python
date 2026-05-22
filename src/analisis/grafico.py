# Semana 12 - Momento 2
# Autor: Grupo 8
# Descripción: Visualizaciones del análisis de notas

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import os

OUT = os.path.join("data", "processed")
RAW = os.path.join("data", "raw")

df           = pd.read_csv(os.path.join(OUT, 'datos_con_columnas.csv'))
promedio_mat = pd.read_csv(os.path.join(OUT, 'promedio_por_materia.csv'))
ranking      = pd.read_csv(os.path.join(OUT, 'ranking_estudiantes.csv'))

os.makedirs(OUT, exist_ok=True)

COLORES = ['#FF6B6B', '#FFD93D', '#6BCB77', '#4D96FF',
           '#C77DFF', '#FF9A3C', '#00C9A7', '#F72585']

FONDO   = '#0D0D0D'
GRID    = '#2a2a2a'

# ── Gráfico 1: LOLLIPOP — promedio por materia ────────────────
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor(FONDO)
ax.set_facecolor(FONDO)

materias  = promedio_mat['nombre_materia']
promedios = promedio_mat['promedio']

for i, (mat, prom) in enumerate(zip(materias, promedios)):
    color = COLORES[i % len(COLORES)]
    ax.plot([0, prom], [i, i], color=color, linewidth=2.5, alpha=0.7)
    ax.scatter(prom, i, color=color, s=180, zorder=5, edgecolors='white', linewidths=0.8)
    ax.text(prom + 0.05, i, f'{prom:.2f}', va='center',
            color='white', fontsize=10, fontweight='bold')

ax.set_yticks(range(len(materias)))
ax.set_yticklabels(materias, color='white', fontsize=11)
ax.set_xlabel('Promedio', color='white', fontsize=12)
ax.set_title('Promedio de Calificaciones por Materia', color='white',
             fontsize=15, fontweight='bold', pad=20)
ax.set_xlim(0, 5.5)
ax.axvline(x=3.0, color='#FF6B6B', linestyle='--', linewidth=1.2, alpha=0.6, label='Umbral 3.0')
ax.tick_params(colors='white')
ax.spines[:].set_color(GRID)
ax.xaxis.grid(True, color=GRID, linestyle='--', alpha=0.5)
ax.set_axisbelow(True)
ax.legend(facecolor='#1A1A1A', edgecolor=GRID, labelcolor='white', fontsize=9)

plt.tight_layout()
plt.savefig(os.path.join(OUT, 'grafico_lollipop_materias.png'), dpi=150, facecolor=FONDO)
plt.show()
print("✅ Gráfico 1 guardado: grafico_lollipop_materias.png")


# ── Gráfico 2: BUMP CHART — ranking por periodo ───────────────
fig, ax = plt.subplots(figsize=(13, 8))
fig.patch.set_facecolor(FONDO)
ax.set_facecolor(FONDO)

periodos = sorted(df['periodo'].dropna().unique())
# Top 8 estudiantes por promedio general
top_estudiantes = (
    df.groupby('nombre_estudiante')['nota']
    .mean()
    .nlargest(8)
    .index.tolist()
)

for i, estudiante in enumerate(top_estudiantes):
    color = COLORES[i % len(COLORES)]
    rankings = []
    for periodo in periodos:
        df_periodo = df[df['periodo'] == periodo]
        rank_periodo = (
            df_periodo.groupby('nombre_estudiante')['nota']
            .mean()
            .rank(ascending=False, method='min')
        )
        pos = rank_periodo.get(estudiante, np.nan)
        rankings.append(pos)

    ax.plot(periodos, rankings, color=color, linewidth=2.5,
            marker='o', markersize=10, label=estudiante,
            markeredgecolor='white', markeredgewidth=0.8)

    # Etiqueta al inicio y al final
    if not np.isnan(rankings[0]):
        ax.text(-0.15, rankings[0], estudiante.split()[0],
                va='center', ha='right', color=color, fontsize=8, fontweight='bold')
    if not np.isnan(rankings[-1]):
        ax.text(len(periodos) - 0.85, rankings[-1], f'#{int(rankings[-1])}',
                va='center', ha='left', color=color, fontsize=9, fontweight='bold')

ax.invert_yaxis()
ax.set_xticks(range(len(periodos)))
ax.set_xticklabels(periodos, color='white', fontsize=12)
ax.set_ylabel('Posición en ranking', color='white', fontsize=12)
ax.set_title('Bump Chart — Evolución del Ranking por Periodo', color='white',
             fontsize=15, fontweight='bold', pad=20)
ax.tick_params(colors='white')
ax.spines[:].set_color(GRID)
ax.yaxis.grid(True, color=GRID, linestyle='--', alpha=0.4)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig(os.path.join(OUT, 'grafico_bump_ranking.png'), dpi=150, facecolor=FONDO)
plt.show()
print("✅ Gráfico 2 guardado: grafico_bump_ranking.png")


# ── Gráfico 3: RADAR — perfil académico por materia ──────────
materias_radar = promedio_mat['nombre_materia'].tolist()
valores        = promedio_mat['promedio'].tolist()
N              = len(materias_radar)

angulos = [n / float(N) * 2 * np.pi for n in range(N)]
angulos += angulos[:1]
valores += valores[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))
fig.patch.set_facecolor(FONDO)
ax.set_facecolor(FONDO)

ax.plot(angulos, valores, color='#4D96FF', linewidth=2.5)
ax.fill(angulos, valores, color='#4D96FF', alpha=0.25)

# Línea de umbral 3.0
umbral = [3.0] * (N + 1)
ax.plot(angulos, umbral, color='#FF6B6B', linewidth=1.5,
        linestyle='--', label='Umbral 3.0')

ax.set_xticks(angulos[:-1])
ax.set_xticklabels(materias_radar, color='white', fontsize=10)
ax.set_ylim(0, 5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(['1', '2', '3', '4', '5'], color='#888888', fontsize=8)
ax.grid(color=GRID, linewidth=0.8)
ax.spines['polar'].set_color(GRID)
ax.set_title('Radar — Perfil Académico por Materia', color='white',
             fontsize=15, fontweight='bold', pad=30)
ax.legend(facecolor='#1A1A1A', edgecolor=GRID, labelcolor='white',
          fontsize=9, loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.savefig(os.path.join(OUT, 'grafico_radar_materias.png'), dpi=150, facecolor=FONDO)
plt.show()
print("✅ Gráfico 3 guardado: grafico_radar_materias.png")


# ── Gráfico 4: POPULATION PYRAMID — aprobados vs reprobados ──
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor(FONDO)
ax.set_facecolor(FONDO)

resumen = (
    df.groupby('nombre_materia')['aprobado']
    .agg(aprobados='sum', total='count')
    .assign(reprobados=lambda x: x['total'] - x['aprobados'])
    .reset_index()
    .sort_values('aprobados', ascending=True)
)

y = range(len(resumen))

ax.barh(list(y), -resumen['reprobados'], color='#FF6B6B',
        label='Reprobados', height=0.6, edgecolor=FONDO, linewidth=0.5)
ax.barh(list(y), resumen['aprobados'], color='#6BCB77',
        label='Aprobados', height=0.6, edgecolor=FONDO, linewidth=0.5)

# Etiquetas valores
for i, (apr, rep) in enumerate(zip(resumen['aprobados'], resumen['reprobados'])):
    ax.text(apr + 0.1, i, str(int(apr)), va='center', color='#6BCB77',
            fontsize=10, fontweight='bold')
    ax.text(-rep - 0.1, i, str(int(rep)), va='center', ha='right',
            color='#FF6B6B', fontsize=10, fontweight='bold')

ax.set_yticks(list(y))
ax.set_yticklabels(resumen['nombre_materia'], color='white', fontsize=11)
ax.axvline(x=0, color='white', linewidth=1.2)
ax.set_xlabel('← Reprobados   |   Aprobados →', color='white', fontsize=11)
ax.set_title('Pirámide — Aprobados vs Reprobados por Materia',
             color='white', fontsize=15, fontweight='bold', pad=20)
ax.tick_params(colors='white')
ax.spines[:].set_color(GRID)
ax.xaxis.grid(True, color=GRID, linestyle='--', alpha=0.4)
ax.set_axisbelow(True)
ax.legend(facecolor='#1A1A1A', edgecolor=GRID, labelcolor='white', fontsize=10)

# Ocultar valores negativos en el eje X
xticks = ax.get_xticks()
ax.set_xticklabels([str(abs(int(x))) for x in xticks], color='white')

plt.tight_layout()
plt.savefig(os.path.join(OUT, 'grafico_piramide_aprobados.png'), dpi=150, facecolor=FONDO)
plt.show()
print("✅ Gráfico 4 guardado: grafico_piramide_aprobados.png")

print("\n✅ Todos los gráficos guardados en data/processed/")