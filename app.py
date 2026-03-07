estudiantes = {}

# Lista de materias disponibles en el sistema
materias_disponibles = ["Matematicas", "Python", "Bases de Datos", "Ingles", "Estadistica"]



# FUNCIONES — cada una hace UNA sola cosa


def generar_codigo():
    """Genera un codigo unico para cada estudiante (E001, E002, ...)."""
    numero = len(estudiantes) + 1
    return f"E{numero:03d}"


def registrar_estudiante():
    """Registra un nuevo estudiante en el sistema."""
    print("\n--- REGISTRAR ESTUDIANTE ---")
    nombre = input("Nombre completo del estudiante: ").strip()

    if not nombre:
        print("El nombre no puede estar vacio.")
        return

    # Verificar que no exista un estudiante con el mismo nombre
    for datos in estudiantes.values():
        if datos["nombre"].lower() == nombre.lower():
            print(f"Ya existe un estudiante con el nombre '{nombre}'.")
            return

    codigo = generar_codigo()
    estudiantes[codigo] = {
        "nombre": nombre,
        "notas": {}
    }
    print(f"Estudiante registrado exitosamente. Codigo asignado: {codigo}")


def registrar_nota():
    """Registra una nota para un estudiante en una materia especifica."""
    print("\n--- REGISTRAR NOTA ---")

    if not estudiantes:
        print("No hay estudiantes registrados. Registra uno primero.")
        return

    # Mostrar lista de estudiantes para seleccionar
    mostrar_estudiantes()
    codigo = input("Ingresa el codigo del estudiante: ").strip().upper()

    if codigo not in estudiantes:
        print(f"No se encontro ningun estudiante con el codigo '{codigo}'.")
        return

    # Mostrar materias disponibles
    print("\nMaterias disponibles:")
    for i, materia in enumerate(materias_disponibles, 1):
        print(f"  {i}. {materia}")

    materia = input("Escribe el nombre de la materia: ").strip()

    if materia not in materias_disponibles:
        print(f"La materia '{materia}' no esta en la lista de materias disponibles.")
        return

    # Validar que la nota sea un numero entre 0 y 5
    try:
        nota = float(input("Ingresa la nota (0.0 a 5.0): "))
        if not (0.0 <= nota <= 5.0):
            print("La nota debe estar entre 0.0 y 5.0.")
            return
    except ValueError:
        print("Debes ingresar un numero valido.")
        return

    # Agregar la nota al diccionario del estudiante
    if materia not in estudiantes[codigo]["notas"]:
        estudiantes[codigo]["notas"][materia] = []

    estudiantes[codigo]["notas"][materia].append(nota)
    nombre = estudiantes[codigo]["nombre"]
    print(f"Nota {nota} registrada para {nombre} en {materia}.")


def calcular_promedio(lista_notas):
    """Calcula y retorna el promedio de una lista de notas."""
    if not lista_notas:
        return 0.0
    return sum(lista_notas) / len(lista_notas)


def ver_promedio():
    """Muestra el promedio general de un estudiante."""
    print("\n--- VER PROMEDIO ---")

    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    mostrar_estudiantes()
    codigo = input("Ingresa el codigo del estudiante: ").strip().upper()

    if codigo not in estudiantes:
        print(f"No se encontro ningun estudiante con el codigo '{codigo}'.")
        return

    estudiante = estudiantes[codigo]
    nombre = estudiante["nombre"]
    notas_por_materia = estudiante["notas"]

    if not notas_por_materia:
        print(f"{nombre} no tiene notas registradas aun.")
        return

    print(f"\nPromedio de {nombre} ({codigo}):")
    print("-" * 40)

    todas_las_notas = []

    for materia, notas in notas_por_materia.items():
        promedio_materia = calcular_promedio(notas)
        todas_las_notas.extend(notas)
        estado = "APROBADO" if promedio_materia >= 3.0 else "REPROBADO"
        print(f"  {materia:<20} Promedio: {promedio_materia:.2f}  [{estado}]")

    print("-" * 40)
    promedio_general = calcular_promedio(todas_las_notas)
    estado_general = "APROBADO" if promedio_general >= 3.0 else "REPROBADO"
    print(f"  {'PROMEDIO GENERAL':<20} {promedio_general:.2f}  [{estado_general}]")


def ver_historial():
    """Muestra todas las notas registradas de un estudiante."""
    print("\n--- HISTORIAL DE NOTAS ---")

    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    mostrar_estudiantes()
    codigo = input("Ingresa el codigo del estudiante: ").strip().upper()

    if codigo not in estudiantes:
        print(f"No se encontro ningun estudiante con el codigo '{codigo}'.")
        return

    estudiante = estudiantes[codigo]
    nombre = estudiante["nombre"]
    notas_por_materia = estudiante["notas"]

    print(f"\nHistorial completo de {nombre} ({codigo}):")
    print("=" * 50)

    if not notas_por_materia:
        print("  Este estudiante no tiene notas registradas.")
        return

    for materia, notas in notas_por_materia.items():
        notas_str = "  |  ".join([str(n) for n in notas])
        promedio = calcular_promedio(notas)
        print(f"\n  Materia : {materia}")
        print(f"  Notas   : {notas_str}")
        print(f"  Promedio: {promedio:.2f}")


def mostrar_estudiantes():
    """Muestra la lista de todos los estudiantes registrados."""
    print("\nEstudiantes registrados:")
    print("-" * 35)
    if not estudiantes:
        print("  (ninguno aun)")
    else:
        for codigo, datos in estudiantes.items():
            print(f"  {codigo} — {datos['nombre']}")
    print("-" * 35)


def mostrar_menu():
    """Imprime el menu principal del sistema."""
    print("\n" + "=" * 50)
    print("   SISTEMA DE GESTION DE NOTAS — Grupo 8")
    print("=" * 50)
    print("  1. Registrar estudiante")
    print("  2. Registrar nota")
    print("  3. Ver promedio de un estudiante")
    print("  4. Ver historial de notas")
    print("  5. Listar todos los estudiantes")
    print("  6. Salir")
    print("=" * 50)



# PUNTO DE ENTRADA — ciclo while con menu interactivo

if __name__ == "__main__":
    print("\nBienvenido al Sistema de Gestion de Notas.")
    print("Desarrollado por Grupo 8 — Nuevas Tecnologias Python.")

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion (1-6): ").strip()

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            registrar_nota()
        elif opcion == "3":
            ver_promedio()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            mostrar_estudiantes()
        elif opcion == "6":
            print("\nCerrando el sistema. Hasta luego.")
            break
        else:
            print("Opcion no valida. Escribe un numero entre 1 y 6.")