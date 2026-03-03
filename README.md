# 📚 Sistema de Gestión de Notas — Grupo 8
Script de lógica base en Python para gestionar estudiantes, notas y promedios académicos.

> **Materia:** Nuevas Tecnologías Python | **Entrega:** Semana 6 | **Grupo:** 8

---

## 📋 Descripción
Script interactivo en terminal que permite registrar estudiantes, ingresar notas por materia y consultar promedios. Es la base lógica del proyecto integrador desarrollado con Spring Boot y React.

---

## ⚙️ Requisitos previos
- Python 3.8 o superior → [descargar](https://www.python.org/downloads/)
- Git → [descargar](https://git-scm.com)
- Windows con PowerShell o Git Bash

---

## 🚀 Configuración del proyecto

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

**PowerShell:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Git Bash:**
```bash
python -m venv .venv
source .venv/Scripts/activate
```

> Si PowerShell muestra error de permisos, ejecuta primero:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
> ```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5. Ejecutar el script
```bash
python app.py
```

---

## 🎮 Uso del sistema

Al ejecutar `app.py` verás este menú:

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
1. Primero registra un estudiante (opción 1)
2. Luego registra sus notas por materia (opción 2)
3. Consulta su promedio (opción 3) 
4. Historial completo (opción 4)

---

## 📁 Estructura del proyecto

```
sistema-gestion-notas-grupo-8/
│
├── app.py               ← script principal con menú interactivo
├── requirements.txt     ← dependencias del proyecto
├── README.md            ← este archivo
├── .gitignore           ← archivos ignorados por Git
│
├── data/
│   ├── raw/             ← datos originales (ignorado por Git)
│   └── processed/       ← datos procesados (ignorado por Git)
│
└── notebooks/           ← notebooks de exploración
```

---

## 🌿 Ramas del repositorio (GitFlow)

| Rama                 | Propósito                               |
|----------------------|-----------------------------------------|
| `main`               | Versión estable para entrega            |
| `develop`            | Integración del trabajo del equipo      |
| `feature/pedro`      | Desarrollo de Pedro (líder)             |
| `feature/mariana`    | Desarrollo de Mariana                   |
| `feature/kevin`      | Desarrollo de Kevin                     |
| `feature/didier`     | Desarrollo de Didier                    |

---

## 👥 Equipo

| Nombre         | Rol       | GitHub                                              |
|----------------|-----------|-----------------------------------------------------|
| Pedro Zamora   | Líder     | [@Pedro-2493](https://github.com/Pedro-2493)        |  
| Didier Achury  | Developer | [@esteban95-a](https://github.com/esteban95-a)      |  
| Mariana Ardila | Developer | [@mariana-ardila](https://github.com/mariana-ardila)|
| Kevin Vélez    | Developer | [@kevinn-9](https://github.com/kevinn-9)            |            

---

## 📝 Notas importantes
- La carpeta `.venv/` **no se sube a Git** — cada desarrollador crea la suya con `pip install -r requirements.txt`
- La carpeta `data/` **no se sube a Git** — puede contener datos sensibles