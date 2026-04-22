# 📚 Sistema de Gestión de Notas — Grupo 8

> Proyecto Integrador Nivel III · Submódulo: Nuevas Tecnologías para la Programación  
> **Materia:** Nuevas Tecnologías Python | **Institución:** CESDE | **Semestre:** 3

---

## 👥 Equipo

| Nombre | Rol | GitHub |
|---|---|---|
| Pedro Zamora | 👑 Líder | [@Pedro-2493](https://github.com/Pedro-2493) |
| Kevin Vélez | Developer | [@kevinn-9](https://github.com/kevinn-9) |
| Mariana Ardila | Developer | [@mariana-ardila](https://github.com/mariana-ardila) |
| Didier Achury | Developer | [@esteban95-a](https://github.com/esteban95-a) |

---

## 📌 Descripción del Proyecto

El **Sistema de Gestión de Notas** centraliza y digitaliza los procesos académicos de una institución educativa. Permite registrar estudiantes, materias y calificaciones, calcular promedios y generar reportes analíticos.

El proyecto se desarrolla en tres capas tecnológicas:

- **Python / Pandas** — Preprocesamiento, limpieza y análisis de datos académicos
- **Spring Boot** — API REST para la gestión del backend
- **React** — Interfaz web para interacción con el sistema

---

## ⚙️ Requisitos previos

- Python 3.8 o superior → [descargar](https://www.python.org/downloads/)
- Git → [descargar](https://git-scm.com)
- Windows con PowerShell o Git Bash

---

## 🚀 Configuración del entorno

### 1. Clonar el repositorio

```bash
git clone https://github.com/Pedro-2493/sistema-gestion-notas-grupo-8.git
cd sistema-gestion-notas-grupo-8
```

### 2. Moverse a la rama de desarrollo

```bash
git checkout dev
```

### 3. Crear el entorno virtual

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

> Si PowerShell muestra error de permisos ejecuta primero:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
> ```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🎮 Momento 1 — Semana 6: Lógica Base en Python

Script interactivo con menú en terminal para registrar estudiantes y notas usando diccionarios y listas.

```bash
python app.py
```

Al ejecutarlo verás este menú:

```
==================================================
   SISTEMA DE GESTION DE NOTAS — Grupo 8
==================================================
  1. Registrar estudiante
  2. Registrar nota
  3. Ver promedio de un estudiante
  4. Ver historial de notas
  5. Listar todos los estudiantes
  6. Salir
==================================================
```

**Flujo básico:**
1. Registra un estudiante (opción 1)
2. Registra sus notas por materia (opción 2)
3. Consulta su promedio (opción 3)
4. Consulta el historial completo (opción 4)

---

## 📊 Momento 2 — Semana 12: Exploración y Transformación de Datos (Pandas)

### 👑 Pedro — Generación del dataset

Genera automáticamente los datasets ficticios con más de 1100 registros.

```bash
python src/generar_dataset.py
```

Archivos generados en `data/raw/`:
- `estudiantes.csv` — 50 estudiantes con nombre, email, documento y grupo
- `materias.csv` — 8 materias con créditos
- `notas.csv` — 1100+ registros por periodo (incluye nulos y duplicados intencionales)

---

### 🧹 Kevin — Limpieza de datos

```bash
python src/limpieza.py
```

Operaciones aplicadas:
- Eliminación de registros duplicados
- Manejo de valores nulos en columna `observacion`
- Conversión de `fecha_registro` de texto a tipo `datetime`
- Exporta `data/processed/datos_limpios.csv`

---

### 📈 Mariana — Agrupaciones y columnas calculadas

```bash
python src/transformacion_groupby.py
```

Transformaciones:
- Columna calculada `nota_final` = (nota1 × 30%) + (nota2 × 30%) + (nota3 × 40%)
- Columna `estado` = Aprobado / Reprobado (umbral: 3.0)
- `groupby` por materia: promedio, mínima, máxima y total estudiantes
- `groupby` por periodo: distribución de aprobados y reprobados

---

### 🔗 Didier — Cruce de datos con merge/join

```bash
python src/transformacion_merge.py
```

Transformaciones:
- `merge` de notas con estudiantes por `id_estudiante`
- `merge` del resultado con materias por `id_materia`
- Dataset final enriquecido con 16 columnas
- Exporta `data/processed/dataset_completo.csv`

---

## 🗂️ Estructura del Repositorio

```
sistema-gestion-notas-grupo-8/
│
├── app.py                          ← Momento 1: menú interactivo
├── requirements.txt                ← dependencias del proyecto
├── README.md
├── .gitignore
│
├── data/
│   ├── raw/                        ← datasets originales (se suben al repo)
│   │   ├── estudiantes.csv
│   │   ├── materias.csv
│   │   └── notas.csv
│   └── processed/                  ← datos procesados (ignorado por Git)
│
├── notebooks/                      ← experimentos en Google Colab
│
└── src/                            ← scripts Python de producción
    ├── generar_dataset.py          ← Pedro
    ├── limpieza.py                 ← Kevin
    ├── transformacion_groupby.py   ← Mariana
    └── transformacion_merge.py     ← Didier
```

---

## 🌿 Estrategia GitFlow

```
main
└── dev
    └── feature/analisis-pandas
        ├── feature/pedro       ← Pedro (dataset + estructura)
        ├── feature/kevin       ← Kevin (limpieza)
        ├── feature/mariana     ← Mariana (groupby)
        └── feature/didier      ← Didier (merge)
```

Cada integrante trabaja en su rama personal, hace merge a `feature/analisis-pandas` al terminar. El líder revisa y hace el merge final a `dev`.

| Rama | Propósito |
|---|---|
| `main` | Versión estable para entrega final |
| `dev` | Integración del trabajo del equipo |
| `feature/analisis-pandas` | Rama principal del Momento 2 |
| `feature/pedro` | Desarrollo del líder |
| `feature/kevin` | Limpieza de datos |
| `feature/mariana` | Transformaciones groupby |
| `feature/didier` | Transformaciones merge |

---

## 🔗 Conexión con el Proyecto Integrador

| Pregunta que responde el análisis | Archivo |
|---|---|
| ¿Cuál es el promedio de notas por materia? | `resumen_por_materia.csv` |
| ¿Cuántos estudiantes aprobaron cada periodo? | `rendimiento_periodo.csv` |
| ¿Qué estudiante tiene mejor rendimiento? | `dataset_completo.csv` |

En el Momento 3 estos análisis se conectarán con la API REST de Spring Boot para trabajar con datos reales.

---

## 📋 Estado del Proyecto

| Momento | Semana | Estado |
|---|---|---|
| Momento 1 — Lógica base Python | Semana 6 | ✅ Completado |
| Momento 2 — Análisis con Pandas | Semana 12 | 🔄 En progreso |
| Momento 3 — Visualización y APIs | Semana 17 | ⏳ Pendiente |

---

## 📝 Notas importantes

- La carpeta `.venv/` **no se sube a Git** — cada desarrollador crea la suya localmente
- La carpeta `data/processed/` **no se sube a Git** — se genera al ejecutar cada script
- La carpeta `data/raw/` **sí se sube** — contiene los datasets base que todos necesitan