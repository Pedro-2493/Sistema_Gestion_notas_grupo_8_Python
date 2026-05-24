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
def obtener_lollipop_materias(promedio_mat: pd.DataFrame) -> list[dict]:
    """
    Promedio por materia con indicador de aprobado.
    Usado por el lollipop de promedios por materia.
    """
    resumen = (
        promedio_mat[['nombre_materia', 'promedio']]
        .copy()
        .assign(
            promedio=lambda x: x['promedio'].round(2),
            aprobado=lambda x: x['promedio'] >= 3.0,
        )
        .sort_values('promedio', ascending=True)
        .reset_index(drop=True)
    )

    return resumen.to_dict(orient='records')





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