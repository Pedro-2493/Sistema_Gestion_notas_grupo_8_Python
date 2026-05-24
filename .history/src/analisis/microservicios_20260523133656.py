
import os
from fastapi import FastAPI
from src.analisis.grafico import obtener_aprobados_reprobados

@app.get("/api/graficos/headless/aprobados-por-materia")
def headless_ep_aprobados_por_materia():
    return obtener_aprobados_reprobados(df)