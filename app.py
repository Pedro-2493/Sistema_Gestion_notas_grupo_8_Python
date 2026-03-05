from colorama import init, Fore, Style
init(autoreset=True)

estudiantes = {}

materias_disponibles = ["Matematicas", "Python", "Bases de Datos", "Ingles", "Estadistica"]


def generar_codigo():
    numero = len(estudiantes) + 1
    return f"E{numero:03d}"


def registrar_estudiante():
    print(Fore.CYAN + "\n--- REGISTRAR ESTUDIANTE ---")
    nombre = input("Nombre completo del estudiante: ").strip()

    if not nombre:
        print(Fore.RED + "El nombre no puede estar vacio.")
        return

    for datos in estudiantes.values():
        if datos["nombre"].lower() == nombre.lower():
            print(Fore.RED + f"Ya existe un estudiante con el nombre '{nombre}'.")
            return

    codigo = generar_codigo()
    estudiantes[codigo] = {
        "nombre": nombre,
        "notas": {}
    }
    print(Fore.GREEN + f"Estudiante registrado exitosamente. Codigo asignado: {codigo}")


def registrar_nota():
    print(Fore.CYAN + "\n--- REGISTRAR NOTA ---")

    if not estudiantes:
        print(Fore.RED + "No hay estudiantes registrados. Registra uno primero.")
        return

    mostrar_estudiantes()
    codigo = input("Ingresa el codigo del estudiante: ").strip().upper()

    if codigo not in estudiantes:
        print(Fore.RED + f"No se encontro ningun estudiante con el codigo '{codigo}'.")
        return

    print("\nMaterias disponibles:")
    for i, materia in enumerate(materias_disponibles, 1):
        print(f"  {i}. {materia}")

    materia = input("Escribe el nombre de la materia: ").strip()

    if materia not in materias_disponibles:
        print(Fore.RED + f"La materia '{materia}' no esta en la lista de materias disponibles.")
        return

    try:
        nota = float(input("Ingresa la nota (0.0 a 5.0): "))
        if not (0.0 <= nota <= 5.0):
            print(Fore.RED + "La nota debe estar entre 0.0 y 5.0.")
            return
    except ValueError:
        print(Fore.RED + "Debes ingresar un numero valido.")
        return

    if materia not in estudiantes[codigo]["notas"]:
        estudiantes[codigo]["notas"][materia] = []

    estudiantes[codigo]["notas"][materia].append(nota)
    nombre = estudiantes[codigo]["nombre"]
    print(Fore.GREEN + f"Nota {nota} registrada para {nombre} en {materia}.")


