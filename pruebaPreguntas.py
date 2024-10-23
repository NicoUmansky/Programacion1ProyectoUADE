rutaArchivo = "Programacion1ProyectoUADE/Files/preguntas.txt"

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
        archivoPreguntas = open(rutaArchivo, 'a', encoding='utf-8')
        numeroPregunta = obtenerNumeroPregunta(rutaArchivo)
        opcionesTexto = ','.join(opciones)

        archivoPreguntas.write(f"{numeroPregunta};{pregunta};{opcionesTexto};{respuestaCorrecta}\n")
        archivoPreguntas.close() 
        print(yellow + "¡Pregunta agregada exitosamente!" + reset)

def obtenerNumeroPregunta(ruta):
    #Consigo el numero de la ultima pregunta para asignarle el siguiente numero a la que estoy creando
    try:
        archivoPreguntas = open(rutaArchivo, 'r', encoding='utf-8')
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

def main():
    agregarPregunta(rutaArchivo)
    

if __name__ == "__main__":
    main()
