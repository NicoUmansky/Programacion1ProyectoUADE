rutaArchivo1 = r"Files/estadisticas" 
rutaArchivo2 = r"Files\estadisticas"
rutaElegida = rutaArchivo1
    
def calcularEstadisticas (usuario, a,b,c,d):
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
        