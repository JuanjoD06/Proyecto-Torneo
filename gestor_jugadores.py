import json

def cargar_json():
    with open("gestor_jugadores.json","r") as file:#se abre el archivo en modo lectura"r"
        return json.load(file)#se convierte el archivo json en un diccionario de python

def guardar_json(archivo):
    with open("gestor_jugadores.json","w") as file:#se abre el archivo en modo escritura"w"
        json.dump(archivo,file,indent=4)#se carga el contenido en json y se guarda en el archivo

def verificar_id_equipo(id_equipo):
    with open("gestor_equipos.json", "r")as file:
        equipos = json.load(file)
        for equipo in equipos["equipo"]:
            if equipo["id_equipo"] == int(id_equipo):
                return True
        return False
            
def registrar_jugador(nombre,numero,posicion,equipo_id):
    archivo = cargar_json()

    if not verificar_id_equipo(equipo_id):
        print("error no existe equipo")
        return "No se realizo el registro"
    
    for jugador in archivo.get("jugador",[]):
        if jugador["numero"] == numero and jugador["equipo_id"] == equipo_id:
            print("Error ya hay otro jugador con ese numero en el mismo equipo")
            return "No se realizo el registro"
        
    if posicion.lower() not in ["delantero", "mediocampista","defensa","portero"]:
        print("Error no existe esa posicion")
        return "No se realizo el registro"

    id_archivo = 0
    for jugador in archivo["jugador"]:
        id_actual = jugador["id_jugador"]
        if id_actual > id_archivo:
            id_archivo = id_actual
    id_nuevo = id_archivo + 1

    jugador_nuevo = {
            "id_jugador": id_nuevo,
            "nombre":nombre,
            "numero":numero,
            "posicion":posicion,
            "equipo_id":equipo_id,
            "estadisticas_jugador":
            {
                "partidos":0,
                "goles":0,
                "asistencias":0,
                "tarjetas_amarillas":0,
                "tarjetas_rojas":0,
                "minutos_jugados":0
            }
    }

    archivo["jugador"].append(jugador_nuevo)
    guardar_json(archivo)
    print("jugador registrado")
    return "Se ha registrado correctamente"
def buscar_jugador(key,value):
    archivo=cargar_json()
    encontrado = False
    for jugador in archivo.get("jugador",[]):
        if jugador.get(key,"").lower() == value.lower():
            encontrado = True
            return jugador
        if not encontrado:
            print("jugador no encontrado")
            return None
def actualizar_estadisticas_equipo(id_jugador,partidos,goles,asistencias,tarjetas_amarillas,tarjetas_rojas,minutos_jugados):
    archivo = cargar_json()
    for jugador in archivo["jugador"]:
        if jugador["id_jugador"] == int(id_jugador):
            if partidos < 0 or goles < 0 or asistencias < 0 or tarjetas_amarillas < 0 or tarjetas_rojas < 0 or minutos_jugados < 0:
                print("error no puede ingresar un numero menor a 0")
                return "No se actualizo el registro"
            else:
                jugador["estadisticas_jugador"]["partidos"] += partidos
                jugador["estadisticas_jugador"]["goles"] += goles
                jugador["estadisticas_jugador"]["asistencias"] += asistencias
                jugador["estadisticas_jugador"]["tarjetas_amarillas"] += tarjetas_amarillas
                jugador["estadisticas_jugador"]["tarjetas_rojas"] += tarjetas_rojas
                jugador["estadisticas_jugador"]["minutos_jugados"] += minutos_jugados

            guardar_json(archivo)
            return "Estadisticas actualizadas"
    print("Equipo no encontrado")
    return "No se actualizo el registro"

if __name__ == "__main__":
      while True:
            print("Menu\n1.Registrar jugador\n2.Buscar jugador\n3.Actualizar estadisticas\n4.Salir")
            opcion = input("Ingrese una opcion:")
            if opcion == "1":
                nombre=input("Ingrese nombre de jugador:")
                numero=int(input("Ingrese el numero del jugador:"))
                posicion=input("Ingrese la posicion del jugador:")
                equipo_id=int(input("Ingrese el id del equipo:"))
                respuesta = registrar_jugador(nombre,numero,posicion,equipo_id)
                if not (nombre and posicion and numero is not None and equipo_id is not None):
                    print ("No puede haber campos vacios")
                else:
                    print("")
            elif opcion == "2":
                key=input("Ingrese el valor de busqueda:")
                value=input("Ingrese el valor a buscar:")
                resultado=buscar_jugador(key,value)
                if resultado:
                    print(resultado)
                else:
                    print("jugador no encontrado")
            elif opcion == "3":
                id_jugador=int(input("Ingrese el id del jugador para actualizar sus estadisticas:"))
                partidos=int(input("Ingresar numero de partidos:"))
                goles=int(input("Ingresar numero de goles:"))
                asistencias=int(input("Ingresar numero de asistencias:"))
                tarjetas_amarillas=int(input("Ingresar numero de tarjetas amarillas:"))
                tarjetas_rojas=int(input("Ingresar numero de tarjetas rojas:"))
                minutos_jugados=int(input("Ingresar numero de minutos jugados:"))
                respuesta=actualizar_estadisticas_equipo(id_jugador,partidos,goles,asistencias,tarjetas_amarillas,tarjetas_rojas,minutos_jugados)
            elif opcion == "4":
                print("fin de programa =)")
                break
            else:
                print("Opcion invalida")




    