📚 Sistema de Gestión de Notas — Grupo 8
Script de lógica base en Python para gestionar estudiantes, notas y promedios académicos.
Materia: Nuevas Tecnologías Python  |  Entrega: Semana 6  |  Grupo: 8

📋 Descripción
Script interactivo en terminal que permite registrar estudiantes, ingresar notas por materia y consultar promedios. Usa colorama para mostrar colores en la terminal y hacer la interfaz más clara.

⚙️ Requisitos previos

Python 3.8 o superior
Git
Windows con PowerShell o Git Bash

🚀 Configuración del proyecto
1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/proyecto_notas.git
cd proyecto_notas

2. Moverse a la rama de desarrollo
git checkout feature/kevin

3. Crear el entorno virtual
PowerShell:python -m venv venv


Git Bash:python -m venv venv
source venv/Scripts/activate

Si PowerShell muestra error de permisos, ejecuta primero:Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

4. Instalar dependencias
pip install -r requirements.txt
Esto instala la siguiente dependencia:

colorama==0.4.6 — permite mostrar colores en la terminal de Windows

También puedes instalarla manualmente:pip install colorama==0.4.6

5. Ejecutar el script
python app.py

6. Desactivar el entorno virtual
deactivate

🎮 Uso del sistema
Al ejecutar app.py verás este menú:
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
Flujo básico:

Primero registra un estudiante (opción 1)
Luego registra sus notas por materia (opción 2)
Consulta su promedio (opción 3)
Historial completo (opción 4)


📁 Estructura del proyecto
proyecto_notas/
│
├── app.py               ← script principal con menú interactivo
├── requirements.txt     ← dependencias del proyecto (colorama)
├── README.md            ← este archivo
└── .gitignore           ← archivos ignorados por Git

🌿 Ramas del repositorio
RamaPropósitofeature/kevinRama principal — configuración del entorno y estructurafeature/notasDesarrollo de funciones de registro de notasfeature/apruebaDesarrollo de la lógica de aprobación y promedios