# Semana 12 - Momento 2
# Autor: Pedro Zamora (Grupo 8)
# Descripcion: Exporta los 4 dataframes analizados a JSON y los envia
#              a la API REST de Spring Boot para que React los consuma

import pandas as pd
import requests
import json
import os
import sys

API_BASE = "http://localhost:8080/api"
PROCESSED_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')


def leer_csv(nombre):
    ruta = f'{PROCESSED_DIR}/{nombre}'
    if not os.path.exists(ruta):
        print(f"  ! ADVERTENCIA: {ruta} no encontrado, se omite")
        return None
    df = pd.read_csv(ruta)
    df = df.where(pd.notna(df), None)
    return json.loads(df.to_json(orient='records', force_ascii=False))


def main():
    print("=" * 55)
    print("  EXPORTAR JSON — 4 DataFrames -> Spring Boot")
    print("=" * 55)

    payload = {
        "resumen_materias": leer_csv("resumen_por_materia.csv") or [],
        "rendimiento_periodo": leer_csv("rendimiento_periodo.csv") or [],
        "distribucion_notas": leer_csv("notas_limpios.csv") or [],
        "resumen_docentes": leer_csv("resumen_por_docente.csv") or [],
    }

    total = sum(len(v) for v in payload.values())
    print(f"\nTotal registros exportados: {total}")
    for key, val in payload.items():
        print(f"  {key}: {len(val)} registros")

    url = f"{API_BASE}/analytics"
    print(f"\nEnviando a {url} ...")
    try:
        resp = requests.post(url, json=payload, timeout=10)
        resp.raise_for_status()
        print(f"  [OK] Respuesta: HTTP {resp.status_code}")
    except requests.exceptions.ConnectionError:
        print(f"  ! ERROR: No se pudo conectar con {API_BASE}")
        print(f"    Asegurate de que el backend de Spring Boot este corriendo.")
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"  ! ERROR HTTP {e.response.status_code}: {e.response.text}")
        sys.exit(1)

    print("\n" + "=" * 55)
    print("  [OK] DATOS EXPORTADOS CORRECTAMENTE")
    print("=" * 55)


if __name__ == '__main__':
    main()
