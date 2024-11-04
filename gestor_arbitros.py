import json
from datetime import datetime

def cargar_json_partido():
    with open("gestor_partidos.json","r", encoding="utf-8") as file:#se abre el archivo en modo lectura"r"
        return json.load(file)#se convierte el archivo json en un diccionario de python
    
def cargar_json():
    with open("gestor_arbitros.json","r", encoding="utf-8") as file:#se abre el archivo en modo lectura"r"
        return json.load(file)#se convierte el archivo json en un diccionario de python

def guardar_json(archivo):
    with open("gestor_arbitros.json","w") as file:#se abre el archivo en modo escritura"w"
        json.dump(archivo,file,indent=4)#se carga el contenido en json y se guarda en el archivo

def verificar_id_equipo(id_partido):
    with open("gestor_equipos.json", "r")as file:
        partidos = json.load(file)
        for partido in partidos["partido"]:
            if partido["id_partido"] == int(id_partido):
                return True
        return False

def registrar_arbitro(nombre,experiencia,categoria,partidos_dirigidos):
    archivo = cargar_json()

    for arbitro in archivo.get("arbitro",[]):
        if arbitro["nombre"].lower() == nombre.lower():
            print("arbitro ya esta registrado")
            return "Registro Fallido"
    if categoria.lower() not in ["fifa", "nacional","regional"]:
        print("Error no existe la categoria")
        return "Registro Fallido"
    if int(experiencia) < 0:
        print("Error el numero de experiencia no puede ser menor a 0")
        return "Registro Fallido"


    id_archivo = 0
    for arbitro in archivo["arbitro"]:
        id_actual = arbitro["id_arbitro"]
        if id_actual > id_archivo:
            id_archivo = id_actual
    id_nuevo = id_archivo + 1

    arbitro_nuevo = {
            "id_arbitro":id_nuevo,
            "nombre":nombre,
            "experiencia":experiencia,
            "categoria":categoria,
            "partidos_dirigidos":partidos_dirigidos
    }

    archivo["arbitro"].append(arbitro_nuevo)
    guardar_json(archivo)
    print("arbitro registrado")

def asignar_arbitro(id_partido,id_arbitro,fecha_asignacion):
    archivo=cargar_json_partido()
    if not verificar_id_equipo(id_partido):
        print("partido no existe")
        return "No se asigno arbitro"
    for arbitro in archivo["partido"]:
        if arbitro["id_arbitro"] == int(id_arbitro) and arbitro["fecha"] == fecha_asignacion:
            print("Ya hay un arbitro asignado en esta fecha")
            return "asignacion fallida"
        
    

if __name__ == "__main__":
        while True:
            print("Menu\n1.Registrar arbitro\n2.Asignar arbitro a un partido\n3.Salir")
            opcion = input("Ingrese una opcion:")
            if opcion == "1":
                nombre=input("Ingrese nombre del arbitro:")
                experiencia=int(input("Ingrese la experiencia:"))
                categoria=input("Ingrese la categoria:")
                partidos_dirigidos=int(input("Ingrese los partidos dirigidos "))
                respuesta = registrar_arbitro(nombre,experiencia,categoria,partidos_dirigidos)
                    
            elif opcion == "2":
                id_partido=int(input("Ingrese el id del partido:"))
                id_arbitro=int(input("Ingrese el id del arbitro:"))
                fecha_asignacion=input("Ingrese fecha de asignacion:")
                asignar_arbitro(id_partido,id_arbitro,fecha_asignacion)
            elif opcion == "3":
                print("Fin del programa =)")
                break
            else:
                print("Opcion invalida")


    