# Menú principal del sistema de gestion de notas - Análisis de Datos
# Momento 2

import subprocess
import sys
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def ejecutar_script(ruta):
    resultado = subprocess.run([sys.executable, ruta], capture_output=False)    
    if resultado.returncode == 0:
        print("\n✅ Script ejecutado exitosamente.")
    else:
        print("\n❌ El script terminó con errores.")
    input("\nPresiona Enter para volver al menú...")        

def mostrar_menu():
    limpiar_pantalla()
    print("=" * 55)
    print(" SISTEMA DE GESTIÓN DE NOTAS - GRUPO 8")
    print(" Análisis de Datos con Pandas")
    print("=" * 55)
    print("  1. Generar dataset (carga desde API)")
    print("  2. Limpiar datos")
    print("  3. Transformaciones groupby")
    print("  4. Transformaciones merge / join")
    print("  5. Generar gráficos")
    print("  6. Ejecutar pipeline completo")
    print("  7. Salir")
    print("=" * 55)
    
def main():
    base    = os.path.dirname(__file__)
    analisis = os.path.join(base, "analisis")

    scripts = {
        "1": os.path.join(analisis, "carga.py"),
        "2": os.path.join(analisis, "limpieza.py"),
        "3": os.path.join(analisis, "03_transformacion_groupby.py"),
        "4": os.path.join(analisis, "transformacion.py"),
        "5": os.path.join(analisis, "grafico.py"),
    }

    nombres = {
        "1": "Generando dataset desde API",
        "2": "Limpiando datos",
        "3": "Transformaciones groupby",
        "4": "Transformaciones merge / join",
        "5": "Generando gráficos",
    }

    while True:
        mostrar_menu()
        opcion = input("  Selecciona una opción: ").strip()
            
        if opcion in scripts:
            ejecutar_script(scripts[opcion])

        elif opcion == "6":
            limpiar_pantalla()
            print(" Ejecutando pipeline completo...\n")
            for key in ["1", "2", "3", "4", "5"]:
                print(f"─── {nombres[key]} ───────────────────────────")
                resultado = subprocess.run([sys.executable, scripts[key]])
                if resultado.returncode != 0:
                    print(f"\n❌ Error en paso {key}. Pipeline detenido.")
                    break
                print()
            else:
                print("\n✅ Pipeline completo ejecutado sin errores.")
            input("\nPresiona Enter para volver al menú...")

        elif opcion == "7":
            print("\nHasta luego 👋")
            break   

        else:
            input("  Opción inválida. Presiona Enter para continuar.")
                
if __name__ == '__main__':
    main()