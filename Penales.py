import random
from inicioSesion import inicioSesion
# Colores usando código ANSI
cyan = '\x1b[36m'
yellow = '\x1b[33m'
white = '\x1b[37m'
green = '\x1b[32m'
red = '\x1b[31m'
blue = '\x1b[34m'
reset = '\x1b[0m'
equipos_argentinos = ["Argentinos Juniors", "Atlético Tucumán", "Banfield", "Barracas Central", "Belgrano", "Boca Juniors", "Deportivo Riestra", "Defensa y Justicia", "Estudiantes", "Gimnasia", "Godoy Cruz", "Huracán", "Independiente", "Independiente de Rivadavia", "Instituto", "Lanús", "Newell's Old Boys", "Platense", "Racing", "River Plate", "Rosario Central", "Sarmiento", "San Lorenzo", "Talleres", "Tigre", "Unión", "Vélez", "Central Córdoba"]

def arco1():
    print("...")
    print("┎⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┒")
    print("|  ✅  ┆  ✅  ┆  ❌  |")
    print("|  ❌  ┆  ❌  ┆  ✅  |")
    print("|  ❌  ┆  ✅  ┆  ✅  |")
    matriz1 = [[1, 1, 0], [0, 0, 1], [0, 1, 1]]
    return matriz1

def arco2():
    print("...")
    print("┎⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┒")
    print("|  ❌  ┆  ✅  ┆  ✅  |")
    print("|  ✅  ┆  ✅  ┆  ❌  |")
    print("|  ✅  ┆  ❌  ┆  ❌  |")
    matriz2 = [[0, 1, 1], [1, 1, 0], [1, 0, 0]]
    return matriz2

def arco3():
    print("...")
    print("┎⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┒")
    print("|  ✅  ┆  ✅  ┆  ❌  |")
    print("|  ❌  ┆  ✅  ┆  ❌  |")
    print("|  ✅  ┆  ✅  ┆  ❌  |")
    matriz3 = [[1, 1, 0], [0, 1, 0], [1, 1, 0]]
    return matriz3  

def cartelGol():
    print("...")
    print()
    print("░██████╗░░█████╗░░█████╗░░█████╗░██╗░░░░░██╗")
    print("██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║░░░░░██║")
    print("██║░░██╗░██║░░██║██║░░██║██║░░██║██║░░░░░██║")
    print("██║░░╚██╗██║░░██║██║░░██║██║░░██║██║░░░░░╚═╝")
    print("╚██████╔╝╚█████╔╝╚█████╔╝╚█████╔╝███████╗██╗")
    print("░╚═════╝░░╚════╝░░╚════╝░░╚════╝░╚══════╝╚═╝")
    
validarCasillero = lambda casillero: casillero.isdigit() and 1 <= int(casillero) <= 9

def penal(equipo):
    rival = random.choice(equipos_argentinos)
    gol = False
    print(f"Comienza el partido, {equipo} vs {rival}")
    print("Es momento de patear un penal para tener la posibilidad de sumar puntos extra, elegí a donde querés patear:")
    print("┎⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┒")
    print("|  1  ┆  2  ┆  3  |")
    print("|  4  ┆  5  ┆  6  |")
    print("|  7  ┆  8  ┆  9  |")
    casillero = input("Ingresa el número del casillero al que querés patear (1 al 9): ")
    while not validarCasillero(casillero):
        print(f"{red}Casillero inexistente {reset}")
        casillero = input("Ingresa el número del casillero al que quieres patear (1 al 9): ")
    
    configuracion = random.randint(1, 3)
    if configuracion == 1:
        arcoElegido = arco1()
    elif configuracion == 2:
        arcoElegido = arco2()
    else:
        arcoElegido = arco3()
    
    print()
    casillero = int(casillero)
    fila = (casillero - 1) // 3  # Por ejemplo si escribe el 6 el cálculo sería 5 // 3 = 1, o sea que es la segunda fila 
    columna = (casillero - 1) % 3  # Por ejemplo si escribe el 6 el cálculo sería 5 % 3 = 2, o sea que es la tercer columna 
    
    if arcoElegido[fila][columna] == 1:
        cartelGol()
        print()
        print(f"{green} ¡Gol! {equipo.capitalize()} a ganado! Obtenés 1 punto extra.{reset}")
        gol = True
    else:   
        print(f"{red} ¡Fallaste!, gano {rival} no obtenés puntos extra{reset}")
    
    return gol  

# Luego de patear un penal, tendrás la posibilidad de atajar uno
def atajar(equipo):
    atajar = False
    print("Es momento de atajar un penal para tener la posibilidad de sumar puntos extra, elegí a donde queres atajar:")
    print("┎⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┒")
    print("|  1  ┆  2  ┆  3  |")
    print("|  4  ┆  5  ┆  6  |")
    print("|  7  ┆  8  ┆  9  |")
    print()
    
    casillero = input("Ingresa el número del casillero al cual deseas atajar (1 al 9): ")
    while not validarCasillero(casillero):
        print(f"{red}Casillero inexistente {reset}")
        casillero = input("Ingresa el número del casillero al cual deseas atajar (1 al 9): ")
    
    configuracion = random.randint(1, 3)
    if configuracion == 1:
        arcoElegido = arco1()
    elif configuracion == 2:
        arcoElegido = arco2()
    else:
        arcoElegido = arco3()
    
    print()
    casillero = int(casillero)
    fila = (casillero - 1) // 3
    columna = (casillero - 1) % 3
    
    if arcoElegido[fila][columna] == 1:
        print(f"{red}¡Fallaste! Perdés un punto{reset}")
    else:
        print(f"{green}¡Atajaste!{reset}")
        print()
        print(f"{green}Ganaste 1 punto extra.{reset}")
        atajar = True
        print()
    
    return atajar
