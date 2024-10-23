#PARA AGREGAR NUEVAS PREGUNTAS

#NUEVO DE AGREGAR PREGUNTAS
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
    