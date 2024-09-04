def inicioSesion():
    print("¡Bienvenido a Kick & Quiz!")
    print("Por favor, logueese para empezar a jugar")

    mail_usuario = input("Ingrese su mail: ")
    contra_usuario = input("Ingrese su contraseña: ")

    while mail_usuario != "eugenia@gmail.com":
        print("Mail incorrecto.")
        mail_usuario = input("Reingrese su mail: ")
    
    while contra_usuario != "1234":
        print("Contraseña incorrecta.")
        contra_usuario = input("Reingrese su contraseña: ")
    
    print("¡Bienvenida Eugenia!")

def empezar_juego():
   
    print("¡Empecemos a jugar!")

def preguntasYRespuestas():
 
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
    
    opcionesYRespuestas = [
        ["Aconcagua", "Cerro Torre", "Monte Fitz Roy", "Nevado de Cachi", "Aconcagua"],
        ["1930", "1934", "1950", "1928", "1930"],
        ["Córdoba", "Mendoza", "Tucumán", "Santa Fe", "Córdoba"],
        ["Hipólito Yrigoyen", "Bartolomé Mitre", "Julio A. Roca", "Domingo F. Sarmiento", "Hipólito Yrigoyen"],
        ["El Calafate", "Ushuaia", "Bariloche", "San Martín de los Andes", "El Calafate"],
        ["Santa Rosa", "General Pico", "San Luis", "Resistencia", "Santa Rosa"],
        ["Río Paraná", "Río Uruguay", "Río Colorado", "Río Salado", "Río Paraná"],
        ["1821", "1816", "1830", "1806", "1821"],
        ["Jorge Luis Borges", "Julio Cortázar", "Adolfo Bioy Casares", "Manuel Puig", "Jorge Luis Borges"],
        ["Chinchulines", "Provoleta", "Empanadas", "Milanesas", "Chinchulines"],
        ["Mendoza", "San Juan", "La Rioja", "Salta", "Mendoza"],
        ["Carlos Gardel", "Atahualpa Yupanqui", "Mercedes Sosa", "Sandro", "Carlos Gardel"],
        ["1947", "1951", "1937", "1960", "1947"],
        ["Parque Nacional Iguazú", "Parque Nacional Nahuel Huapi", "Parque Nacional Los Glaciares", "Parque Nacional Talampaya", "Parque Nacional Iguazú"],
        ["Río Uruguay", "Río Paraná", "Río de la Plata", "Río Colorado", "Río Uruguay"],
        ["Ushuaia", "Río Gallegos", "El Chaltén", "Puerto Madryn", "Ushuaia"],
        ["1816", "1810", "1820", "1806", "1816"],
        ["Salta", "Formosa", "Jujuy", "Misiones", "Formosa"],
        ["SAC-B", "ARSAT-1", "SAOCOM 1A", "LUSAT-1", "LUSAT-1"],
        ["Mendoza", "San Juan", "La Rioja", "San Rafael", "Mendoza"]
    ]
    
    return preguntas, opcionesYRespuestas

def main():
    inicioSesion()
    
    preguntas, opcionesRespuestas = preguntasYRespuestas()
    print(preguntas)
    print(opcionesRespuestas)
    

if __name__ == "__main__":
    main()
