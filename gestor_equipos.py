import json
from datetime import datetime

def cargar_json():
    with open("gestor_equipos.json","r", encoding="utf-8") as file:#se abre el archivo en modo lectura"r"
        return json.load(file)#se convierte el archivo json en un diccionario de python

def guardar_json(archivo):
    with open("gestor_equipos.json","w") as file:#se abre el archivo en modo escritura"w"
        json.dump(archivo,file,indent=4)#se carga el contenido en json y se guarda en el archivo

def verificar_ciudad(ciudad):
    with open("ciudades_colombia.json","r") as file:
        departamentos = json.load(file)
        for departamento in departamentos:
            if ciudad.lower() in [c.lower() for c in departamento["ciudades"]]:
                return True

def registrar_equipo(nombre,ciudad,dt):
    archivo = cargar_json()
    
    for equipo in archivo.get("equipo",[]):
        if equipo["nombre"].lower() == nombre.lower():
            print("equipo ya esta registrado")
            return "Registro Fallido"
        
    if not verificar_ciudad(ciudad):
        return "Ciudad no valida"

    id_archivo = 0
    for equipo in archivo["equipo"]:
        id_actual = equipo["id_equipo"]
        if id_actual > id_archivo:
            id_archivo = id_actual
    id_nuevo = id_archivo + 1

    equipo_nuevo = {
        "id_equipo": id_nuevo,
        "nombre":nombre,
        "ciudad":ciudad,
        "dt":dt,
        "jugadores": [],
        "estadisticas_equipo": {
            "puntos": 0,
            "jugados": 0,
            "ganados": 0,
            "empatados": 0,
            "perdidos": 0,
            "goles_favor": 0,
            "goles_contra": 0
            }
    }

    archivo["equipo"].append(equipo_nuevo)
    guardar_json(archivo)
    print("equipo registrado")

def buscar_equipo(key,value):
    archivo=cargar_json()
    for equipo in archivo.get("equipo",[]):
        if equipo.get(key,"").lower() == value.lower():
            print(equipo)
            return True
    print("Ese valor no existe")
    return False

def actualizar_estadisticas_equipo(id_equipo,puntos,jugados,ganados,empatados,perdidos,goles_favor,goles_contra):
    archivo = cargar_json()
    for equipo in archivo["equipo"]:
        if equipo["id_equipo"] == int(id_equipo):
            if puntos < 0 or jugados < 0 or ganados < 0 or empatados < 0 or perdidos < 0 or goles_favor < 0 or goles_contra < 0:
                print("error no puede ingresar un numero menor a 0")
                return "No se actualizo el registro"
            else:
                equipo["estadisticas_equipo"]["puntos"] += puntos
                equipo["estadisticas_equipo"]["jugados"] += jugados
                equipo["estadisticas_equipo"]["ganados"] += ganados
                equipo["estadisticas_equipo"]["empatados"] += empatados
                equipo["estadisticas_equipo"]["perdidos"] += perdidos
                equipo["estadisticas_equipo"]["goles_favor"] += goles_favor
                equipo["estadisticas_equipo"]["goles_contra"] += goles_contra
                guardar_json(archivo)
                return "Estadisticas actualizadas"
                
    print("Equipo no encontrado")
    return "No se actualizo el registro"

if __name__ == "__main__":
        while True:
            print("Menu\n1.Registrar equipo\n2.Buscar equipo\n3.Actualizar estadisticas\n4.Salir")
            opcion = input("Ingrese una opcion:")
            if opcion == "1":
                nombre=input("Ingrese nombre de equipo:")
                ciudad=input("Ingrese ciudad:")
                dt=input("Ingrese nombre de tecnico:")
                if nombre == "" or ciudad == "" or dt == "":
                    print("No pueden haber campos vacios")   
                else:
                    respuesta = registrar_equipo(nombre,ciudad,dt)
                    print(respuesta)
            elif opcion == "2":
                key=input("Ingrese el valor de busqueda:")
                value=input("Ingrese el valor a buscar:")
                buscar_equipo(key,value) 

            elif opcion == "3":
                id_equipo = int(input("Ingresar el id del equipo para actualizar sus estadisticas"))
                puntos=int(input("Ingresar numero de puntos:"))
                jugados=int(input("Ingresar numero de partidos jugados:"))
                ganados=int(input("Ingresar numero de partidos ganados:"))
                empatados=int(input("Ingresar numero de partios empatados:"))
                perdidos=int(input("Ingresar numero de partidos perdidos:"))
                goles_favor=int(input("Ingresar numero de goles a favor:"))
                goles_contra=int(input("Ingresar numero de goles en contra:"))
                respuesta = actualizar_estadisticas_equipo(id_equipo,puntos,jugados,ganados,empatados,perdidos,goles_favor,goles_contra)
            elif opcion == "4":
                print("fin de programa =)")
                break
            else:
                print("Opcion invalida")



