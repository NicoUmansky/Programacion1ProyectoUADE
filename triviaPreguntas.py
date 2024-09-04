from colorama import Fore, init

def mostrarPregunta(pregunta, opciones):
    init()
    print(pregunta)
    for i in range(len(opciones)):
        print(Fore.WHITE + f"{i+1}. {opciones[i]}")

def obtenerRespuestaValida(opciones):
    init()
    while True:
        respuesta = input("Seleccione una opción (1-4): ")
        if respuesta.isdigit():
            respuesta = int(respuesta) - 1
            if 0 <= respuesta < len(opciones):
                return respuesta
            else:
                print(Fore.YELLOW +"Opción inválida. Por favor, seleccione un número entre 1 y 4.")
        else:
            print(Fore.YELLOW +"Entrada inválida. Por favor, ingrese un número entre 1 y 4.")

def jugarPreguntas(preguntas, opciones, respuestasCorrectas):
    vidas = 3
    puntuacion = 0

    for i in range(len(preguntas)):
        if vidas <= 0:
            return puntuacion

        mostrarPregunta(preguntas[i], opciones[i])
        respuestaUsuario = obtenerRespuestaValida(opciones[i])
        
        if respuestaUsuario == respuestasCorrectas[i]:
            print(Fore.GREEN + "¡Respuesta correcta!")
            puntuacion += 1
        else:
            print(Fore.BLUE +"Respuesta incorrecta.")
            vidas -= 1
            print(Fore.RED + f"Te quedan {vidas} vidas.")

    return puntuacion
