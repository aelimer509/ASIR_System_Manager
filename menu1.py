#Menú de información del sistema
import os

while True:
    os.system("clear")
    print("Menú de Información del Sistema")
    print("1.Mostrar el nombre del equipo, el tipo de sistema operativo y el número de CPU lógicas.")
    print("2. Mostrar el directorio de trabajo actual")
    print("3. Listar contenido de la carpeta 'laboratorio'")
    print("4. Crear directorio de prueba en 'laboratorio/salidas'")
    print("0. Volver al menú")
    print("")
    opcion=str(input("Deme una opcion: ")).strip()
    match opcion:
        case "1":
            print("Información del Sistema:")
            print(f"Nombre del equipo -> {os.popen('hostname').read().strip()}")
            print(f"Tipo de Sistema Operativo -> {os.uname()}")
            print(f"Número de CPU lógicas -> {os.cpu_count()}")
            input("Pulse enter para continuar...")
        case "2":
            print(f"Directorio de trabajo actual -> {os.getcwd()}")
            input("Pulse enter para continuar...")
        case "3":
            print("Contenido de la carpeta 'laboratorio': ")
            print(f"{os.listdir('laboratorio')}")
            input("Pulse enter para continuar...")
        case "4":
            print("Creando Directorio de Prueba")
            ndir=str(input("Deme el nombre del directorio a crear: ")).strip()

            ruta_carpeta=os.path.join("laboratorio","salidas",ndir)
            if os.path.exists(ruta_carpeta):
                print(f"El directorio especificado {ndir} ya existe")
            else:
                try:
                    os.makedirs(ruta_carpeta)
                    print(f"Directorio {ndir} creado con éxito en la ruta {ruta_carpeta}")
                except Exception:
                    print(f"Ocurrió un error al crear la carpeta")
            input("Pulse enter para continuar...")

        case _:
            break