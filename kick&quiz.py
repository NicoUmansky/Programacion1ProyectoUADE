rutaArchivo1 = "Programacion1ProyectoUADE/Files/preguntas.txt" 
rutaArchivo2 = "Files\preguntas.txt"

rutaElegida = rutaArchivo1

from triviaPreguntas import jugarPreguntas, agregarPregunta, cargarPreguntas, obtenerNumeroPregunta
from ranking import mostrarRanking, actualizarRanking, puntuaciones
from inicioSesion import inicioSesion
from estadisticas import calcularEstadisticas
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
    print(yellow + "3. ¡Agregar Pregunta!")
    print(yellow + "4. Salir")
    opcion = input(white + "Seleccione una opción (1, 2, 3 o 4): ")
    return opcion


def main():

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
            
            preguntas, opciones, indiceCorrectas = cargarPreguntas(rutaElegida)

            puntuacionFinal, respuestasCorrectas, respuestasTotales, efectividad = jugarPreguntas(preguntas, opciones, indiceCorrectas, equipo)
            print(green + f"Juego terminado. Tu puntuación final es {puntuacionFinal}.")
            calcularEstadisticas(nombreUsuario, respuestasTotales, respuestasCorrectas, puntuacionFinal, efectividad)

            actualizarRanking(nombreUsuario, puntuacionFinal)

            cambiarUsuario = input(white + "¿Quieres cambiar de usuario para intentar de nuevo? Ingresá SI para cambiar, o presioná cualquier tecla para salir: ").upper()
            if cambiarUsuario != 'SI':
                print(red + "¡Muchas gracias por jugar! Te esperamos nuevamente.")
                continuar = False
                
        elif opcion == '2':
            mostrarRanking()
    
        elif opcion == '3': 
            agregarPregunta(rutaElegida)
            
        elif opcion == '4': 
            print(red + "¡Muchas gracias por jugar! Te esperamos nuevamente.")
            continuar = False
    
        else:
            print(red + "Opción inválida. Por favor, selecciona 1, 2 o 3.")

if __name__ == "__main__":
    main()
