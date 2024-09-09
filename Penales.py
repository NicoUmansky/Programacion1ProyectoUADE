import random
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

def gol():
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
    Gol = False
    print("Es momento de patear un penal para tener la posibilidad de sumar puntos extra, elige a donde quieres patear:")
    print("┎⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┒")
    print("|  1  ┆  2  ┆  3  |")
    print("|  4  ┆  5  ┆  6  |")
    print("|  7  ┆  8  ┆  9  |")
    casillero = input("Ingresa el número de la casillero a la que quieres patear (1 al 9): ")
    while not validarCasillero(casillero):
        print("casillero inexistente. Intente nuevamente")
        casillero =input("Ingresa el número de la casillero a la que quieres patear (1 al 9): ")
    
    configuracion = random.randint(1,3)
    if configuracion == 1:
        config = arco1()
    elif configuracion == 2:
        config = arco2()
    else:
        config = arco3()
    print()
    casillero = int(casillero)
    fila = (casillero - 1) // 3
    columna = (casillero - 1) % 3
    if config[fila][columna] == 1:
        gol()
        print()
        print("\x1b[1;32m"+"Gol! Obtienes 1 punto extra.")
        Gol = True
    else:   
        print("\033[1;31m"+"Fallaste!, no obtienes puntos extra")
    
    return Gol  

#Luego de patear un penal, tendras la posibilidad de atajar uno
def atajar():
    Atajar = False
    print("Es momento de atajar un penal para tener la posibilidad de sumar puntos extra, elige a donde quieres atajar:")
    print("┎⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┒")
    print("|  1  ┆  2  ┆  3  |")
    print("|  4  ┆  5  ┆  6  |")
    print("|  7  ┆  8  ┆  9  |")
    print()
    
    casillero = (input("Ingresa el número de casillero en la cual deseas atajar: "))
    while not validarCasillero(casillero):
        print("casillero inexistente")
        casillero =(input("Ingresa el número de la casillero en la cual deseas atajar: "))
    
    configuracion = random.randint(1,3)
    if configuracion == 1:
        config = arco1()
    elif configuracion == 2:
        config = arco2()
    else:
        config = arco3()
    print()
    casillero = int(casillero)
    fila = (casillero - 1) // 3
    columna = (casillero - 1) % 3
    if config[fila][columna] == 1:
        print("\033[1;31m"+"Fallaste! Pierdes un punto")
    else:
        print("\x1b[1;32m"+"Atajaste!")
        print()
        print("\x1b[1;32m"+"Ganaste 1 punto extra.")
        Atajar = True
        print()
    return Atajar


#penal()
#input("\033[0;37m"+"Presiona 1 para continuar: ")
#atajar()