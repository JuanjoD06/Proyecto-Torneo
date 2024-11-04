import json
from datetime import datetime

def cargar_json():
    with open("gestor_partidos.json","r", encoding="utf-8") as file:#se abre el archivo en modo lectura"r"
        return json.load(file)#se convierte el archivo json en un diccionario de python

def guardar_json(archivo):
    with open("gestor_partidos.json","w") as file:#se abre el archivo en modo escritura"w"
        json.dump(archivo,file,indent=4)#se carga el contenido en json y se guarda en el archivo

def verificar_id_equipo(id_equipo):
    with open("gestor_equipos.json", "r")as file:
        equipos = json.load(file)
        for equipo in equipos["equipo"]:
            if equipo["id_equipo"] == int(id_equipo):
                return True
        return False
    
def verificar_id_jugador(id_jugador):
    with open("gestor_jugadores.json", "r")as file:
        jugadores = json.load(file)
        for jugador in jugadores["jugador"]:
            if jugador["id_jugador"] == int(id_jugador):
                return True
        return False
    
def registrar_partido(fecha,id_arbitro,equipo_local,equipo_visitante,goles_local,goles_visitante):
    archivo = cargar_json()

    if equipo_local == equipo_visitante:
        print("El equipo local y el visitante deben de ser diferentes")
    
    if not verificar_id_equipo(equipo_local):
        print("Este equipo no existe")
        return "Registro fallido"
    
    if not verificar_id_equipo(equipo_visitante):
        print("Este equipo no existe")
        return "Registro fallido"
    
    for partido in archivo.get("partido",[]):
        if partido["fecha"] == fecha and (partido["equipo_local"] == equipo_local and partido["equipo_visitante"] == equipo_visitante or
                                          partido["equipo_local"] == equipo_visitante and partido["equipo_visitante"] == equipo_local):
            print("ya hay un partido en esta fecha y con estos equipos")
            return "Registro Fallido"
        

    id_archivo = 0
    for partido in archivo["partido"]:
        id_actual = partido["id_partido"]
        if id_actual > id_archivo:
            id_archivo = id_actual
    id_nuevo = id_archivo + 1

    equipo_nuevo ={
            "id_partido":id_nuevo,
            "fecha":fecha,
            "id_arbitro":id_arbitro,
            "equipo_local":equipo_local,
            "equipo_visitante":equipo_visitante,
            "goles_local":goles_local,
            "goles_visitante":goles_visitante,
            "alineacion_local":[],
            "alineacion_visitante":[],
            "eventos":
                    {
                        "minuto":0,
                        "tipo":"gol",
                        "jugador":0,
                        "equipo":0
                    }           
}

    archivo["partido"].append(equipo_nuevo)
    guardar_json(archivo)
    print("partido registrado")
    
def actualizar_estadisticas_equipo(id_partido,goles_local,goles_visitante):
    archivo = cargar_json()
    for partido in archivo["partido"]:
            if partido["id_partido"] == int(id_partido):
                if int(goles_local) < 0 or int(goles_visitante) < 0: 
                    print("error no puede ingresar un numero menor a 0")
                    return "Actualizacion fallida"
                else:
                    partido["goles_local"] += goles_local
                    partido["goles_visitante"] += goles_visitante
                    guardar_json(archivo)
                    return "Estadisticas actualizadas"
                    
    print("Equipo no encontrado")
    return "Actualizacion fallida"

def registrar_evento(id_partido,minuto,tipo,id_jugador,id_equipo):
    archivo = cargar_json()
    for partido in archivo["partido"]:
        if partido["id_partido"] == id_partido:
            if tipo.lower() not in ["gol", "tarjeta amarilla","tarjeta roja","sustitucion"]:
                print("Error no existe ese tipo")
                return "No se realizo el registro de evento"
            
            if not verificar_id_equipo(id_equipo):
                print("Este equipo no existe")
                return "Registro fallido"
            
            if not verificar_id_jugador(id_jugador):
                print("Este jugador no existe")
                return "Registro fallido"
            partido["eventos"] = {
                "minuto": minuto,
                "tipo": tipo,
                "id_jugador": id_jugador,
                "id_equipo": id_equipo
            }
            guardar_json(archivo)
            return "eventos actualizados"

if __name__ == "__main__":
    while True:
            print("Menu\n1.Registrar partido\n2.Actualizar resultado\n3.registrar evento\n4.Salir")
            opcion = input("Ingrese una opcion:")
            if opcion == "1":
                fecha=input("Ingrese la fecha del partido (dd-mm-yyyy):")
                if fecha == datetime.strptime(fecha,"%d-%m-%Y"):
                    pass
                else:
                    print ("Fecha incorrecta")
                id_arbitro=int(input("Ingrese el id del arbitro:"))
                equipo_local=int(input("Ingrese el id del equipo local:"))
                equipo_visitante=int(input("Ingrese el id del equipo visitante:"))
                goles_local=int(input("Ingrese goles del equipo local:"))
                goles_visitante=int(input("Ingrese goles del equipo visitante:"))
                registrar_partido(fecha,id_arbitro,equipo_local,equipo_visitante,goles_local,goles_visitante)
            elif opcion == "2":
                id_partido=input("Ingrese id del partido:")
                goles_local=input("Ingrese los goles del equipo local:")
                goles_visitante=input("Ingrese goles del equipo visitante:")
                respuesta = actualizar_estadisticas_equipo(id_partido,goles_local,goles_visitante)
            elif opcion == "3":
                id_partido=int(input("Ingrese id del partido:"))
                minuto=int(input("Ingresar minutos:"))
                tipo=input("Ingresar el tipo de evento:")
                id_jugador=int(input("Ingresar el id del jugador:"))
                id_equipo=int(input("Ingresar el id del equipo:"))
                respuesta = registrar_evento(id_partido,minuto,tipo,id_jugador,id_equipo)
            elif opcion == "4":
                print("fin de programa =)")
                break
            else:
                print("Opcion invalida")