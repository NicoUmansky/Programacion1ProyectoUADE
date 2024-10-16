from inicioSesion import inicioSesion
from triviaPreguntas import jugarPreguntas
from ranking import mostrarRanking, actualizarRanking, puntuaciones

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
    print(yellow + "3. Salir")
    opcion = input(white + "Seleccione una opción (1, 2 o 3): ")
    return opcion

def main():
    continuar = True
    
    while continuar:
        opcion = mostrarMenu()
        
        if opcion == '1':
            print(red + "¡Bienvenido a Kick & Quiz!")
            print(yellow + "Por favor, ingrese a su cuenta o registrese para empezar a jugar")
            
            cambiarUsuario = True
            while cambiarUsuario:
                usuarioEnRanking = False
                i = 0
                while i < len(puntuaciones):
                    if puntuaciones[i][0] == nombreUsuario:
                        usuarioEnRanking = True
                        i = len(puntuaciones)
                    i += 1
                if usuarioEnRanking:
                    print(red + "Ya jugaste y estás en el ranking. Por favor, inicia sesión con otro usuario.")
                else:
                    cambiarUsuario = False 

            print(blue + "¡Empecemos a jugar!")
            print(red + "Tenes 3 vidas disponibles. ¡Aprovechalas! ❤️  ❤️  ❤️" + reset)
            
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
                "¿En qué ciudad argentina se realiza anualmente la Fiesta Nacional de la Vendimia?",
                "¿Cuál fue la primera película argentina en ganar un premio Óscar?",
                "¿En qué año se inauguró el Obelisco de Buenos Aires?",
                "¿Qué famoso músico argentino lideró la banda Soda Stereo?",
            ]
            
            opciones = [
                ["Aconcagua", "Cerro Torre", "Monte Fitz Roy", "Nevado de Cachi"],
                ["1928", "1930", "1934", "1950"],
                ["Mendoza", "Córdoba", "Tucumán", "Santa Fe"],
                ["Bartolomé Mitre", "Julio A. Roca", "Domingo F. Sarmiento", "Hipólito Yrigoyen"],
                ["El Calafate", "Ushuaia", "Bariloche", "San Martín de los Andes"],
                ["Santa Rosa", "General Pico", "San Luis", "Resistencia"],
                ["Río Uruguay", "Río Paraná", "Río Colorado", "Río Salado"],
                ["1816", "1821", "1830", "1806"],
                ["Julio Cortázar", "Adolfo Bioy Casares", "Jorge Luis Borges", "Manuel Puig"],
                ["Chinchulines", "Provoleta", "Empanadas", "Milanesas"],
                ["San Juan", "La Rioja", "Salta", "Mendoza"],
                ["Atahualpa Yupanqui", "Mercedes Sosa", "Carlos Gardel", "Sandro"],
                ["1947", "1951", "1937", "1960"],
                ["Parque Nacional Nahuel Huapi", "Parque Nacional Iguazú", "Parque Nacional Los Glaciares", "Parque Nacional Talampaya"],
                ["Río Paraná", "Río Uruguay", "Río de la Plata", "Río Colorado"],
                ["Río Gallegos", "Ushuaia", "El Chaltén", "Puerto Madryn"],
                ["1810", "1820", "1806", "1816"],
                ["Formosa", "Salta", "Jujuy", "Misiones"],
                ["SAC-B", "ARSAT-1", "SAOCOM 1A", "LUSAT-1"],
                ["San Juan", "La Rioja", "Mendoza", "San Rafael"],
                ["La Historia Oficial", "El Secreto de Sus Ojos", "Camila", "Nueve Reinas"],
                ["1936", "1945", "1952", "1960"],
                ["Luis Alberto Spinetta", "Fito Páez", "Charly García", "Gustavo Cerati"]
            ]
            
            respuestasCorrectas = [0, 1, 1, 3, 0, 0, 1, 1, 2, 0, 3, 2, 0, 1, 1, 1, 3, 0, 3, 2, 1, 0, 3]

            puntuacionFinal = jugarPreguntas(preguntas, opciones, respuestasCorrectas,equipo)
            print(green + f"Juego terminado. Tu puntuación final es {puntuacionFinal}.")

            actualizarRanking(nombreUsuario, puntuacionFinal)

            cambiarUsuario = input(white + "¿Querés cambiar de usuario para intentar de nuevo? Ingresá SI para cambiar, o presioná cualquier tecla para salir: ").upper()
            if cambiarUsuario != 'SI':
                print(red + "¡Muchas gracias por jugar! Te esperamos nuevamente.")
                continuar = False
    
        elif opcion == '2':
            mostrarRanking()
    
        elif opcion == '3': 
            print(red + "¡Muchas gracias por jugar! Te esperamos nuevamente.")
            continuar = False
    
        else:
            print(red + "Opción inválida. Por favor, selecciona 1, 2 o 3.")

if __name__ == "__main__":
    main()
