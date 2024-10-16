rutaArchivo = "C:\\Users\\manni\\OneDrive\\Escritorio\\VALENTINA\\VALEN-2024 UADE\\2DO CUATRIMESTRE\\PROGRAMACION I\\Programacion1ProyectoUADE\\Files\\preguntas.txt"
preguntas = {}

try:
    with open(rutaArchivo, 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
        
        for line in lines:
            partes = line.strip().split(';')
            numeroPregunta = int(partes[0].strip())  
            pregunta = partes[1].strip()              
            opciones = [option.strip() for option in partes[2].split(',')]  
            respuestaCorrecta = int(partes[3].strip())   
            
            preguntas[numeroPregunta] = {
                "pregunta": pregunta,
                "opciones": opciones,
                "respuestaCorrecta": respuestaCorrecta
            }

except FileNotFoundError:
    print("Error: No se pudo encontrar el archivo de preguntas.")

print(preguntas[1])
print("---------------------")
print(preguntas[1]["pregunta"])
print("---------------------")
print(preguntas[1]["opciones"])
print("---------------------")
print(preguntas[1]["respuestaCorrecta"])
