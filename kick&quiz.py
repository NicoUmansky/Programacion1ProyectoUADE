from inicioSesion import inicioSesion
from triviaPreguntas import jugarPreguntas

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
