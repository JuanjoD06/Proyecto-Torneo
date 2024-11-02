import json
import sys

def registrar_jugador(nombre,numero,posicion):
    with open("gestor_jugadores.json","r") as file:#se abre el archivo en modo lectura"r"
        archivo=json.load(file)#se convierte el archivo json en un diccionario de python

    for jugadores in archivo["jugador"]:
        if jugadores["nombre"].lower() == nombre.lower():
            print("jugador ya esta registrado")
            return
    jugador_nuevo = {
        "id": id +1,
        "nombre":nombre,
        "numero":numero,
        "posicion":posicion
            }
    archivo["jugador"].append(jugador_nuevo)
    with open("registros.json","w") as file:#se abre el archivo en modo escritura"w"
        json.dump(archivo,file,indent=4)#se carga el contenido en json y se guarda en el archivo
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
    archivo["estadisticas_jugador"]["goles"] += asistencias
    archivo["estadisticas_jugador"]["asistencias"] += asistencias
    archivo["estadisticas_jugador"]["tarjetas_amarillas"] += tarjetas_amarillas
    archivo["estadisticas_jugador"]["tarjetas_rojas"] += tarjetas_rojas
    archivo["estadisticas_jugador"]["minutos_jugados"] += minutos_jugados

    with open("registros.json","w") as file:
        json.dump(archivo,file,indent=4)
        print("estadisticas de jugador actualizadas")