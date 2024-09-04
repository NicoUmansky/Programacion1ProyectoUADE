#Programa principal           
def main():
    
    #Lista de preguntas
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

# Matriz en la que cada fila tiene cinco elementos: las cuatro opciones de respuesta y, en el último, la opción correcta.
opciones_y_respuestas = [
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


print("¡Bienvenido a Kick & Quiz!")
print("Por favor, logueese para empezar a jugar")

mail_usuario = input("Ingrese su mail: ")
contra_usuario= input("Ingrese su contraseña: ")

if mail_usuario == "eugenia@gmail.com":
    if contra_usuario == "1234":
        print("¡Bienvenida Eugenia!")
    else:
        print("Contraseña incorrecta.")
        while(contra_usuario != "1234"):
            print("Contraseña incorrecta.")
            contra_usuario= input("Reingrese su contraseña: ")
else:
    print("Mail incorrecto.")
    while(mail_usuario != "eugenia@gmail.com"):
        mail_usuario = input("Reingrese su mail: ")
        print("Mail incorrecto.")
    print("¡Bienvenida Eugenia!")


print("¡Empecemos a jugar!")






if __name__ == "__main__":
    main()


#OBLIGATORIO: TEMA - ALCANCE - INFORMES (3)

#hay que poner una condicion de fin, dejo de cargar cuando... 
#EJ: (haya cargado x cant de elementos, o cuando el usuario ingrese un valor "no quiero cargar mas", etc)

#MINIMO 3 INFORMES, como me queda la matriz es un buen informe
#podemos hacer x cant jugadores, x cant de jugadas, x cant de puntos --> esos 3 se relacionan 
#despues el informe me dice
#1) cuanto gano cada jugador
#2) el promedio de puntos del total de jugadas
#3) el jugador con mas/menos puntos
#otra opcion: listado ordenado... 

#puedo poner un log in (dos listas paralelas- nombre de usuario + contraseña)- 
#aca incorporo cadena de caracteres y modulo. 
#Funcion que los valide- requerimiento (usuario valido segun nuestras condiciones y que el usuario no se repita)
