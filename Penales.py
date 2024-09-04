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
    print("░██████╗░░█████╗░░█████╗░░█████╗░██╗░░░░░██╗")
    print("██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║░░░░░██║")
    print("██║░░██╗░██║░░██║██║░░██║██║░░██║██║░░░░░██║")
    print("██║░░╚██╗██║░░██║██║░░██║██║░░██║██║░░░░░╚═╝")
    print("╚██████╔╝╚█████╔╝╚█████╔╝╚█████╔╝███████╗██╗")
    print("░╚═════╝░░╚════╝░░╚════╝░░╚════╝░╚══════╝╚═╝")
#Funcion para patear un penal en caso de que la respuesta sea correcta
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
        print()
    elif configuracion == 2:
        config = arco2()
        print()
    else:
        config = arco3()
        print()
    if casilla == 1:
        if config[0][0] == 1:
            gol()
            print("Gol! Obtienes 1 punto extra.")
        else:
            print("Fallaste!")
    elif casilla == 2:
        if config[0][1] == 1:
            gol()
            print("Gol! Obtienes 1 punto extra.")
        else:
            print("Fallaste!")
    elif casilla == 3:
        if config[0][2] == 1:
            gol()
            print("Gol! Obtienes 1 punto extra.")
        else:
            print("Fallaste!")
    elif casilla == 4:
        if config[1][0] == 1:
            gol()
            print("Gol! Obtienes 1 punto extra.")
        else:
            print("Fallaste!")
    elif casilla == 5:
        if config[1][1] == 1:
            gol()
            print("Gol! Obtienes 1 punto extra.")
        else:
            print("Fallaste!")
    elif casilla == 6:
        if config[1][2] == 1:
            gol()
            print("Gol! Obtienes 1 punto extra.")
        else:
            print("Fallaste!")
    elif casilla == 7:
        if config[2][0] == 1:
            gol()
            print("Gol! Obtienes 1 punto extra.")
        else:
            print("Fallaste!")
    elif casilla == 8:
        if config[2][1] == 1:
            gol()
            print("Gol! Obtienes 1 punto extra.")
        else:
            print("Fallaste!")
    elif casilla == 9:
        if config[2][2] == 1:
            gol()
            print("Gol! Obtienes 1 punto extra.")
        else:
            print("Fallaste!")



penal()