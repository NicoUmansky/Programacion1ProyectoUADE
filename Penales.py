import random

# Colores usando código ANSI
cyan = '\x1b[36m'
yellow = '\x1b[33m'
white = '\x1b[37m'
green = '\x1b[32m'
red = '\x1b[31m'
blue = '\x1b[34m'

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
    return  matriz2
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
    
validarCasillero = lambda casillero : casillero.isdigit() and 1 <= int(casillero) <= 9

def penal():
    gol = False
    print("Es momento de patear un penal para tener la posibilidad de sumar puntos extra, elige a donde quieres patear:")
    print("┎⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┒")
    print("|  1  ┆  2  ┆  3  |")
    print("|  4  ┆  5  ┆  6  |")
    print("|  7  ┆  8  ┆  9  |")
    casillero = input("Ingresa el número del casillero al que quieres patear (1 al 9): ")
    while not validarCasillero(casillero):
        print("Casillero inexistente")
        casillero = input("Ingresa el número del casillero al que quieres patear (1 al 9): ")
    configuracion = random.randint(1,3)
    if configuracion == 1:
        arcoElegido = arco1()
    elif configuracion == 2:
        arcoElegido = arco2()
    else:
        arcoElegido = arco3()
    print()
    casillero = int(casillero)
    fila = (casillero - 1) // 3 # Por ejemplo si escribe el 6 el calculo sería 5 // 3 = 1 osea que es la segunda fila 
    columna = (casillero - 1) % 3 # Por ejemplo si escribe el 6 el calculo sería 5 % 3 = 2 osea que es la tercer columna 
    if arcoElegido[fila][columna] == 1:
        cartelGol()
        print()
        print("\x1b[1;32m"+"Gol! Obtienes 1 punto extra.")
        gol = True
    else:   
        print("\033[1;31m"+"Fallaste!, no obtienes puntos extra")
    
    return gol  

#Luego de patear un penal, tendras la posibilidad de atajar uno
def atajar():
    atajar = False
    print("Es momento de atajar un penal para tener la posibilidad de sumar puntos extra, elige a donde quieres atajar:")
    print("┎⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┒")
    print("|  1  ┆  2  ┆  3  |")
    print("|  4  ┆  5  ┆  6  |")
    print("|  7  ┆  8  ┆  9  |")
    print()
    
    casillero = input("Ingresa el número del casillero al cual deseas atajar (1 al 9): ")
    while not validarCasillero(casillero):
        print("Casillero inexistente")
        casillero = input("Ingresa el número del casillero al cual deseas atajar (1 al 9): ")
    
    configuracion = random.randint(1,3)
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
        print("\033[1;31m"+"Fallaste! Pierdes un punto")
    else:
        print("\x1b[1;32m"+"Atajaste!")
        print()
        print("\x1b[1;32m"+"Ganaste 1 punto extra.")
        atajar = True
        print()
    return atajar


#penal()
#input("\033[0;37m"+"Presiona 1 para continuar: ")
#atajar()