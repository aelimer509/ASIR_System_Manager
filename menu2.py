#Menú de Archivos y Copias
import shutil
import os

while True:
    os.system("clear")
    print("Menú de Gestión de Archivos")
    print("1. Copiar 'ejemplo.txt' a 'laboratorio/salidas'")
    print("2. Copiar 'ejemplo.txt' a 'laboratorio/salidas' conservando metadatos")
    print("3. Consultar espacio en disco (total, usado, libre en GiB)")
    print("4. Crear archivo ZIP desde una carpeta en 'laboratorio/salidas'")
    print("0. Volver al menú / Salir")
    opcion=str(input("Deme una opción: ")).strip()
    match opcion:
        case "1":
            print("Copiar achivo")
            origen=os.path.join("laboratorio","ejemplo.txt")
            destino=os.path.join("laboratorio","salidas")
            os.makedirs(destino, exist_ok=True) # Con "exist_ok=True" si salidas no existe, lo crea. Similar en bash a "mkdir -p carpeta"
            
            if os.path.exists(origen):
                try:
                    shutil.copy(origen,destino)
                    print(f"Archivo copiado con éxito a {destino}")
                except Exception:
                    print("No se pudo copiar el archivo")
            else:
                print(f"El archivo de origen {origen} no existe")
            input("Pulse enter para continuar...")
        case "2":
            print("Copiar achivo con metadatos")
            origen=os.path.join("laboratorio","ejemplo.txt")
            destino=os.path.join("laboratorio","salidas")
            os.makedirs(destino, exist_ok=True) # Con "exist_ok=True" si salidas no existe, lo crea. Similar en bash a "mkdir -p carpeta"
            
            if os.path.exists(origen):
                try:
                    shutil.copy2(origen,destino)
                    print(f"Archivo copiado con éxito a {destino}")
                except Exception:
                    print("No se pudo copiar el archivo")
            else:
                print(f"El archivo de origen {origen} no existe")
            input("Pulse enter para continuar...")
        case "3":
            print("Consultar el espacio total, utilizado y libre en GiB")
            ruta_objetivo="laboratorio"
            uso_disco=shutil.disk_usage(ruta_objetivo) # Almacena una tupla con nombres que contiene tres valores "total", "used" y "free"
            print(uso_disco)
            input("Pulse enter para continuar...")
        case "0":
            print("Saliendo...")
            break
        case _:
            print("Opción no válida")
        
            