import json
import sys

def cargar_json(gestor_equipos):
    with open("gestor_equipos.json","r") as file:#se abre el archivo en modo lectura"r"
        return json.load(file)#se convierte el archivo json en un diccionario de python

def guardar_json(gestor_equipos):
    with open("gestor_equipos.json","w") as file:#se abre el archivo en modo escritura"w"
        json.dump(file,indent=4)#se carga el contenido en json y se guarda en el archivo

def verificar_ciudad(ciudad):
    with open("ciudades_colombia.json","r") as file:#se abre el archivo en modo lectura"r"
        return json.load(file)#se convierte el archivo json en un diccionario de python

def registrar_equipo(id,nombre,ciudad,dt):
    archivo = cargar_json("gestor_equipos.json")
    for equipo in archivo["equipo"]:
        if equipo["nombre"].lower() == nombre.lower():
            print("equipo ya esta registrado")
            return
    if not verificar_ciudad(ciudad):
        print("Ciudad no valida")

    equipo_nuevo = {
        "id": id + 1,
        "nombre":nombre,
        "ciudad":ciudad,
        "dt":dt
            }

    archivo["equipo"].append(equipo_nuevo)
    guardar_json("gestor_equipos.json",archivo)
    print("equipo registrado")

def buscar_equipo(key,value):
    archivo=cargar_json("gestor_equipos.json")
    for equipo in archivo.get("equipo",[]):
        if equipo.get(key,"").lower() == value.lower():
            return equipo
    print("Equipo no encontrado")

def actualizar_estadisticas_equipo(puntos,partidos_jugados,ganados,empatados,perdidos,goles_favor,goles_contra):
    archivo = cargar_json("gestor_equipos.json")
    if actualizar_estadisticas_equipo < 0:
        print("error no puede ingresar un numero menor a 0")
    else:
        pass
    archivo["estadisticas_equipo"]["puntos"] += puntos
    archivo["estadisticas_equipo"]["partidos_jugados"] += partidos_jugados
    archivo["estadisticas_equipo"]["ganados"] += ganados
    archivo["estadisticas_equipo"]["empatados"] += empatados
    archivo["estadisticas_equipo"]["perdidos"] += perdidos
    archivo["estadisticas_equipo"]["goles_favor"] += goles_favor
    archivo["estadisticas_equipo"]["goles_contra"] += goles_contra

    guardar_json("gestor_equipos.json",archivo)
    print("Estadisticas actualizadas")

if __name__ == "__main__":
    # Verifica si hay suficientes argumentos
    if len(sys.argv) < 2:
        sys.exit(1)
    
    # Toma la función a ejecutar desde los argumentos
    funcion = sys.argv[1]

    if funcion == "registrar_equipo":
        # Verifica si hay suficientes argumentos para registrar un equipo
        if len(sys.argv) < 6:
            print("Uso: script.py registrar_equipo <id> <nombre> <ciudad> <dt>")
            sys.exit(1)
        
        # Pasa los argumentos a la función
        id = int(sys.argv[2])
        nombre = sys.argv[3]
        ciudad = sys.argv[4]
        dt = sys.argv[5]
        registrar_equipo(id, nombre, ciudad, dt)

    elif funcion == "buscar_equipo":
        # Verifica si hay suficientes argumentos para buscar un equipo
        if len(sys.argv) < 4:
            sys.exit(1)
        
        # Pasa los argumentos a la función
        key = sys.argv[2]
        value = sys.argv[3]
        equipo = buscar_equipo(key, value)
        if equipo:
            print("Equipo encontrado:", equipo)

    else:
        print("Función no reconocida. Usa 'registrar_equipo' o 'buscar_equipo'.")

        

