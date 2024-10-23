rutaArchivo1 = "Programacion1ProyectoUADE/Files/preguntas.txt" 
rutaArchivo2 = "Files\preguntas.txt"

rutaElegida = rutaArchivo1

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
    print(yellow + "3. ¡Agregar Pregunta!")
    print(yellow + "4. Salir")
    opcion = input(white + "Seleccione una opción (1, 2, 3 o 4): ")
    return opcion

def cargarPreguntas(rutaElegida):
    preguntas = {}
    opciones = []
    respuestasCorrectas = []
    try:
        file = open(rutaElegida, 'r', encoding='utf-8')
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

#NUEVO DE AGREGAR PREGUNTAS
def agregarPregunta(rutaArchivo):
    print(cyan + "Agregar Nueva Pregunta:" + reset)
    pregunta = input("Ingrese la pregunta: ")
    
    opciones = []
    for i in range(4):
        opcion = input(f"Ingrese la opción de respuesta {i + 1}: ")
        opciones.append(opcion)
    
    respuestaCorrecta = input("Ingrese el número de la opción correcta (1-4): ")
    while not (respuestaCorrecta.isdigit() and int(respuestaCorrecta) in [1, 2, 3, 4]):
        print(f"{yellow}Opción inválida. Debe ser un número entre 1 y 4.{reset}")
        respuestaCorrecta = input("Ingrese el número de la opción correcta (1-4): ")

# Agarro y corro a todo 1 indice menor, porque empiezan en 1 y yo necesito que empiecen en 0
    respuestaCorrecta = int(respuestaCorrecta) - 1  
    
# Guardamos la nueva pregunta en el archivo
    archivoPreguntas = open(rutaArchivo, 'a', encoding='utf-8')
    numeroPregunta = obtenerNumeroPregunta(rutaArchivo)
    opcionesTexto = ','.join(opciones)
    archivoPreguntas.write(f"{numeroPregunta};{pregunta};{opcionesTexto};{respuestaCorrecta}\n")
    archivoPreguntas.close()
    
    print(green + "Pregunta agregada con éxito." + reset)

def obtenerNumeroPregunta(rutaArchivo):
    try:
        with open(rutaArchivo, 'r', encoding='utf-8') as archivoPreguntas:
            lines = archivoPreguntas.readlines()
            if lines:
                ultimoLinea = lines[-1].strip()
                return int(ultimoLinea.split(';')[0]) + 1
            else:
                return 1 
    except FileNotFoundError:
        return 1 
    
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
            
            preguntas, opciones, respuestasCorrectas = cargarPreguntas(rutaElegida)

            puntuacionFinal = jugarPreguntas(preguntas, opciones, respuestasCorrectas, equipo)
            print(green + f"Juego terminado. Tu puntuación final es {puntuacionFinal}.")

            actualizarRanking(nombreUsuario, puntuacionFinal)

            cambiarUsuario = input(white + "¿Quieres cambiar de usuario para intentar de nuevo? Ingresá SI para cambiar, o presioná cualquier tecla para salir: ").upper()
            if cambiarUsuario != 'SI':
                print(red + "¡Muchas gracias por jugar! Te esperamos nuevamente.")
                continuar = False
        elif opcion == '2':
            mostrarRanking()
    
        elif opcion == '3': 
            print(red + "¡Agregar pregunta! ¡Próximamente!")
            
        elif opcion == '4': 
            print(red + "¡Muchas gracias por jugar! Te esperamos nuevamente.")
            continuar = False
    
        else:
            print(red + "Opción inválida. Por favor, selecciona 1, 2 o 3.")


if __name__ == "__main__":
    main()
