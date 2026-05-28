# Semana 12 - Momento 2
# Autor: Kevin Vélez (Grupo 8)
# Descripción: Obtiene datos desde la API REST de Spring Boot y realiza limpieza
#              (tipos, nulos, duplicados, rangos)

import pandas as pd
import requests
import os
import sys

API_BASE = "http://localhost:8080/api"
PROCESSED_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')


def fetch_json(endpoint):
    url = f"{API_BASE}/{endpoint}"
    print(f"  -> GET {url}")
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.ConnectionError:
        print(f"  ! ERROR: No se pudo conectar con {API_BASE}")
        print(f"    Asegurate de que el backend de Spring Boot este corriendo.")
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"  ! ERROR HTTP {e.response.status_code} en {url}")
        sys.exit(1)


def normalizar_estudiantes(data):
    return pd.DataFrame([{
        'id_estudiante': s['id'],
        'nombre': s['studentName'],
        'email': s['email'],
        'documento': s['document']
    } for s in data])


def normalizar_materias(data):
    return pd.DataFrame([{
        'id_materia': s['id'],
        'nombre': s['subjectName'],
        'descripcion': s.get('description', ''),
        'teacher_id': s.get('teacherId')
    } for s in data])


def normalizar_docentes(data):
    return pd.DataFrame([{
        'id_docente': t['id'],
        'nombre': t['teacherName'],
        'email': t['email']
    } for t in data])


def normalizar_notas(data):
    rows = []
    for g in data:
        student = g.get('student', {}) or {}
        subject = g.get('subject', {}) or {}
        teacher = g.get('teacher', {}) or {}
        rows.append({
            'id_nota': g['id'],
            'value': g['value'],
            'periodo': g['period'],
            'fecha_registro': g['registrationDate'],
            'id_estudiante': student.get('id'),
            'nombre_estudiante': student.get('studentName'),
            'id_materia': subject.get('id'),
            'nombre_materia': subject.get('subjectName'),
            'id_docente': teacher.get('id'),
            'nombre_docente': teacher.get('teacherName')
        })
    return pd.DataFrame(rows)


def normalizar_asistencias(data):
    rows = []
    for a in data:
        student = a.get('student', {}) or {}
        subject = a.get('subject', {}) or {}
        rows.append({
            'id_asistencia': a['id'],
            'fecha': a['date'],
            'estado': a['status'],
            'id_estudiante': student.get('id'),
            'nombre_estudiante': student.get('studentName'),
            'id_materia': subject.get('id'),
            'nombre_materia': subject.get('subjectName')
        })
    return pd.DataFrame(rows)


def limpiar_notas(df):
    print("  Limpiando dataset de notas...")

    antes = len(df)
    df = df.drop_duplicates()
    dupes = antes - len(df)
    if dupes:
        print(f"    Duplicados eliminados: {dupes}")

    df['fecha_registro'] = pd.to_datetime(df['fecha_registro'], errors='coerce')
    df['value'] = pd.to_numeric(df['value'], errors='coerce')

    nulos_valor = df['value'].isna().sum()
    if nulos_valor:
        df['value'] = df['value'].fillna(0.0)
        print(f"    Valores nulos en 'value' rellenados con 0.0: {nulos_valor}")

    fuera_rango = ((df['value'] < 0.0) | (df['value'] > 5.0)).sum()
    if fuera_rango:
        df['value'] = df['value'].clip(0.0, 5.0)
        print(f"    Notas fuera de rango 0-5 corregidas: {fuera_rango}")

    nulos_fecha = df['fecha_registro'].isna().sum()
    if nulos_fecha:
        df['fecha_registro'] = df['fecha_registro'].fillna(pd.Timestamp.now())
        print(f"    Fechas nulas rellenadas con fecha actual: {nulos_fecha}")

    df = df.sort_values('fecha_registro').reset_index(drop=True)
    return df


def limpiar_asistencias(df):
    print("  Limpiando dataset de asistencias...")
    antes = len(df)
    df = df.drop_duplicates()
    dupes = antes - len(df)
    if dupes:
        print(f"    Duplicados eliminados: {dupes}")

    df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
    estados_validos = ['PRESENTE', 'AUSENTE', 'TARDANZA']
    df['estado'] = df['estado'].where(df['estado'].isin(estados_validos), 'AUSENTE')

    nulos_fecha = df['fecha'].isna().sum()
    if nulos_fecha:
        df['fecha'] = df['fecha'].fillna(pd.Timestamp.now())
        print(f"    Fechas nulas en asistencia rellenadas: {nulos_fecha}")

    return df


def main():
    print("=" * 55)
    print("  LIMPIEZA DE DATOS — API REST Spring Boot")
    print("=" * 55)

    os.makedirs(PROCESSED_DIR, exist_ok=True)

    # 1. Fetch desde la API
    print("\n1. Obteniendo datos desde la API...")
    estudiantes_raw = fetch_json("students")
    materias_raw = fetch_json("subjects")
    docentes_raw = fetch_json("teachers")
    notas_raw = fetch_json("grades")
    asistencias_raw = fetch_json("attendance")

    # 2. Normalizar (aplanar objetos anidados)
    print("\n2. Normalizando datos...")
    df_estudiantes = normalizar_estudiantes(estudiantes_raw)
    df_materias = normalizar_materias(materias_raw)
    df_docentes = normalizar_docentes(docentes_raw)
    df_notas = normalizar_notas(notas_raw)
    df_asistencias = normalizar_asistencias(asistencias_raw)

    # 3. Limpiar
    print("\n3. Limpiando datasets...")
    df_notas = limpiar_notas(df_notas)
    df_asistencias = limpiar_asistencias(df_asistencias)

    # 4. Guardar
    print("\n4. Guardando datasets limpios...")
    df_estudiantes.to_csv(f'{PROCESSED_DIR}/estudiantes_limpios.csv', index=False)
    df_materias.to_csv(f'{PROCESSED_DIR}/materias_limpios.csv', index=False)
    df_docentes.to_csv(f'{PROCESSED_DIR}/docentes_limpios.csv', index=False)
    df_notas.to_csv(f'{PROCESSED_DIR}/notas_limpios.csv', index=False)
    df_asistencias.to_csv(f'{PROCESSED_DIR}/asistencias_limpios.csv', index=False)

    print("\n" + "=" * 55)
    print("  [OK] LIMPIEZA COMPLETADA")
    print("=" * 55)
    print(f"  Estudiantes : {len(df_estudiantes)}")
    print(f"  Materias    : {len(df_materias)}")
    print(f"  Docentes    : {len(df_docentes)}")
    print(f"  Notas       : {len(df_notas)}")
    print(f"  Asistencias : {len(df_asistencias)}")
    print(f"  Guardado en : {PROCESSED_DIR}")
    print("=" * 55)


if __name__ == '__main__':
    main()
