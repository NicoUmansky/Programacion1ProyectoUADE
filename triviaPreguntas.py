from Penales import penal, atajar
import random

# Colores usando código ANSI
cyan = '\x1b[36m'
yellow = '\x1b[33m'
white = '\x1b[37m'
green = '\x1b[32m'
red = '\x1b[31m'
blue = '\x1b[34m'
reset = '\x1b[0m'

def cargarPreguntas(rutaElegida):
    preguntas = {}
    opciones = []
    respuestasCorrectas = []
    try:
        archivoPreguntas = open(rutaElegida, 'r', encoding='utf-8')
        lineas = archivoPreguntas.readlines()
        archivoPreguntas.close()

        for linea in lineas:
            partes = linea.strip().split(';')
            numeroPregunta = int(partes[0].strip())
            pregunta = partes[1].strip()
            opcion = [opcion.strip() for opcion in partes[2].split(',')]
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

def agregarPregunta(rutaElegida):
    
        print(yellow + "Agregar Nueva Pregunta:" + reset)
        pregunta = input("Ingrese la pregunta: ")
    
        opciones = []
        for i in range(4):
            opcion = input(f"Ingrese la opción de respuesta {i + 1}: ")
            opciones.append(opcion)

        respuestaCorrecta = input("Ingrese el número de la opción correcta (1-4): ")
        while not (respuestaCorrecta.isdigit() and int(respuestaCorrecta) in [1, 2, 3, 4]):
            print(f"{yellow}Opción inválida. Debe ser un número entre 1 y 4.{reset}")
            respuestaCorrecta = input("Ingrese el número de la opción correcta (1-4): ")

        respuestaCorrecta = int(respuestaCorrecta) - 1
        archivoPreguntas = open(rutaElegida, 'a', encoding='utf-8')
        numeroPregunta = obtenerNumeroPregunta(rutaElegida)
        opcionesTexto = ','.join(opciones)

        archivoPreguntas.write(f"{numeroPregunta};{pregunta};{opcionesTexto};{respuestaCorrecta}\n")
        archivoPreguntas.close() 
        print(yellow + "¡Pregunta agregada exitosamente!" + reset)

def obtenerNumeroPregunta(rutaElegida):
    #Consigo el numero de la ultima pregunta para asignarle el siguiente numero a la que estoy creando
    try:
        archivoPreguntas = open(rutaElegida, 'r', encoding='utf-8')
        lineas = archivoPreguntas.readlines()
        archivoPreguntas.close()
        if lineas:
            ultimoLinea = lineas[-1].strip()
            return int(ultimoLinea.split(';')[0]) + 1
        else:
            return 1 #Si el archivo esta vacio porque no hay preguntas, le asigno el indice 1
        
    except FileNotFoundError:
        print("Error: No se pudo encontrar el archivo de preguntas.")
        return 0
    
def mostrarPregunta(pregunta, opciones):
    print(f"{green}{pregunta}{reset}")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{white}{i}. {opcion}{reset}")

validarRespuesta = lambda respuesta: respuesta.isdigit() and respuesta in ['1', '2', '3', '4']

def jugarPreguntas(preguntas, opciones, indiceCorrectas, equipo):
    respuestasCorrectas = 0
    respuestasIncorrectas = 0
    vidas = 3
    puntuacion = 0
    efectividad = 0
    preguntasHechas = []
    
    while len(preguntasHechas) < len(preguntas):
        indicesDisponibles = [i for i in range(len(preguntas)) if i not in preguntasHechas]
        indiceElegido = random.choice(indicesDisponibles)
        preguntasHechas.append(indiceElegido)
        
        if vidas <= 0:
            respuestasTotales = respuestasCorrectas + respuestasIncorrectas
            efectividad = (respuestasCorrectas/respuestasTotales) * 100
            return puntuacion, respuestasCorrectas, respuestasTotales, efectividad
        
        mostrarPregunta(preguntas[indiceElegido]["pregunta"], preguntas[indiceElegido]["opciones"])
        respuestaUsuario = input("Seleccione una opción (1-4): ")
        
        while not validarRespuesta(respuestaUsuario):
            print(f"{yellow}Opción inválida. Por favor, seleccione un número entre 1 y 4.{reset}")
            respuestaUsuario = input("Seleccione una opción (1-4): ")
        
        if (int(respuestaUsuario) - 1) == preguntas[indiceElegido]["respuestaCorrecta"]:
            print(f"{green}¡Respuesta correcta!{reset}")
            respuestasCorrectas += 1
            puntuacion += 2
            gol = penal(equipo)
            if gol:
                puntuacion += 1
            input(f"{white}Presiona cualquier botón para continuar: {reset}")
            atajado = atajar(equipo)
            if atajado:
                puntuacion += 1
            else:
                puntuacion -= 1
            print(f"{green}Tu puntuación hasta el momento es de {puntuacion}.{reset}")
            input(f"{white}Presiona cualquier botón para continuar con las preguntas: {reset}")
        
        else:
            print(f"{blue}Respuesta incorrecta.{reset}")
            vidas -= 1
            respuestasIncorrectas += 1
            print(f"{red}Te quedan {vidas} vidas.{reset}")
        
    respuestasTotales = respuestasCorrectas + respuestasIncorrectas
    if respuestasTotales == 0:
        efectividad = 0
    else:
        efectividad = (respuestasCorrectas/respuestasTotales) * 100

    print(puntuacion)
    print(respuestasCorrectas)
    print(respuestasTotales)
    print(efectividad)
    return puntuacion, respuestasCorrectas, respuestasTotales, efectividad
