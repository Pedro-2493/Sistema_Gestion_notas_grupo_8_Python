# Semana 12 - Momento 3
# Autor: Grupo 8
# Descripción: Gráficos basados en datos transformados (merge + join)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

OUT   = os.path.join("data", "processed")
FONDO = '#0D0D0D'
GRID  = '#2a2a2a'
COLORES = ['#FF6B6B', '#FFD93D', '#6BCB77', '#4D96FF',
           '#C77DFF', '#FF9A3C', '#00C9A7', '#F72585']

# Cargar datasets
df_completo      = pd.read_csv(os.path.join(OUT, 'datos_transformados.csv'))
df_con_asistencia = pd.read_csv(os.path.join(OUT, 'notas_con_asistencia.csv'))


# ── Gráfico 1: SCATTER — nota vs presencias ───────────────────
def grafico_nota_vs_presencias():
    fig, ax = plt.subplots(figsize=(11, 7))
    fig.patch.set_facecolor(FONDO)
    ax.set_facecolor(FONDO)

    materias = df_con_asistencia['id_materia'].unique()
    for i, mat in enumerate(materias):
        sub = df_con_asistencia[df_con_asistencia['id_materia'] == mat]
        ax.scatter(sub['presencias'], sub['nota'],
                   color=COLORES[i % len(COLORES)],
                   label=f'Materia {int(mat)}',
                   s=100, alpha=0.8,
                   edgecolors='white', linewidths=0.4)

    ax.axhline(y=3.0, color='#FF6B6B', linestyle='--',
               linewidth=1.5, label='Umbral 3.0')
    ax.set_xlabel('Presencias', color='white', fontsize=12)
    ax.set_ylabel('Nota', color='white', fontsize=12)
    ax.set_title('Relación entre Presencias y Nota por Materia',
                 color='white', fontsize=15, fontweight='bold', pad=20)
    ax.tick_params(colors='white')
    ax.spines[:].set_color(GRID)
    ax.grid(color=GRID, linestyle='--', alpha=0.4)
    ax.set_axisbelow(True)
    ax.legend(facecolor='#1A1A1A', edgecolor=GRID,
              labelcolor='white', fontsize=9)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, 'grafico2_nota_vs_presencias.png'),
                dpi=150, facecolor=FONDO)
    plt.show()
    print("✅ Gráfico 1 guardado: grafico2_nota_vs_presencias.png")


# ── Gráfico 2: HEATMAP — promedio por estudiante y materia ────
def grafico_heatmap_notas():
    pivot = df_completo.pivot_table(
        index='nombre_estudiante',
        columns='nombre_materia',
        values='nota',
        aggfunc='mean'
    ).round(2)

    fig, ax = plt.subplots(figsize=(13, 8))
    fig.patch.set_facecolor(FONDO)
    ax.set_facecolor(FONDO)

    im = ax.imshow(pivot.values, cmap='RdYlGn', aspect='auto',
                   vmin=1.0, vmax=5.0)

    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels(pivot.columns, rotation=35, ha='right',
                       color='white', fontsize=10)
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index, color='white', fontsize=10)

    # Valores dentro de cada celda
    for i in range(len(pivot.index)):
        for j in range(len(pivot.columns)):
            val = pivot.values[i, j]
            if not np.isnan(val):
                ax.text(j, i, f'{val:.1f}', ha='center', va='center',
                        color='black', fontsize=9, fontweight='bold')

    cbar = plt.colorbar(im, ax=ax)
    cbar.ax.yaxis.set_tick_params(color='white')
    cbar.ax.set_ylabel('Nota', color='white', fontsize=10)
    plt.setp(cbar.ax.yaxis.get_ticklabels(), color='white')

    ax.set_title('Heatmap — Notas por Estudiante y Materia',
                 color='white', fontsize=15, fontweight='bold', pad=20)
    ax.spines[:].set_color(GRID)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, 'grafico2_heatmap_notas.png'),
                dpi=150, facecolor=FONDO)
    plt.show()
    print("✅ Gráfico 2 guardado: grafico2_heatmap_notas.png")


# ── Gráfico 3: STACKED BAR — asistencia por materia ──────────
def grafico_asistencia_por_materia():
    resumen = (
        df_con_asistencia
        .groupby('id_materia')[['presencias', 'ausencias', 'tardanzas']]
        .sum()
        .reset_index()
    )
    # Unir nombre de materia
    nombres = df_completo[['id_materia', 'nombre_materia']].drop_duplicates()
    resumen = resumen.merge(nombres, on='id_materia', how='left')

    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor(FONDO)
    ax.set_facecolor(FONDO)

    x = range(len(resumen))
    ax.bar(x, resumen['presencias'], label='Presencias',
           color='#6BCB77', edgecolor=FONDO)
    ax.bar(x, resumen['tardanzas'], bottom=resumen['presencias'],
           label='Tardanzas', color='#FFD93D', edgecolor=FONDO)
    ax.bar(x, resumen['ausencias'],
           bottom=resumen['presencias'] + resumen['tardanzas'],
           label='Ausencias', color='#FF6B6B', edgecolor=FONDO)

    ax.set_xticks(list(x))
    ax.set_xticklabels(resumen['nombre_materia'], rotation=30,
                       ha='right', color='white', fontsize=11)
    ax.set_ylabel('Total registros', color='white', fontsize=12)
    ax.set_title('Asistencia por Materia (Presencias / Tardanzas / Ausencias)',
                 color='white', fontsize=14, fontweight='bold', pad=20)
    ax.tick_params(colors='white')
    ax.spines[:].set_color(GRID)
    ax.yaxis.grid(True, color=GRID, linestyle='--', alpha=0.4)
    ax.set_axisbelow(True)
    ax.legend(facecolor='#1A1A1A', edgecolor=GRID,
              labelcolor='white', fontsize=10)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, 'grafico2_asistencia_materias.png'),
                dpi=150, facecolor=FONDO)
    plt.show()
    print("✅ Gráfico 3 guardado: grafico2_asistencia_materias.png")


# ── Gráfico 4: LOLLIPOP — promedio por estudiante ─────────────
def grafico_promedio_estudiantes():
    promedio = (
        df_completo
        .groupby('nombre_estudiante')['nota']
        .mean()
        .round(2)
        .sort_values(ascending=True)
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(11, 8))
    fig.patch.set_facecolor(FONDO)
    ax.set_facecolor(FONDO)

    for i, row in promedio.iterrows():
        color = '#6BCB77' if row['nota'] >= 3.0 else '#FF6B6B'
        ax.plot([0, row['nota']], [i, i], color=color,
                linewidth=2.2, alpha=0.7)
        ax.scatter(row['nota'], i, color=color, s=160,
                   zorder=5, edgecolors='white', linewidths=0.7)
        ax.text(row['nota'] + 0.05, i, f"{row['nota']:.2f}",
                va='center', color='white', fontsize=9, fontweight='bold')

    ax.set_yticks(range(len(promedio)))
    ax.set_yticklabels(promedio['nombre_estudiante'],
                       color='white', fontsize=10)
    ax.axvline(x=3.0, color='#FF6B6B', linestyle='--',
               linewidth=1.2, alpha=0.7, label='Umbral 3.0')
    ax.set_xlim(0, 5.5)
    ax.set_xlabel('Promedio', color='white', fontsize=12)
    ax.set_title('Promedio General por Estudiante',
                 color='white', fontsize=15, fontweight='bold', pad=20)
    ax.tick_params(colors='white')
    ax.spines[:].set_color(GRID)
    ax.xaxis.grid(True, color=GRID, linestyle='--', alpha=0.4)
    ax.set_axisbelow(True)
    ax.legend(facecolor='#1A1A1A', edgecolor=GRID,
              labelcolor='white', fontsize=9)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, 'grafico2_promedio_estudiantes.png'),
                dpi=150, facecolor=FONDO)
    plt.show()
    print("✅ Gráfico 4 guardado: grafico2_promedio_estudiantes.png")


# ── MAIN ──────────────────────────────────────────────────────
if __name__ == '__main__':
    grafico_nota_vs_presencias()
    grafico_heatmap_notas()
    grafico_asistencia_por_materia()
    grafico_promedio_estudiantes()
    print("\n✅ Todos los gráficos de transformación guardados en data/processed/")