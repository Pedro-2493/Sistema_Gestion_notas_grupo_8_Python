
import os
from fastapi import FastAPI

fro

app = FastAPI(title="Analisis de Notas")

@app.get("/api/graficos/headless/aprobados-por-materia")
def headless_ep_aprobados_por_materia():
    return obtener_aprobados_reprobados()

@app.get("/api/graficos/headless/radar-materias")
def headless_ep_radar_materias():
    return obtener_radar_materias()