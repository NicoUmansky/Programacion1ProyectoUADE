import random
def arco1():
    print("┎⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┒")
    print("|  ✅  ┆  ✅  ┆  ❌  |")
    print("|  ❌  ┆  ❌  ┆  ✅  |")
    print("|  ❌  ┆  ✅  ┆  ✅  |")
    matrix1 = [[1, 1, 0], [0, 0, 1], [0, 1, 1]]
    return matrix1
def arco2():
    print("┎⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┒")
    print("|  ❌  ┆  ✅  ┆  ✅  |")
    print("|  ✅  ┆  ✅  ┆  ❌  |")
    print("|  ✅  ┆  ❌  ┆  ❌  |")
    matrix2 = [[0, 1, 1], [1, 1, 0], [1, 0, 0]]
    return matrix2
def arco3():
    print("┎⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┒")
    print("|  ✅  ┆  ✅  ┆  ❌  |")
    print("|  ❌  ┆  ✅  ┆  ❌  |")
    print("|  ✅  ┆  ✅  ┆  ❌  |")
    matrix3 = [[1, 1, 0], [0, 1, 0], [1, 1, 0]]
    return matrix3  

def gol():
    print("...")
    print()
    print("░██████╗░░█████╗░░█████╗░░█████╗░██╗░░░░░██╗")
    print("██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║░░░░░██║")
    print("██║░░██╗░██║░░██║██║░░██║██║░░██║██║░░░░░██║")
    print("██║░░╚██╗██║░░██║██║░░██║██║░░██║██║░░░░░╚═╝")
    print("╚██████╔╝╚█████╔╝╚█████╔╝╚█████╔╝███████╗██╗")
    print("░╚═════╝░░╚════╝░░╚════╝░░╚════╝░╚══════╝╚═╝")

def penal():
    print("Es momento de patear un penal para tener la posibilidad de sumar puntos extra, elige a donde quieres patear:")
    print("┎⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┒")
    print("|  1  ┆  2  ┆  3  |")
    print("|  4  ┆  5  ┆  6  |")
    print("|  7  ┆  8  ┆  9  |")
    casilla = int(input("Ingresa el número de la casilla a la que quieres patear: "))

    configuracion = random.randint(1,3)
    if configuracion == 1:
        config = arco1()
    elif configuracion == 2:
        config = arco2()
    else:
        config = arco3()
    print()
    fil = (casilla - 1) // 3
    col = (casilla - 1) % 3
    if config[fil][col] == 1:
        gol()
        print()
        print("\x1b[1;32m"+"Gol! Obtienes 1 punto extra.")
    else:
        print("\033[1;31m"+"Fallaste!")

#Luego de patear un penal, tendras la posibilidad de atajar uno
def atajar():
    print("Es momento de atajar un penal para tener la posibilidad de sumar puntos extra, elige a donde quieres atajar:")
    print("┎⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┒")
    print("|  1  ┆  2  ┆  3  |")
    print("|  4  ┆  5  ┆  6  |")
    print("|  7  ┆  8  ┆  9  |")
    print()
    casilla = int(input("Ingresa el número de la casilla a la que quieres atajar: "))
    configuracion = random.randint(1,3)
    if configuracion == 1:
        config = arco1()
    elif configuracion == 2:
        config = arco2()
    else:
        config = arco3()
    print()
    fil = (casilla - 1) // 3
    col = (casilla - 1) % 3
    if config[fil][col] == 1:
        print("\033[1;31m"+"Fallaste! Pierdes un punto")
    else:
        print("\x1b[1;32m"+"Atajaste!")
        print()
        print("\x1b[1;32m"+"Ganaste 1 punto extra.")
        print()


#penal()
#input("\033[0;37m"+"Presiona 1 para continuar: ")
#atajar()