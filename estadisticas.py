rutaArchivo1 = r"Programacion1ProyectoUADE/Files/estadisticasPuntaje.csv" 
rutaArchivo2 = r"Files\estadisticasPuntaje.csv"
rutaElegida = rutaArchivo2

def calcularEstadisticas (usuario, a,b,c,d):
    try:
        arch = open(rutaElegida, "at")
    except IOError:
        print("Error al abrir el archivo")
    else:
        arch.write(f"{usuario};{a};{b};{d}\n")
        arch.close()
        
