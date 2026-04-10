# 📚 Sistema de Gestión de Notas — Grupo 8

> Proyecto Integrador Nivel III · Submódulo: Nuevas Tecnologías para la Programación  
> Institución: CESDE · Semestre 3

---

## 👥 Equipo

| Rol | Integrante |
|---|---|
| 👑 Líder | Pedro Zamora |
| Desarrollador | Kevin Velez |
| Desarrolladora | Mariana Ardila |
| Desarrollador | Didier Achury|

---

## 📌 Descripción del Proyecto

El **Sistema de Gestión de Notas** centraliza y digitaliza los procesos académicos de una institución educativa. Permite registrar estudiantes, materias y calificaciones, calcular promedios y generar reportes analíticos.

El proyecto se desarrolla en tres capas tecnológicas:

- **Python / Pandas** — Preprocesamiento, limpieza y análisis de datos académicos
- **Spring Boot** — API REST para la gestión del backend
- **React** — Interfaz web para interacción con el sistema

---

## 🗂️ Estructura del Repositorio

```
sistema-gestion-notas/
│
├── data/
│   ├── raw/                  # Datasets originales generados (CSV)
│   │   ├── estudiantes.csv
│   │   ├── materias.csv
│   │   └── notas.csv
│   └── processed/            # Datos limpios y transformados
│
├── notebooks/                # Experimentos en Google Colab / Jupyter
│
├── src/                      # Scripts Python de producción
│   ├── generar_dataset.py    # Momento 2 · Pedro — Generación de datos
│   ├── limpieza.py           # Momento 2 · Kevin — Limpieza de datos
│   ├── transformacion_groupby.py  # Momento 2 · Mariana — Agrupaciones
│   └── transformacion_merge.py    # Momento 2 · Didier — Cruce de datos
│
├── .venv/                    # Entorno virtual (no se sube a GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Configuración del Entorno

### 1. Clonar el repositorio

```bash
git clone https://github.com/Pedro-2493/Sistema_Gestion_notas_grupo_8_Python.git
cd sistema-gestion-notas
```

### 2. Crear y activar el entorno virtual

**Git Bash:**
```bash
python -m venv .venv
source .venv/Scripts/activate
```

**PowerShell:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución por Momento

### Momento 1 — Semana 6: Lógica Base en Python

Script interactivo con menú en terminal para registrar estudiantes y notas usando diccionarios y listas.

```bash
python src/app.py
```

**Funcionalidades:**
- Registrar estudiantes con nombre y código único
- Registrar notas por estudiante y materia
- Calcular promedio general automáticamente
- Consultar historial de notas por estudiante
- Menú interactivo con ciclo `while`

---

### Momento 2 — Semana 12: Exploración y Transformación de Datos (Pandas)

#### 📁 Pedro — Generación del dataset

Genera automáticamente los datasets ficticios del sistema con más de 500 registros.

```bash
python src/generar_dataset.py
```

Archivos generados en `data/raw/`:
- `estudiantes.csv` — 50 estudiantes con nombre, email, documento y grupo
- `materias.csv` — 8 materias con créditos
- `notas.csv` — 1100+ registros de notas por periodo (incluye nulos y duplicados intencionales)

#### 🧹 Kevin — Limpieza de datos

```bash
python src/limpieza.py
```

Operaciones aplicadas:
- Eliminación de registros duplicados
- Manejo de valores nulos en columna `observacion`
- Conversión de `fecha_registro` de texto a tipo `datetime`
- Exporta `data/processed/datos_limpios.csv`

#### 📊 Mariana — Agrupaciones y columnas calculadas

```bash
python src/transformacion_groupby.py
```

Transformaciones:
- Columna calculada `nota_final` = (nota1 × 30%) + (nota2 × 30%) + (nota3 × 40%)
- Columna `estado` = Aprobado / Reprobado (umbral: 3.0)
- `groupby` por materia: promedio, mínima, máxima y total de estudiantes
- `groupby` por periodo: distribución de aprobados y reprobados

#### 🔗 Didier — Cruce de datos con merge/join

```bash
python src/transformacion_merge.py
```

Transformaciones:
- `merge` de notas con estudiantes por `id_estudiante`
- `merge` del resultado con materias por `id_materia`
- Dataset final enriquecido: 16 columnas con información completa
- Exporta `data/processed/dataset_completo.csv`

---

### Momento 3 — Semana 17: Visualización y Consumo de APIs *(próximamente)*

- Consumo de la API REST del backend con `requests`
- Visualizaciones con `Matplotlib` y `Seaborn`
- Reporte analítico final en HTML

---

## 🌿 Estrategia GitFlow

```
main
└── develop
    ├── feature/analisis-pandas      ← Pedro (Momento 2 - Dataset)
    ├── feature/limpieza-datos       ← Kevin
    ├── feature/transformacion-groupby ← Mariana
    └── feature/transformacion-merge   ← Didier
```

Cada integrante trabaja en su rama `feature/`, abre un Pull Request hacia `develop` al terminar, y el líder revisa antes de hacer el merge.

---

## 🔗 Conexión con el Proyecto Integrador

Este módulo de análisis en Python está directamente conectado con el backend y frontend del proyecto:

| Pregunta que responde el análisis | Fuente de datos |
|---|---|
| ¿Cuál es el promedio de notas por materia? | `resumen_por_materia.csv` |
| ¿Cuántos estudiantes aprobaron cada periodo? | `rendimiento_periodo.csv` |
| ¿Qué estudiante tiene el mejor rendimiento? | `dataset_completo.csv` |

En el Momento 3, estos análisis se conectarán directamente con la API REST de Spring Boot para trabajar con datos reales en lugar de ficticios.

---

## 📦 Dependencias

```
pandas
faker
openpyxl
```

Instalar con:
```bash
pip install -r requirements.txt
```

---

## 📋 Estado del Proyecto

| Momento | Semana | Estado |
|---|---|---|
| Momento 1 — Lógica base Python | Semana 6 | ✅ Completado |
| Momento 2 — Análisis con Pandas | Semana 12 | 🔄 En progreso |
| Momento 3 — Visualización y APIs | Semana 17 | ⏳ Pendiente |