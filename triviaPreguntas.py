from penales import penal, atajar
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
        
    except FileNotFoundError:
        print("¡Error! No se encontro el archivo con las preguntas")
        return preguntas, opciones, respuestasCorrectas
    except IOError:
        print("¡Error! No se pudo leer el archivo de preguntas")
        return preguntas, opciones, respuestasCorrectas

    for linea in lineas:
        partes = linea.strip().split(';')
        if len(partes) < 4:
            print(f"Error en la línea '{linea.strip()}' ya que no tiene el formato correcto.")
            continue
        
        numeroPregunta = int(partes[0].strip())
        pregunta = partes[1].strip()
        opcion = [opcion.strip() for opcion in partes[2].split(',')]
        
        try:
            respuestaCorrecta = int(partes[3].strip())
            if respuestaCorrecta < 0 or respuestaCorrecta >= len(opcion):
                print(f"¡Error! El índice de respuesta correcta para la pregunta '{pregunta}' está fuera de rango.")
                continue
            
            preguntas[numeroPregunta] = {
                "pregunta": pregunta,
                "opciones": opcion,
                "respuestaCorrecta": respuestaCorrecta
            }
            opciones.append(opcion)
            respuestasCorrectas.append(respuestaCorrecta)

        except ValueError:
            print(f"Error en la línea '{linea.strip()}': respuesta correcta inválida.")

    return preguntas, opciones, respuestasCorrectas

def agregarPregunta(rutaElegida):
    preguntas, opciones, respuestasCorrectas = cargarPreguntas(rutaElegida)

    if not preguntas:
        print("No se pueden agregar preguntas hasta que se carguen preguntas válidas.")
        return

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

    try:
        archivoPreguntas = open(rutaElegida, 'at', encoding='utf-8')
        numeroPregunta = obtenerNumeroPregunta(rutaElegida)
        opcionesTexto = ','.join(opciones)
        archivoPreguntas.write(f"{numeroPregunta};{pregunta};{opcionesTexto};{respuestaCorrecta}\n")
        archivoPreguntas.close() 
        print(yellow + "¡Pregunta agregada exitosamente!" + reset)

    except IOError:
        print("Error: No se pudo escribir en el archivo de las preguntas")

def obtenerNumeroPregunta(rutaElegida):
    try:
        archivoPreguntas = open(rutaElegida, 'r', encoding='utf-8')
        lineas = archivoPreguntas.readlines()
        archivoPreguntas.close()

        if lineas:
            ultimoLinea = lineas[-1].strip()
            return int(ultimoLinea.split(';')[0]) + 1
        else:
            return 1  # Si el archivo está vacío, se puede agregar la pregunta que sería la 1
        
    except FileNotFoundError:
        print("¡Error! No se encontró el archivo de las pregunta.")
    except IOError:
        print("¡Error! No se pudo leer el archivo de preguntas")

def mostrarPregunta(pregunta, opciones):
    print(f"{green}{pregunta}{reset}")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{white}{i}. {opcion}{reset}")
    

validarRespuesta = lambda respuesta: respuesta.isdigit() and respuesta in ['1', '2', '3', '4']

def jugarPreguntas(preguntas, opciones, indiceCorrectas, equipo):
    respuestasCorrectas = 0
    respuestasIncorrectas = 0
    penalesAcertados = 0
    penalesPateados = 0
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
            efectividadPenales = (penalesAcertados/penalesPateados) * 100
            return puntuacion, respuestasCorrectas, respuestasTotales, efectividad, penalesPateados, penalesAcertados, efectividadPenales
        
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
                penalesPateados += 1
                penalesAcertados += 1
            else:
                penalesPateados += 1
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
            print(green + "La respuesta correcta era: " + white + preguntas[indiceElegido]["opciones"][preguntas[indiceElegido]["respuestaCorrecta"]] + reset)
            vidas -= 1
            respuestasIncorrectas += 1
            print(f"{red}Te quedan {vidas} vidas.{reset}")
            print("\n")

        
    respuestasTotales = respuestasCorrectas + respuestasIncorrectas
    if respuestasTotales == 0:
        efectividad = 0
        efectividadPenales = 0
    else:
        efectividad = (respuestasCorrectas/respuestasTotales) * 100
        efectividadPenales = (penalesAcertados/penalesPateados) * 100

    return puntuacion, respuestasCorrectas, respuestasTotales, efectividad, penalesPateados, penalesAcertados, efectividadPenales
