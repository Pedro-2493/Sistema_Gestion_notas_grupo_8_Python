# Semana 12 - Momento 2
# Autor: Pedro Zamora (Líder Grupo 8)
# Descripción: Genera dataset ficticio del Sistema de Gestión de Notas

import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import os

fake = Faker('es_CO')
random.seed(42)

def generar_estudiantes():
    estudiantes = []
    for i in range(1, 51):
        estudiantes.append({
            'id_estudiante': i,
            'nombre': fake.first_name(),
            'apellido': fake.last_name(),
            'email': fake.email(),
            'documento': fake.numerify(text='##########'),
            'grupo': random.choice(['Grupo A', 'Grupo B', 'Grupo C'])
        })
    return pd.DataFrame(estudiantes)

def generar_materias():
    materias = [
        {'id_materia': 1, 'nombre': 'Matemáticas',      'creditos': 4},
        {'id_materia': 2, 'nombre': 'Programación',      'creditos': 4},
        {'id_materia': 3, 'nombre': 'Base de Datos',     'creditos': 3},
        {'id_materia': 4, 'nombre': 'Inglés',            'creditos': 2},
        {'id_materia': 5, 'nombre': 'Redes',             'creditos': 3},
        {'id_materia': 6, 'nombre': 'Algoritmos',        'creditos': 4},
        {'id_materia': 7, 'nombre': 'Estadística',       'creditos': 3},
        {'id_materia': 8, 'nombre': 'Ética Profesional', 'creditos': 2},
    ]
    return pd.DataFrame(materias)

def generar_notas(estudiantes, materias):
    notas = []
    id_nota = 1
    periodos = ['2024-1', '2024-2', '2025-1']

    for periodo in periodos:
        for _, estudiante in estudiantes.iterrows():
            for _, materia in materias.iterrows():
                if random.random() < 0.95:
                    fecha_base = datetime(2024, 1, 15) if periodo == '2024-1' else \
                                 datetime(2024, 7, 15) if periodo == '2024-2' else \
                                 datetime(2025, 1, 15)
                    fecha_registro = fecha_base + timedelta(days=random.randint(0, 60))

                    notas.append({
                        'id_nota': id_nota,
                        'id_estudiante': estudiante['id_estudiante'],
                        'id_materia': materia['id_materia'],
                        'periodo': periodo,
                        'nota1': round(random.uniform(1.0, 5.0), 1),
                        'nota2': round(random.uniform(1.0, 5.0), 1),
                        'nota3': round(random.uniform(1.0, 5.0), 1),
                        'fecha_registro': fecha_registro.strftime('%Y-%m-%d'),
                        'observacion': fake.sentence() if random.random() > 0.6 else None,
                    })
                    id_nota += 1

    df = pd.DataFrame(notas)
    duplicados = df.sample(n=20, random_state=42)
    df = pd.concat([df, duplicados], ignore_index=True)
    return df

if __name__ == '__main__':
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
    os.makedirs(output_dir, exist_ok=True)

    df_estudiantes = generar_estudiantes()
    df_materias    = generar_materias()
    df_notas       = generar_notas(df_estudiantes, df_materias)

    df_estudiantes.to_csv(f'{output_dir}/estudiantes.csv', index=False)
    df_materias.to_csv(f'{output_dir}/materias.csv',       index=False)
    df_notas.to_csv(f'{output_dir}/notas.csv',             index=False)

    print("✅ Dataset generado exitosamente")
    print(f"   Estudiantes : {len(df_estudiantes)}")
    print(f"   Materias    : {len(df_materias)}")
    print(f"   Notas       : {len(df_notas)} (incluye duplicados intencionales)")