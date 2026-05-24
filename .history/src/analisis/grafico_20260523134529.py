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





# ── Gráfico 2: RADAR — perfil académico por materia ──────────
def obtener_radar_materias(promedio_mat: pd.DataFrame) -> list[dict]:
    """
    Retorna los datos del radar por materia.
    Incluye nombre, promedio y ángulo para renderizar en frontend.
    """
    materias = promedio_mat['nombre_materia'].tolist()
    promedios = promedio_mat['promedio'].tolist()
    N = len(materias)

    angulos = [round(n / float(N) * 360, 2) for n in range(N)]

    resultado = [
        {
            'nombre_materia': mat,
            'promedio':       round(prom, 2),
            'angulo_grados':  ang,
            'aprobado':       prom >= 3.0,
        }
        for mat, prom, ang in zip(materias, promedios, angulos)
    ]
    return resultado.to_dict(orient='records')


# ── Gráfico 3: POPULATION PYRAMID — aprobados vs reprobados ──
def obtener_aprobados_reprobados(df: pd.DataFrame) -> list[dict]:
    """
    Calcula aprobados y reprobados por materia.
    Retorna lista de dicts lista para JSON o DataFrame.
    """
    resumen = (
        df.groupby('nombre_materia')['aprobado']
        .agg(aprobados='sum', total='count')
        .assign(reprobados=lambda x: x['total'] - x['aprobados'])
        .reset_index()
        .sort_values('aprobados', ascending=True)
    )

    return resumen.to_dict(orient='records')