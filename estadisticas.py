<<<<<<< Updated upstream
rutaArchivo1 = r"Files/estadisticas" 
rutaArchivo2 = r"Files\estadisticas"
rutaElegida = rutaArchivo1
    
def calcularEstadisticas (usuario, a,b,c,d):
=======
def calcularEstadisticas (usuario, a,b,d):
    rutaArchivo1 = r"Programacion1ProyectoUADE/Files/estadisticasPuntaje.csv" 
    rutaArchivo2 = r"Files\estadisticasPuntaje.csv"
    rutaElegida = rutaArchivo2
>>>>>>> Stashed changes
    try:
        arch = open(rutaElegida + "Puntaje.csv", "at")
    except IOError:
        print("Error al abrir el archivo")
    else:
        arch.write(f"{usuario};{a};{b};{d}\n")
        arch.close()
        
def calcularEstadisticasPenales (usuario, a, b, c):
    try:
        arch = open(rutaElegida + "Penales.csv", "at")
    except IOError:
        print("Error al abrir el archivo")
    else:
        arch.write(f"{usuario};{a};{b};{c}\n")
        arch.close()
        