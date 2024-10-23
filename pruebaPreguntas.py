rutaArchivo = "Programacion1ProyectoUADE/Files/preguntas.txt"
from triviaPreguntas import validarRespuesta
from funcionesGenericas import validarRespuesta
# Colores para impresión
yellow = '\x1b[33m'
blue = '\x1b[34m'
white = '\x1b[37m'
reset = '\x1b[0m'

def cargarPreguntas(rutaElegida):
    preguntas = {}
    opciones = []
    respuestasCorrectas = []
    try:
        archivoPreguntas = open(rutaElegida, 'r', encoding='utf-8')
        lines = archivoPreguntas.readlines()
        archivoPreguntas.close()

        for line in lines:
            partes = line.strip().split(';')
            numeroPregunta = int(partes[0].strip())
            pregunta = partes[1].strip()
            opcion = [option.strip() for option in partes[2].split(',')]
            respuestaCorrecta = int(partes[3].strip())
            
            preguntas[numeroPregunta] = {
                "pregunta": pregunta,
                "opciones": opcion,
                "respuestaCorrecta": respuestaCorrecta
            }
            
            opciones.append(opcion)
            respuestasCorrectas.append(respuestaCorrecta)

    except FileNotFoundError:
        print("Error: No se pudo encontrar el archivo de preguntas.")
    
    return preguntas, opciones, respuestasCorrectas

def agregarPregunta(rutaArchivo):
    preguntaEnArchivo = True
    while preguntaEnArchivo:
        print(yellow + "Agregar Nueva Pregunta:" + reset)
        pregunta = input("Ingrese la pregunta: ")

        preguntasExistentes = cargarPreguntas(rutaArchivo)[0]
        if pregunta in [p['pregunta'] for p in preguntasExistentes.values()]:
            print(f"{yellow}Error: La pregunta ya existe. Por favor, ingrese una nueva.{reset}")
            continue  # Volver a pedir la pregunta

        opciones = []
        for i in range(4):
            opcion = input(f"Ingrese la opción de respuesta {i + 1}: ")
            opciones.append(opcion)

        respuestaCorrecta = input("Ingrese el número de la opción correcta (1-4): ")
        while not (respuestaCorrecta.isdigit() and int(respuestaCorrecta) in [1, 2, 3, 4]):
            print(f"{yellow}Opción inválida. Debe ser un número entre 1 y 4.{reset}")
            respuestaCorrecta = input("Ingrese el número de la opción correcta (1-4): ")

        respuestaCorrecta = int(respuestaCorrecta) - 1
        archivoPreguntas = open(rutaArchivo, 'a', encoding='utf-8')
        numeroPregunta = obtenerNumeroPregunta(rutaArchivo)
        opcionesTexto = ','.join(opciones)

        archivoPreguntas.write(f"\n{numeroPregunta};{pregunta};{opcionesTexto};{respuestaCorrecta}")
        archivoPreguntas.close() 
        print(yellow + "Pregunta agregada con éxito." + reset)
        preguntaEnArchivo = False

def obtenerNumeroPregunta(rutaArchivo):
    try:
        archivoPreguntas = open(rutaArchivo, 'r', encoding='utf-8')
        lines = archivoPreguntas.readlines()
        archivoPreguntas.close()
        
        if lines:
            ultimoLinea = lines[-1].strip()
            return int(ultimoLinea.split(';')[0]) + 1
        else:
            return 1 
    except FileNotFoundError:
        return 1 

def main():
    # Cargo en el diccionario las preguntas existentes
    preguntas, opciones, respuestasCorrectas = cargarPreguntas(rutaArchivo)

    # Recorro 
    print("Preguntas cargadas:")
    for numero, pregunta in preguntas.items():
        print(f"{numero}: {pregunta['pregunta']}")
        for i, opcion in enumerate(pregunta['opciones']):
            print(f"   Opción {i + 1}: {opcion}")
        print(f"   Respuesta correcta: Opción {pregunta['respuestaCorrecta'] + 1}\n")

    #Agrego una pregunta
    agregarPregunta(rutaArchivo)


if __name__ == "__main__":
    main()
