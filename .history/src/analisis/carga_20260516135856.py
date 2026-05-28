# Semana 12 - Momento 2
# Autor: Pedro Zamora (Líder Grupo 8)
# Descripción: Consume la API del Sistema de Gestión de Notas y genera el dataset

import pandas as pd
import requests
import random
import os

BASE_URL = 'http://localhost:8080'

# ─────────────────────────────────────────────
# FUNCIONES DE CONSUMO DE API
# ─────────────────────────────────────────────

def obtener_estudiantes():
    """Consume GET /api/students y retorna un DataFrame."""
    response = requests.get(f'{BASE_URL}/api/students')

    if response.status_code == 200:
        datos = response.json()
        print(f"✅ /api/students  → {len(datos)} registros")

        df = pd.DataFrame(datos)

        # Renombramos campos para mantener consistencia con el resto del pipeline
        df = df.rename(columns={
            'id':          'id_estudiante',
            'studentName': 'nombre',
            'email':       'email',
            'document':    'documento',
        })
        return df

    else:
        print(f"❌ /api/students falló con código {response.status_code}")
        return pd.DataFrame()


def obtener_materias():
    """Consume GET /api/subjects y retorna un DataFrame."""
    response = requests.get(f'{BASE_URL}/api/subjects')

    if response.status_code == 200:
        datos = response.json()
        print(f"✅ /api/subjects  → {len(datos)} registros")

        df = pd.DataFrame(datos)

        df = df.rename(columns={
            'id':          'id_materia',
            'subjectName': 'nombre',
            'description': 'descripcion',
        })
        return df

    else:
        print(f"❌ /api/subjects falló con código {response.status_code}")
        return pd.DataFrame()


def obtener_notas():
    """
    Consume GET /api/grades y retorna un DataFrame.
    Grade tiene objetos anidados: student, subject, teacher → los aplanamos.
    """
    response = requests.get(f'{BASE_URL}/api/grades')

    if response.status_code == 200:
        datos = response.json()
        print(f"✅ /api/grades    → {len(datos)} registros")

        filas = []
        for g in datos:
            filas.append({
                'id_nota':          g.get('id'),
                'value':            g.get('value'),
                'period':           g.get('period'),
                'registrationDate': g.get('registrationDate'),
                # Objetos anidados → extraemos solo el id y el nombre
                'id_estudiante':    g.get('student', {}).get('id'),
                'nombre_estudiante':g.get('student', {}).get('studentName'),
                'id_materia':       g.get('subject', {}).get('id'),
                'nombre_materia':   g.get('subject', {}).get('subjectName'),
                'id_teacher':       g.get('teacher', {}).get('id'),
                'nombre_teacher':   g.get('teacher', {}).get('teacherName'),
            })

        df = pd.DataFrame(filas)

        # Agregamos 20 duplicados intencionales para el ejercicio de limpieza
        duplicados = df.sample(n=min(20, len(df)), random_state=42)
        df = pd.concat([df, duplicados], ignore_index=True)

        return df

    else:
        print(f"❌ /api/grades falló con código {response.status_code}")
        return pd.DataFrame()


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == '__main__':
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
    os.makedirs(output_dir, exist_ok=True)

    print("🔄 Consumiendo API del Sistema de Gestión de Notas...\n")

    df_estudiantes = obtener_estudiantes()
    df_materias    = obtener_materias()
    df_notas       = obtener_notas()

    # Guardamos solo si la API devolvió datos
    if not df_estudiantes.empty:
        df_estudiantes.to_csv(f'{output_dir}/estudiantes.csv', index=False)
    if not df_materias.empty:
        df_materias.to_csv(f'{output_dir}/materias.csv', index=False)
    if not df_notas.empty:
        df_notas.to_csv(f'{output_dir}/notas.csv', index=False)

    print("\n✅ Dataset generado exitosamente")
    print(f"   Estudiantes : {len(df_estudiantes)}")
    print(f"   Materias    : {len(df_materias)}")
    print(f"   Notas       : {len(df_notas)} (incluye duplicados intencionales)")