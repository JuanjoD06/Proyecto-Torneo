from gestor_equipos import registrar_equipo, buscar_equipo, actualizar_estadisticas_equipo
from gestor_jugadores import registrar_jugador,buscar_jugador,actualizar_estadisticas_jugador


while True:
    print('''Ingrese una opcion
          Opcion1: Registrar equipo
          Opcion2: Buscar equipo
          Opcion3:Actualizar estadisticas de equipo
          Opcion4: Registrar jugador
          Opcion5: Buscar un jugador
          ''')
    opcion = int(input("Ingrese la opcion que requiera:"))

    if opcion == 1:
            nombre = input("Ingrese nombre de equipo")
            ciudad = input("Ingrese la ciudad del equipo")
            dt = input("Ingrese el nombre del tecnico")
            respuesta = registrar_equipo(id,nombre,ciudad,dt)
            print(respuesta)
    elif opcion == 2:
            key = input("ingrese parametro para buscar (nombre,ciudad,dt)")
            respuesta = buscar_equipo(key)
            print(respuesta)
    elif opcion == 3:
            puntos=input("ingrese puntos del equipo")
            partidos_jugados=input("Ingrese los partidos que han jugados")
            ganados=input("Ingrese los partidos ganados del equipo")
            empatados=input("Ingrese los partidos empatados del equipo")
            perdidos=input("Ingrese los partidos perdidos del equipo")
            goles_favor=input("Ingrese los goles a favor")
            goles_contra=input("Ingrese los goles en contra")
            respuesta=actualizar_estadisticas_equipo(puntos,partidos_jugados,ganados,empatados,perdidos,goles_favor,goles_contra)
            print(respuesta)
    elif opcion == 4:
        nombre = input("Ingrese nombre del jugador")
        numero = input("Ingrese numero del jugador")
        posicion = input("Ingrese la posicion del jugador")
        respuesta = registrar_jugador(nombre,numero,posicion)
        print(respuesta)
    elif opcion == 5:
            break
    else:
            print("opcion incorrecta")

