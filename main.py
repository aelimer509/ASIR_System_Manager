import menu1
import menu2
import menu3

def mostrar_menu():
    os.system("clear")
    print("====================================")
    print("      ASIR SYSTEM MANAGER v0.1      ")
    print("====================================")
    print("1. Información del sistema")
    print("2. Gestión de archivos y copias")
    print("3. Monitorización del equipo")
    print("0. Salir")
    opcion=str(input("Seleccione una opción: "))
    return opcion

while True:
    match mostrar_menu():
        case "1":
            print("Información del sistema")
        case "2":
            print("Gestión de archivos y copias")
        case "3":
            print("Monitorización del equipo")
        case "0":
            print(Saliendo...)
            break
        case _:
            print("Opción no válida)

