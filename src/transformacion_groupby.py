# Semana 12 - Momento 2
# Autor: Mariana Ardila (Grupo 8)
# Descripción: Agrupaciones (groupby) y columnas calculadas sobre datos
#              obtenidos desde la API REST de Spring Boot

import pandas as pd
import os

PROCESSED_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')


def calcular_promedio_estudiante(df):
    """Agrupa por (estudiante, materia, periodo) y calcula el promedio."""
    grupo = df.groupby(['id_estudiante', 'nombre_estudiante',
                        'id_materia', 'nombre_materia', 'periodo'],
                       as_index=False, dropna=False)['value'].agg(
        promedio='mean',
        nota_min='min',
        nota_max='max',
        cantidad_notas='count'
    )
    grupo['promedio'] = grupo['promedio'].round(2)
    grupo['estado'] = grupo['promedio'].apply(lambda x: 'Aprobado' if x >= 3.0 else 'Reprobado')
    return grupo


def resumen_por_materia(df_promedio):
    """GroupBy por materia: promedio general, mínimo, máximo y total estudiantes."""
    resumen = df_promedio.groupby(['id_materia', 'nombre_materia'], as_index=False).agg(
        promedio_general=('promedio', 'mean'),
        nota_minima_general=('promedio', 'min'),
        nota_maxima_general=('promedio', 'max'),
        total_estudiantes=('id_estudiante', 'nunique')
    )
    resumen['promedio_general'] = resumen['promedio_general'].round(2)
    resumen = resumen.sort_values('promedio_general', ascending=False).reset_index(drop=True)
    return resumen


def rendimiento_por_periodo(df_promedio):
    """GroupBy por periodo: distribución de aprobados y reprobados."""
    rendimiento = df_promedio.groupby(['periodo', 'estado'], as_index=False).agg(
        cantidad_estudiantes=('id_estudiante', 'nunique')
    )
    rendimiento = rendimiento.sort_values(['periodo', 'estado']).reset_index(drop=True)
    return rendimiento


def tabla_pivot_periodo(df_rendimiento):
    """Convierte el rendimiento por periodo en formato pivote."""
    pivot = df_rendimiento.pivot(
        index='periodo',
        columns='estado',
        values='cantidad_estudiantes'
    ).fillna(0).astype(int)
    pivot['Total'] = pivot.sum(axis=1)
    pivot = pivot.reset_index()
    for col in ['Aprobado', 'Reprobado']:
        if col not in pivot.columns:
            pivot[col] = 0
    columnas = [c for c in ['periodo', 'Aprobado', 'Reprobado', 'Total'] if c in pivot.columns]
    return pivot[columnas]


def resumen_por_docente(df_notas):
    """GroupBy por docente: cantidad de notas registradas y promedio."""
    resumen = df_notas.groupby(['id_docente', 'nombre_docente'], as_index=False).agg(
        total_notas=('id_nota', 'count'),
        promedio_general=('value', 'mean')
    )
    resumen['promedio_general'] = resumen['promedio_general'].round(2)
    resumen = resumen.sort_values('total_notas', ascending=False).reset_index(drop=True)
    return resumen


def main():
    print("=" * 55)
    print("  TRANSFORMACIONES — GROUPBY Y COLUMNAS CALCULADAS")
    print("=" * 55)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 1. Cargar datos limpios
    print("\n1. Cargando datos limpios...")
    df_notas = pd.read_csv(f'{PROCESSED_DIR}/notas_limpios.csv')
    print(f"    Registros de notas cargados: {len(df_notas)}")

    # 2. Columnas calculadas: promedio por (estudiante, materia, periodo)
    print("\n2. Calculando promedios por estudiante, materia y periodo...")
    df_promedio = calcular_promedio_estudiante(df_notas)
    print(f"    Combinaciones únicas: {len(df_promedio)}")

    resumen_estado = df_promedio['estado'].value_counts()
    for estado, count in resumen_estado.items():
        print(f"      {estado}: {count}")

    # 3. GroupBy por materia
    print("\n3. Resumen por materia...")
    df_resumen_materia = resumen_por_materia(df_promedio)
    print(df_resumen_materia.to_string(index=False))

    # 4. GroupBy por periodo
    print("\n4. Rendimiento por periodo...")
    df_rendimiento = rendimiento_por_periodo(df_promedio)
    df_pivot = tabla_pivot_periodo(df_rendimiento)
    print(df_pivot.to_string(index=False))

    # 5. Resumen por docente
    print("\n5. Resumen por docente...")
    df_docente = resumen_por_docente(df_notas)
    print(df_docente.to_string(index=False))

    # 6. Guardar resultados
    print("\n6. Guardando resultados...")
    df_promedio.to_csv(f'{OUTPUT_DIR}/promedio_estudiantes.csv', index=False)
    df_resumen_materia.to_csv(f'{OUTPUT_DIR}/resumen_por_materia.csv', index=False)
    df_pivot.to_csv(f'{OUTPUT_DIR}/rendimiento_periodo.csv', index=False)
    df_docente.to_csv(f'{OUTPUT_DIR}/resumen_por_docente.csv', index=False)

    print("\n" + "=" * 55)
    print("  [OK] TRANSFORMACIONES COMPLETADAS")
    print("=" * 55)
    print(f"  Promedio estudiantes  : {len(df_promedio)} registros")
    print(f"  Resumen por materia   : {len(df_resumen_materia)} materias")
    print(f"  Rendimiento por periodo: {len(df_pivot)} periodos")
    print(f"  Resumen por docente   : {len(df_docente)} docentes")
    print(f"  Guardado en           : {OUTPUT_DIR}")
    print("=" * 55)


if __name__ == '__main__':
    main()
