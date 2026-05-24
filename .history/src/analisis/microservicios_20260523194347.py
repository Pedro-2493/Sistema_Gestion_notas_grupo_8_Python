
import os
from fastapi import FastAPI

from .grafico import obtener_aprobados_reprobados, obtener_radar_materias

app = FastAPI(title="Analisis de Notas")

@app.get("/api/graficos/headless/aprobados-por-materia")
def headless_ep_aprobados_por_materia():
    return obtener_aprobados_reprobados()

@app.get("/api/graficos/headless/radar-materias")
def headless_ep_radar_materias():
    return obtener_radar_materias()

# ── Endpoints ────────────────────────────────────────────────

@app.get("/api/graficos/headless/nota-vs-presencias")
def headless_ep_nota_vs_presencias():
    return obtener_nota_vs_presencias()


@app.get("/api/graficos/headless/heatmap-notas")
def headless_ep_heatmap_notas():
    return obtener_heatmap_notas()


@app.get("/api/graficos/headless/asistencia-por-materia")
def headless_ep_asistencia_por_materia():
    return obtener_asistencia_por_materia()


@app.get("/api/graficos/headless/promedio-estudiantes")
def headless_ep_promedio_estudiantes():
    return obtener_promedio_estudiantes()