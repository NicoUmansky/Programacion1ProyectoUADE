puntuaciones = []

yellow = '\x1b[33m'
blue = '\x1b[34m'
white = '\x1b[37m'


def obtenerPuntos(puntuacion):
    return puntuacion[1]

def mostrarRanking():
    if len(puntuaciones) == 0:
        print("No hay puntuaciones para mostrar.")
    else:
        puntuacionesOrdenadas = sorted(puntuaciones, key=obtenerPuntos, reverse=True)
        print(blue + "Ranking:")
        for i in range(len(puntuacionesOrdenadas)):
            nombre = puntuacionesOrdenadas[i][0]
            puntos = puntuacionesOrdenadas[i][1]
            print(yellow + f"{i + 1}. {nombre} - {puntos} puntos")
    
    input(f"{white}Presiona cualquier botón para continuar: {reset}")



def actualizarRanking(nombreUsuario, puntuacionFinal):
    for puntuacion in puntuaciones:
        if puntuacion[0] == nombreUsuario:
            print("Ya estás en el ranking. No podes volver a jugar.")
            return
    puntuaciones.append([nombreUsuario, puntuacionFinal])