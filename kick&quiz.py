from triviaPreguntas import jugarPreguntas
from ranking import mostrarRanking, actualizarRanking, puntuaciones
from inicioSesion import inicioSesion
import random

# Colores usando código ANSI
cyan = '\x1b[36m'
yellow = '\x1b[33m'
white = '\x1b[37m'
green = '\x1b[32m'
red = '\x1b[31m'
blue = '\x1b[34m'
reset = '\x1b[0m'

def mostrarMenu():
    print(cyan + "Menú Principal:")
    print(yellow + "1. Jugar")
    print(yellow + "2. Ver Ranking")
    print(yellow + "3. Salir")
    opcion = input(white + "Seleccione una opción (1, 2 o 3): ")
    return opcion

def cargarPreguntas(rutaArchivo):
    preguntas = {}
    opciones = []
    respuestasCorrectas = []
    try:
        file = open(rutaArchivo, 'r', encoding='utf-8')
        lines = file.readlines()
        file.close()

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

def main():
    rutaArchivo = "Programacion1ProyectoUADE/Files/preguntas.txt" 

    continuar = True
    
    while continuar:
        opcion = mostrarMenu()
        
        if opcion == '1':
            print(red + "¡Bienvenido a Trivia Argentina!")
            print(yellow + "Por favor, ingrese a su cuenta o regístrese para empezar a jugar.")
            
            cambiarUsuario = True
            while cambiarUsuario:
                nombreUsuario, equipo = inicioSesion()
                usuarioEnRanking = any(usuario[0] == nombreUsuario for usuario in puntuaciones)
                
                if usuarioEnRanking:
                    print(red + "Ya jugaste y estás en el ranking. Por favor, inicia sesión con otro usuario.")
                else:
                    cambiarUsuario = False 

            print(blue + "¡Empecemos a jugar!")
            print(red + "Tienes 3 vidas disponibles. ¡Aprovechalas! ❤️  ❤️  ❤️" + reset)
            
            preguntas, opciones, respuestasCorrectas = cargarPreguntas(rutaArchivo)

            puntuacionFinal = jugarPreguntas(preguntas, opciones, respuestasCorrectas, equipo)
            print(green + f"Juego terminado. Tu puntuación final es {puntuacionFinal}.")

            actualizarRanking(nombreUsuario, puntuacionFinal)

            cambiarUsuario = input(white + "¿Quieres cambiar de usuario para intentar de nuevo? Ingresá SI para cambiar, o presioná cualquier tecla para salir: ").upper()
            if cambiarUsuario != 'SI':
                print(red + "¡Muchas gracias por jugar! Te esperamos nuevamente.")
                continuar = False

if __name__ == "__main__":
    main()
