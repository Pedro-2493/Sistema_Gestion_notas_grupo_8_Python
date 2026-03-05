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


def calcular_promedio(lista_notas):
    if not lista_notas:
        return 0.0
    return sum(lista_notas) / len(lista_notas)


def ver_promedio():
    print(Fore.CYAN + "\n--- VER PROMEDIO ---")

    if not estudiantes:
        print(Fore.RED + "No hay estudiantes registrados.")
        return

    mostrar_estudiantes()
    codigo = input("Ingresa el codigo del estudiante: ").strip().upper()

    if codigo not in estudiantes:
        print(Fore.RED + f"No se encontro ningun estudiante con el codigo '{codigo}'.")
        return

    estudiante = estudiantes[codigo]
    nombre = estudiante["nombre"]
    notas_por_materia = estudiante["notas"]

    if not notas_por_materia:
        print(Fore.YELLOW + f"{nombre} no tiene notas registradas aun.")
        return

    print(f"\nPromedio de {nombre} ({codigo}):")
    print("-" * 40)

    todas_las_notas = []

    for materia, notas in notas_por_materia.items():
        promedio_materia = calcular_promedio(notas)
        todas_las_notas.extend(notas)
        if promedio_materia >= 3.0:
            estado = Fore.GREEN + "APROBADO"
        else:
            estado = Fore.RED + "REPROBADO"
        print(f"  {materia:<20} Promedio: {promedio_materia:.2f}  [{estado}{Style.RESET_ALL}]")

    print("-" * 40)
    promedio_general = calcular_promedio(todas_las_notas)
    if promedio_general >= 3.0:
        estado_general = Fore.GREEN + "APROBADO"
    else:
        estado_general = Fore.RED + "REPROBADO"
    print(f"  {'PROMEDIO GENERAL':<20} {promedio_general:.2f}  [{estado_general}{Style.RESET_ALL}]")


def ver_historial():
    print(Fore.CYAN + "\n--- HISTORIAL DE NOTAS ---")

    if not estudiantes:
        print(Fore.RED + "No hay estudiantes registrados.")
        return

    mostrar_estudiantes()
    codigo = input("Ingresa el codigo del estudiante: ").strip().upper()

    if codigo not in estudiantes:
        print(Fore.RED + f"No se encontro ningun estudiante con el codigo '{codigo}'.")
        return

    estudiante = estudiantes[codigo]
    nombre = estudiante["nombre"]
    notas_por_materia = estudiante["notas"]

    print(f"\nHistorial completo de {nombre} ({codigo}):")
    print("=" * 50)

    if not notas_por_materia:
        print(Fore.YELLOW + "  Este estudiante no tiene notas registradas.")
        return

    for materia, notas in notas_por_materia.items():
        notas_str = "  |  ".join([str(n) for n in notas])
        promedio = calcular_promedio(notas)
        print(f"\n  Materia : {materia}")
        print(f"  Notas   : {notas_str}")
        print(f"  Promedio: {promedio:.2f}")


def mostrar_estudiantes():
    print("\nEstudiantes registrados:")
    print("-" * 35)
    if not estudiantes:
        print(Fore.YELLOW + "  (ninguno aun)")
    else:
        for codigo, datos in estudiantes.items():
            print(f"  {codigo} — {datos['nombre']}")
    print("-" * 35)


def mostrar_menu():
    print("\n" + "=" * 50)
    print(Fore.CYAN + "   SISTEMA DE GESTION DE NOTAS — Grupo 8")
    print(Style.RESET_ALL + "=" * 50)
    print("  1. Registrar estudiante")
    print("  2. Registrar nota")
    print("  3. Ver promedio de un estudiante")
    print("  4. Ver historial de notas")
    print("  5. Listar todos los estudiantes")
    print("  6. Salir")
    print("=" * 50)


if __name__ == "__main__":
    print(Fore.CYAN + "\nBienvenido al Sistema de Gestion de Notas.")
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
            print(Fore.YELLOW + "\nCerrando el sistema. Hasta luego.")
            break
        else:
            print(Fore.RED + "Opcion no valida. Escribe un numero entre 1 y 6.")
