# Semana 12 - Momento 2
# Autor: Didier Achury (Grupo 8)
# Descripción: Cruce de datos (merge/join) de estudiantes, materias, docentes,
#              notas y asistencias desde la API REST de Spring Boot

import pandas as pd
import os

PROCESSED_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')


def calcular_promedio_estudiante(df_notas):
    grupo = df_notas.groupby(
        ['id_estudiante', 'nombre_estudiante', 'id_materia', 'nombre_materia', 'periodo'],
        as_index=False, dropna=False
    )['value'].agg(
        promedio=('mean'),
        nota_min=('min'),
        nota_max=('max'),
        cantidad_notas=('count')
    )
    grupo['promedio'] = grupo['promedio'].round(2)
    grupo['estado'] = grupo['promedio'].apply(lambda x: 'Aprobado' if x >= 3.0 else 'Reprobado')
    return grupo


def merge_notas_estudiantes(df_promedio, df_estudiantes):
    """Merge 1: promedios con datos del estudiante (documento, email)."""
    return pd.merge(
        df_promedio,
        df_estudiantes[['id_estudiante', 'email', 'documento']],
        on='id_estudiante',
        how='left'
    )


def merge_con_materias(df, df_materias):
    """Merge 2: resultado con datos de la materia (descripción, teacher_id)."""
    return pd.merge(
        df,
        df_materias[['id_materia', 'descripcion', 'teacher_id']],
        on='id_materia',
        how='left'
    )


def merge_con_docentes(df, df_docentes):
    """Merge 3: resultado con datos del docente (email del docente)."""
    return pd.merge(
        df,
        df_docentes[['id_docente', 'email']].rename(
            columns={'id_docente': 'teacher_id', 'email': 'email_docente'}
        ),
        on='teacher_id',
        how='left'
    )


def merge_asistencias_con_estudiantes(df_asistencias, df_estudiantes):
    """Merge de asistencias con datos de estudiantes."""
    return pd.merge(
        df_asistencias,
        df_estudiantes[['id_estudiante', 'email', 'documento']],
        on='id_estudiante',
        how='left'
    )


def merge_asistencias_con_materias(df, df_materias):
    """Merge de asistencias+estudiantes con materias."""
    return pd.merge(
        df,
        df_materias[['id_materia', 'descripcion']],
        on='id_materia',
        how='left'
    )


def main():
    print("=" * 55)
    print("  TRANSFORMACIONES — MERGE / JOIN DE DATOS")
    print("=" * 55)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 1. Cargar datasets limpios
    print("\n1. Cargando datasets limpios...")
    df_notas = pd.read_csv(f'{PROCESSED_DIR}/notas_limpios.csv')
    df_estudiantes = pd.read_csv(f'{PROCESSED_DIR}/estudiantes_limpios.csv')
    df_materias = pd.read_csv(f'{PROCESSED_DIR}/materias_limpios.csv')
    df_docentes = pd.read_csv(f'{PROCESSED_DIR}/docentes_limpios.csv')
    df_asistencias = pd.read_csv(f'{PROCESSED_DIR}/asistencias_limpios.csv')

    print(f"  Notas       : {len(df_notas)}")
    print(f"  Estudiantes : {len(df_estudiantes)}")
    print(f"  Materias    : {len(df_materias)}")
    print(f"  Docentes    : {len(df_docentes)}")
    print(f"  Asistencias : {len(df_asistencias)}")

    # 2. Merge del dataset de notas
    print("\n2. Calculando promedios por (estudiante, materia, periodo)...")
    df_promedio = calcular_promedio_estudiante(df_notas)
    print(f"  Promedios calculados: {len(df_promedio)}")

    print("\n3. Merge 1: Promedios + Estudiantes (documento, email)...")
    df_completo = merge_notas_estudiantes(df_promedio, df_estudiantes)
    print(f"  Registros tras merge: {len(df_completo)}")

    print("\n4. Merge 2: Resultado + Materias (descripción, teacher_id)...")
    df_completo = merge_con_materias(df_completo, df_materias)
    print(f"  Registros tras merge: {len(df_completo)}")
    print(f"  Columnas totales: {list(df_completo.columns)}")

    print("\n5. Merge 3: Resultado + Docentes (email docente)...")
    df_completo = merge_con_docentes(df_completo, df_docentes)
    print(f"  Registros tras merge: {len(df_completo)}")
    print(f"  Columnas totales: {list(df_completo.columns)}")

    # 6. Merge del dataset de asistencias
    print("\n6. Merge de asistencias con estudiantes...")
    df_asist_completo = merge_asistencias_con_estudiantes(df_asistencias, df_estudiantes)
    print(f"  Registros: {len(df_asist_completo)}")

    print("\n7. Merge de asistencias con materias...")
    df_asist_completo = merge_asistencias_con_materias(df_asist_completo, df_materias)
    print(f"  Registros: {len(df_asist_completo)}")
    print(f"  Columnas: {list(df_asist_completo.columns)}")

    # 8. Guardar resultados
    print("\n8. Guardando datasets enriquecidos...")
    df_completo.to_csv(f'{OUTPUT_DIR}/dataset_completo.csv', index=False)
    df_asist_completo.to_csv(f'{OUTPUT_DIR}/asistencias_completo.csv', index=False)

    print("\n" + "=" * 55)
    print("  [OK] MERGE COMPLETADO")
    print("=" * 55)
    print(f"  Dataset completo notas  : {len(df_completo)} registros, {len(df_completo.columns)} columnas")
    print(f"  Asistencias completo    : {len(df_asist_completo)} registros, {len(df_asist_completo.columns)} columnas")
    print(f"  Guardado en             : {OUTPUT_DIR}")
    print("=" * 55)


if __name__ == '__main__':
    main()
