print("┎⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┒")
print("|  1  ┆  2  ┆  3  |")
print("|  4  ┆  5  ┆  6  |")
print("|  7  ┆  8  ┆  9  |")

def arco1():
    print("┎⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┒")
    print("|  ✅  ┆  ✅  ┆  ❌  |")
    print("|  ❌  ┆  ❌  ┆  ✅  |")
    print("|  ❌  ┆  ✅  ┆  ✅  |")

arco1 = [[1, 1, 0], [0, 0, 1], [0, 1, 1]]

matriz = [[1, 1, 0], [0, 0, 1], [0, 1, 1]]
print("┎⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┒")
for fila in matriz:
    print("|", end=" ")
    for casillero in fila:
        print("  " + str(casillero) + "  ┆", end=" ")
    print()
