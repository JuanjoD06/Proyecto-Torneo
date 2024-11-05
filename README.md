Juan Jose Duque Castro 

Instrucciones de ejecución:
1.Clonar el repositorio
2.Importar las bibliotecas necesarias, en este caso (json,datetime) no es necesario instalar nada ya que vienen por defecto en el lenguaje python
3.Usar todos los archivos en un mismo directorio para que no hayan errores de ejecución
4.Cada archivo tiene su interfaz por medio de consola para acceder a la funcionalidades del proyecto
5.Sigue las intrucciones según las opciones de cada archivo.py

Estructura del proyecto:
gestor_equipos.py:Archivo que tiene la logica para ejecutar las funcionalidades del proyecto
gestor_equipos.json:Archivo que contiene y donde se guardan la información de los equipos
ciudades_colombia.json:Archivo que contiene todas las ciudades de colombia
gestor_jugadores.py:
gestor_jugadores.json:
gestor_partidos.py:
gestor_partidos.json:
gestor_arbitros.py:
gestor_arbitros.json:

Explicación de funcionalidades implementadas
1.Registro de: [equipos,jugadores,partidos,arbitros]

2.Busqueda de: [equipos,jugadores,partidos]

3.Actualización de estadísticas de: [equipos,jugadores,partidos]

4.Guardar información de cada archivo .py en su respectivo archivo .json

5.Se implementan algunas validaciones obligatorias que se deben de cumplir para poder interactuar de forma eficiente con el programa. Las validaciones son las siguientes:

    1.Para gestor de equipos: *No pueden existir dos equipos con el mismo nombre
    *La ciudad debe ser una ciudad válida de Colombia
    *El equipo debe de tener todos sus datos básicos
    *Las estadisticas no pueden tener numeros negativos

    2.Para gestor de jugadores: *No pueden existir dos jugadores con el mismo número en el mismo equipo
    *La posición debe ser válida (por ejemplo: Delantero, Mediocampista, Defensa,
    Portero)
    *El jugador debe tener todos sus datos básicos
    *Las estadísticas no pueden tener números negativos
    *El equipo al que se asigna el jugador debe existir

    3.Para gestor de partidos: *No pueden existir dos partidos con la misma fecha y los mismos equipos
    *Los equipos local y visitante deben existir y ser diferentes
    *Los goles no pueden ser números negativos
    *Los tipos de eventos deben ser válidos (por ejemplo: gol, tarjeta amarilla,
    tarjeta roja, sustitución)
    *Los jugadores y equipos en los eventos deben existir y corresponder a los
    equipos del partido

    4.Para gestor de arbitros: *No pueden existir dos árbitros con el mismo nombre
    *La categoría debe ser válida (por ejemplo: FIFA, Nacional, Regional)
    *La experiencia debe ser un número positivo
    *Un árbitro no puede ser asignado a dos partidos en la misma fecha

6.Se manejan 2 funciones claves para entender como cargar y guardar en los archivos json llamadas (cargar_json) (guardar_json)

Conceptos utilizados:
*Listas, Tuplas y Diccionarios
*Manejo de archivos JSON
*Funciones y modularización
*Manejo de excepciones
*Estructuras de control
*Manipulación de strings