from Penales import penal, atajar
import random
def mostrarPregunta(pregunta, opciones):
    print(pregunta)
    for i in range(len(opciones)):
        print(f"\033[1;37m{i+1}. {opciones[i]}\033[0m")

def obtenerRespuestaValida(opciones):
    while True:
        respuesta = input("Seleccione una opción (1-4): ")
        if respuesta.isdigit():
            respuesta = int(respuesta) - 1
            if 0 <= respuesta < len(opciones):
                return respuesta
            else:
                print("\033[1;33mOpción inválida. Por favor, seleccione un número entre 1 y 4.\033[0m")
        else:
            print("\033[1;33mEntrada inválida. Por favor, ingrese un número entre 1 y 4.\033[0m")

def jugarPreguntas(preguntas, opciones, respuestasCorrectas):
    vidas = 3
    puntuacion = 0

    # for i in range(len(preguntas)):
    #     if vidas <= 0:
    #         return puntuacion

    #     mostrarPregunta(preguntas[i], opciones[i])
    #     respuestaUsuario = obtenerRespuestaValida(opciones[i])
        
    #     if respuestaUsuario == respuestasCorrectas[i]:
    #         print("\033[1;32m¡Respuesta correcta!\033[0m")
    #         puntuacion += 2
    #         Gol = penal()
    #         if Gol == True:
    #             puntuacion += 1
    #         input("\033[0;37m"+"Presiona cualquier botón para continuar: ")
    #         Atjar = atajar()
    #         if Atjar == True:
    #             puntuacion += 1
    #         else:
    #             puntuacion -= 1
    #         print(f"\033[1;32mTu puntuación hasta el momento es de {puntuacion}.\033[0m")
    #         int(input("\033[0;37m"+"Presiona cualquier botón para continuar con las preguntas: "))
        
    #     else:
    #         print("\033[1;34mRespuesta incorrecta.\033[0m")
    #         vidas -= 1
    #         print(f"\033[1;31mTe quedan {vidas} vidas.\033[0m")
    preguntasHechas = []
    while len(preguntasHechas) < len(preguntas):
        indiceElegido = random.randint(0,len(preguntas)-1)
        while indiceElegido in preguntasHechas:
            indiceElegido = random.randint(0,len(preguntas)-1)
        preguntasHechas.append(indiceElegido)
        if vidas <= 0:
            return puntuacion

        mostrarPregunta(preguntas[indiceElegido], opciones[indiceElegido])
        respuestaUsuario = obtenerRespuestaValida(opciones[indiceElegido])
        
        if respuestaUsuario == respuestasCorrectas[indiceElegido]:
            print("\033[1;32m¡Respuesta correcta!\033[0m")
            puntuacion += 2
            Gol = penal()
            if Gol == True:
                puntuacion += 1
            input("\033[0;37m"+"Presiona cualquier botón para continuar: ")
            Atjar = atajar()
            if Atjar == True:
                puntuacion += 1
            else:
                puntuacion -= 1
            print(f"\033[1;32mTu puntuación hasta el momento es de {puntuacion}.\033[0m")
            input("\033[0;37m"+"Presiona cualquier botón para continuar con las preguntas: ")
        
        else:
            print("\033[1;34mRespuesta incorrecta.\033[0m")
            vidas -= 1
            print(f"\033[1;31mTe quedan {vidas} vidas.\033[0m")



    return puntuacion

