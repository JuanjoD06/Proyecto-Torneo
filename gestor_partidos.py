import json
import datetime



def registrar_partido(fecha,equipo_local,equipo_visitante):
    archivo = cargar_json("gestor_partidos.json")
    for partidos in archivo["fecha"]:
        if partidos["fecha"] == fecha:
            print("jugador ya esta registrado")
            return
        id = id + 1
    partido_nuevo = {
        "id": id,
        "equipo_local":0,
        "equipo_visitante":0
            }
    archivo["jugador"].append(jugador_nuevo)
    
    print("jugador registrado")

def buscar_jugador(key,value):
    with open("equipos.json","r") as file:
        archivo=json.load(file)
    
    for jugador in archivo:
        if jugador.get(key).lower() == value.lower():
            return jugador

def actualizar_estadisticas_jugador(partidos,goles,asistencias,tarjetas_amarillas,tarjetas_rojas,minutos_jugados):
    with open("gestor_jugadores.json","r") as file:
        archivo=json.load(file)
    
    archivo["estadisticas_jugador"]["partidos"] += partidos
    archivo["estadisticas_jugador"]["goles"] += goles
    archivo["estadisticas_jugador"]["asistencias"] += asistencias
    archivo["estadisticas_jugador"]["tarjetas_amarillas"] += tarjetas_amarillas
    archivo["estadisticas_jugador"]["tarjetas_rojas"] += tarjetas_rojas
    archivo["estadisticas_jugador"]["minutos_jugados"] += minutos_jugados

    