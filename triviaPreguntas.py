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

def mostrarPregunta(pregunta, opciones):
    print(pregunta)
    for i in range(len(opciones)):
        print(f"{white}{i+1}. {opciones[i]}{reset}")

validarRespuesta = lambda respuesta: respuesta.isdigit() and respuesta in ['1','2','3','4']    

def jugarPreguntas(preguntas, opciones, respuestasCorrectas,equipo):
    vidas = 3
    puntuacion = 0
    preguntasHechas = []
    
    while len(preguntasHechas) < len(preguntas):
        # Crear una lista de índices no usados
        indicesDisponibles = [i for i in range(len(preguntas)) if i not in preguntasHechas]
        # Elegir un índice de las preguntas no usadas utilizando slicing
        indiceElegido = random.choice(indicesDisponibles[:])
        preguntasHechas.append(indiceElegido)
        
        if vidas <= 0:
            return puntuacion
        mostrarPregunta(preguntas[indiceElegido], opciones[indiceElegido])
        respuestaUsuario = input("Seleccione una opción (1-4): ")
        
        while not validarRespuesta(respuestaUsuario):
            print(f"{yellow}Opción inválida. Por favor, seleccione un número entre 1 y 4.{reset}")
            respuestaUsuario = input("Seleccione una opción (1-4): ")
        
        if (int(respuestaUsuario) -1 ) == respuestasCorrectas[indiceElegido]:
            print(f"{green}¡Respuesta correcta!{reset}")
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
            print(f"{red}Te quedan {vidas} vidas.{reset}")

    return puntuacion
    
