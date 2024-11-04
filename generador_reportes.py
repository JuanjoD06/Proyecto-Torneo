import json

def cargar_json():
    with open("gestor_equipos.json","r", encoding="utf-8") as file:#se abre el archivo en modo lectura"r"
        return json.load(file)#se convierte el archivo json en un diccionario de python
    
def guardar_json(archivo):
    with open("tabla_posiciones.json","w") as file:#se abre el archivo en modo escritura"w"
        json.dump({"equipos": archivo}, file,indent=4)#se carga el contenido en json y se guarda en el archivo

def generar_tabla_posiciones():
    archivo = cargar_json()
    equipos=archivo["partido"]

    for i in range(archivo(len(equipos))):
        for j in range(archivo(len(equipos)) - 1):
            if equipos[j]["estadisticas_equipo"]["ganados"] < equipos [j+1]["estadisticas_equipo"]["ganados"]:
                equipos[j], equipos[j+1] = equipos[j+1], equipos[j]
    guardar_json(equipos)
            
        

    

            
