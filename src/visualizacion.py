# Semana 12 - Momento 2
# Autor: Kevin Velez (Grupo 8)
# Descripcion: Modulo de visualizacion con 4 graficos basados en datos
#              procesados del backend Spring Boot

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", palette="muted")

PROCESSED_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')
FIGURES_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'figures')


def grafico_promedio_materias():
    df = pd.read_csv(f'{PROCESSED_DIR}/resumen_por_materia.csv')
    df = df.sort_values('promedio_general', ascending=True)

    plt.figure(figsize=(10, 6))
    bars = plt.barh(df['nombre_materia'], df['promedio_general'],
                    color=sns.color_palette("viridis", len(df)))
    for bar, val in zip(bars, df['promedio_general']):
        plt.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2,
                 f'{val:.2f}', va='center', fontsize=9)

    plt.xlabel('Promedio General')
    plt.ylabel('Materia')
    plt.title('Promedio de Notas por Materia')
    plt.xlim(0, 5.5)
    plt.tight_layout()
    plt.savefig(f'{FIGURES_DIR}/promedio_materias.png', dpi=150)
    plt.close()
    print(f"  [OK] promdio_materias.png")


def grafico_rendimiento_periodo():
    df = pd.read_csv(f'{PROCESSED_DIR}/rendimiento_periodo.csv')
    df_melted = df.melt(id_vars=['periodo'], value_vars=['Aprobado', 'Reprobado'],
                        var_name='Estado', value_name='Cantidad')

    plt.figure(figsize=(9, 6))
    sns.barplot(data=df_melted, x='periodo', y='Cantidad', hue='Estado',
                palette={'Aprobado': '#2ecc71', 'Reprobado': '#e74c3c'})

    plt.xlabel('Periodo Academico')
    plt.ylabel('Cantidad de Estudiantes')
    plt.title('Rendimiento por Periodo')
    plt.legend(title='Estado')
    plt.tight_layout()
    plt.savefig(f'{FIGURES_DIR}/rendimiento_periodo.png', dpi=150)
    plt.close()
    print(f"  [OK] rendimiento_periodo.png")


def grafico_distribucion_notas():
    df = pd.read_csv(f'{PROCESSED_DIR}/notas_limpios.csv')

    plt.figure(figsize=(10, 6))
    sns.histplot(df['value'], bins=12, kde=True, color='#3498db',
                 edgecolor='white', alpha=0.7)

    plt.axvline(x=3.0, color='#e74c3c', linestyle='--', linewidth=2,
                label='Umbral aprobacion (3.0)')
    media = df['value'].mean()
    plt.axvline(x=media, color='#f39c12', linestyle=':', linewidth=2,
                label=f'Media ({media:.2f})')

    plt.xlabel('Valor de Nota')
    plt.ylabel('Frecuencia')
    plt.title('Distribucion de Notas')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'{FIGURES_DIR}/distribucion_notas.png', dpi=150)
    plt.close()
    print(f"  [OK] distribucion_notas.png")


def grafico_rendimiento_docentes():
    df = pd.read_csv(f'{PROCESSED_DIR}/resumen_por_docente.csv')
    df = df.sort_values('promedio_general', ascending=True)

    plt.figure(figsize=(10, 6))
    bars = plt.barh(df['nombre_docente'], df['promedio_general'],
                    color=sns.color_palette("rocket", len(df)))
    for bar, val in zip(bars, df['promedio_general']):
        plt.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2,
                 f'{val:.2f}', va='center', fontsize=9)

    plt.xlabel('Promedio General de Notas')
    plt.ylabel('Docente')
    plt.title('Rendimiento por Docente')
    plt.xlim(0, 5.5)
    plt.tight_layout()
    plt.savefig(f'{FIGURES_DIR}/rendimiento_docentes.png', dpi=150)
    plt.close()
    print(f"  [OK] rendimiento_docentes.png")


def generar_todos():
    os.makedirs(FIGURES_DIR, exist_ok=True)

    print("Generando graficos...")
    grafico_promedio_materias()
    grafico_rendimiento_periodo()
    grafico_distribucion_notas()
    grafico_rendimiento_docentes()

    print(f"\n  {4} graficos guardados en: {FIGURES_DIR}")


if __name__ == '__main__':
    generar_todos()
