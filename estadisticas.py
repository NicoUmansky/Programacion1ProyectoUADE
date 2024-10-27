def calcularEstadisticas (usuario, a,b,c,d):
    rutaArchivo1 = r"Programacion1ProyectoUADE/Files/estadisticasPuntaje.csv" 
    rutaArchivo2 = r"Files\estadisticasPuntaje.csv"
    rutaElegida = rutaArchivo2
    try:
        arch = open(rutaElegida, "at")
    except IOError:
        print("Error al abrir el archivo")
    else:
        arch.write(f"{usuario};{a};{b};{d}\n")
        arch.close()
        
def calcularEstadisticasPenales (usuario, a, b, c):
    rutaArchivo1 = r"Programacion1ProyectoUADE/Files/estadisticasPenales.csv" 
    rutaArchivo2 = r"Files\estadisticasPenales.csv"
    rutaElegida = rutaArchivo2
    try:
        arch = open(rutaElegida, "at")
    except IOError:
        print("Error al abrir el archivo")
    else:
        arch.write(f"{usuario};{a};{b};{c}\n")
        arch.close()