# Semana 12 - Momento 2
# Autor: Pedro Zamora (Líder Grupo 8)
# Descripción: Consume la API del Sistema de Gestión de Notas y genera el dataset

import pandas as pd
import requests
import os

BASE_URL = 'https://prueba-con-render.onrender.com'

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
        df = df.rename(columns={
            'id':          'id_estudiante',
            'studentName': 'nombre_estudiante',
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
            'subjectName': 'nombre_materia',
            'description': 'descripcion',
        })
        return df

    else:
        print(f"❌ /api/subjects falló con código {response.status_code}")
        return pd.DataFrame()


def obtener_notas():
    """
    Consume GET /api/grades y retorna un DataFrame.
    Aplana los objetos anidados student, subject y teacher.
    """
    response = requests.get(f'{BASE_URL}/api/grades')

    if response.status_code == 200:
        datos = response.json()
        print(f"✅ /api/grades    → {len(datos)} registros")

        filas = []
        for g in datos:
            filas.append({
                'id_nota':           g.get('id'),
                'id_estudiante':     g.get('student', {}).get('id'),
                'nombre_estudiante': g.get('student', {}).get('studentName'),
                'id_materia':        g.get('subject', {}).get('id'),
                'nombre_materia':    g.get('subject', {}).get('subjectName'),
                'id_teacher':        g.get('teacher', {}).get('id'),
                'nombre_teacher':    g.get('teacher', {}).get('teacherName'),
                'nota':              g.get('value'),
                'periodo':           g.get('period'),
                'fecha_registro':    g.get('registrationDate'),
            })

        df = pd.DataFrame(filas)

        # 20 duplicados intencionales para el ejercicio de limpieza
        duplicados = df.sample(n=min(20, len(df)), random_state=42)
        df = pd.concat([df, duplicados], ignore_index=True)
        return df

    else:
        print(f"❌ /api/grades falló con código {response.status_code}")
        return pd.DataFrame()


def obtener_asistencias():
    """Consume GET /api/attendance y retorna un DataFrame."""
    response = requests.get(f'{BASE_URL}/api/attendance')

    if response.status_code == 200:
        datos = response.json()
        print(f"✅ /api/attendance → {len(datos)} registros")

        filas = []
        for a in datos:
            filas.append({
                'id_asistencia':     a.get('id'),
                'id_estudiante':     a.get('student', {}).get('id'),
                'nombre_estudiante': a.get('student', {}).get('studentName'),
                'id_materia':        a.get('subject', {}).get('id'),
                'nombre_materia':    a.get('subject', {}).get('subjectName'),
                'fecha':             a.get('date'),
                'estado':            a.get('status'),
            })

        return pd.DataFrame(filas)

    else:
        print(f"❌ /api/attendance falló con código {response.status_code}")
        return pd.DataFrame()


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == '__main__':
   
    output_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'raw')
    os.makedirs(output_dir, exist_ok=True)

    print("🔄 Consumiendo API del Sistema de Gestión de Notas...\n")

    df_estudiantes = obtener_estudiantes()
    df_materias    = obtener_materias()
    df_notas       = obtener_notas()
    df_asistencias = obtener_asistencias()

    if not df_estudiantes.empty:
        df_estudiantes.to_csv(f'{output_dir}/estudiantes.csv', index=False)
    if not df_materias.empty:
        df_materias.to_csv(f'{output_dir}/materias.csv', index=False)
    if not df_notas.empty:
        df_notas.to_csv(f'{output_dir}/notas.csv', index=False)
    if not df_asistencias.empty:
        df_asistencias.to_csv(f'{output_dir}/asistencias.csv', index=False)

    print("\n✅ Dataset generado exitosamente")
    print(f"   Estudiantes  : {len(df_estudiantes)}")
    print(f"   Materias     : {len(df_materias)}")
    print(f"   Notas        : {len(df_notas)} (incluye duplicados intencionales)")
    print(f"   Asistencias  : {len(df_asistencias)}")