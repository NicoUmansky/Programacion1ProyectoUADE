def inicioSesion():
    mailCorrecto = "eugenia@gmail.com"
    contraCorrecta = "1234"

    mailUsuario = input("Ingrese su mail: ")
    while mailUsuario != mailCorrecto:
        print("Mail incorrecto.")
        mailUsuario = input("Reingrese su mail: ")

    contraUsuario = input("Ingrese su contraseña (4 dígitos): ")
    while not (contraUsuario.isdigit() and len(contraUsuario) == 4):
        print("Contraseña incorrecta. Debe ser un número de 4 dígitos.")
        contraUsuario = input("Reingrese su contraseña (4 dígitos): ")
    
    while contraUsuario != contraCorrecta:
        print("Contraseña incorrecta.")
        contraUsuario = input("Reingrese su contraseña (4 dígitos): ")
    
    print("¡Bienvenida Eugenia!")

def mostrarPregunta(pregunta, opciones):
    print(pregunta)
    for i in range(len(opciones)):
        print(f"{i+1}. {opciones[i]}")

def obtenerRespuestaValida(opciones):
    while True:
        respuesta = input("Seleccione una opción (1-4): ")
        if respuesta.isdigit():
            respuesta = int(respuesta) - 1
            if 0 <= respuesta < len(opciones):
                return respuesta
            else:
                print("Opción inválida. Por favor, seleccione un número entre 1 y 4.")
        else:
            print("Entrada inválida. Por favor, ingrese un número entre 1 y 4.")

def jugarPreguntas(preguntas, opciones, respuestasCorrectas):
    vidas = 3
    puntuacion = 0

    for i in range(len(preguntas)):
        if vidas <= 0:
            return puntuacion

        mostrarPregunta(preguntas[i], opciones[i])
        respuestaUsuario = obtenerRespuestaValida(opciones[i])
        
        if respuestaUsuario == respuestasCorrectas[i]:
            print("¡Respuesta correcta!")
            puntuacion += 1
        else:
            print("Respuesta incorrecta.")
            vidas -= 1
            print(f"Te quedan {vidas} vidas.")

    return puntuacion

def main():
    print("¡Bienvenido a Kick & Quiz!")
    print("Por favor, loguéese para empezar a jugar")

    inicioSesion()
    print("¡Empecemos a jugar!")

    preguntas = [
        "¿Cuál es la montaña más alta de Argentina?",
        "¿En qué año se celebró el primer Mundial de Fútbol en el que participó Argentina?",
        "¿Qué provincia argentina es conocida como 'La Docta'?",
        "¿Quién fue el primer presidente argentino en llegar al poder mediante elecciones directas?",
        "¿En qué ciudad se encuentra el famoso glaciar Perito Moreno?",
        "¿Cuál es la capital de la provincia de La Pampa?",
        "¿Cuál es el río más largo de Argentina?",
        "¿En qué año se fundó la Universidad de Buenos Aires?",
        "¿Qué famoso escritor argentino es conocido por su obra 'El Aleph'?",
        "¿Cuál es el plato típico argentino que consiste en intestinos de vaca asados a la parrilla?",
        "¿Qué provincia argentina es la mayor productora de vino?",
        "¿Qué famoso cantante argentino es conocido como 'El Zorzal Criollo'?",
        "¿En qué año fue sancionada la Ley de Voto Femenino en Argentina?",
        "¿Cuál es el nombre del Parque Nacional que protege las Cataratas del Iguazú?",
        "¿Qué río marca la frontera natural entre Argentina y Uruguay?",
        "¿Cuál es la ciudad más austral del mundo, ubicada en Argentina?",
        "¿En qué año se declaró la independencia de Argentina?",
        "¿Qué provincia argentina limita con Bolivia y Paraguay?",
        "¿Cuál es el nombre del primer satélite argentino lanzado al espacio?",
        "¿En qué ciudad argentina se realiza anualmente la Fiesta Nacional de la Vendimia?"
    ]
    
    opciones = [
        ["Aconcagua", "Cerro Torre", "Monte Fitz Roy", "Nevado de Cachi"],
        ["1930", "1934", "1950", "1928"],
        ["Córdoba", "Mendoza", "Tucumán", "Santa Fe"],
        ["Hipólito Yrigoyen", "Bartolomé Mitre", "Julio A. Roca", "Domingo F. Sarmiento"],
        ["El Calafate", "Ushuaia", "Bariloche", "San Martín de los Andes"],
        ["Santa Rosa", "General Pico", "San Luis", "Resistencia"],
        ["Río Paraná", "Río Uruguay", "Río Colorado", "Río Salado"],
        ["1821", "1816", "1830", "1806"],
        ["Jorge Luis Borges", "Julio Cortázar", "Adolfo Bioy Casares", "Manuel Puig"],
        ["Chinchulines", "Provoleta", "Empanadas", "Milanesas"],
        ["Mendoza", "San Juan", "La Rioja", "Salta"],
        ["Carlos Gardel", "Atahualpa Yupanqui", "Mercedes Sosa", "Sandro"],
        ["1947", "1951", "1937", "1960"],
        ["Parque Nacional Iguazú", "Parque Nacional Nahuel Huapi", "Parque Nacional Los Glaciares", "Parque Nacional Talampaya"],
        ["Río Uruguay", "Río Paraná", "Río de la Plata", "Río Colorado"],
        ["Ushuaia", "Río Gallegos", "El Chaltén", "Puerto Madryn"],
        ["1816", "1810", "1820", "1806"],
        ["Salta", "Formosa", "Jujuy", "Misiones"],
        ["SAC-B", "ARSAT-1", "SAOCOM 1A", "LUSAT-1"],
        ["Mendoza", "San Juan", "La Rioja", "San Rafael"]
    ]
    
    respuestasCorrectas = [0, 1, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 3, 0]

    puntuacionFinal = jugarPreguntas(preguntas, opciones, respuestasCorrectas)
    print(f"Juego terminado. Tu puntuación final es {puntuacionFinal}.")

if __name__ == "__main__":
    main()
