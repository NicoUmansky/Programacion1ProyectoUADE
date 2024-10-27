puntuaciones = []
yellow = '\x1b[33m'
blue = '\x1b[34m'
white = '\x1b[37m'
reset = '\x1b[0m'

def obtenerPuntos(puntuacion):
    return puntuacion[1]

def mostrarRanking():
    if len(puntuaciones) == 0:
        print("No hay puntuaciones para mostrar.")
    else:
        puntuacionesOrdenadas = sorted(puntuaciones, key=obtenerPuntos, reverse=True)
        print(f"{blue}Ranking:{reset}")
        for i in range(len(puntuacionesOrdenadas)):
            nombre = puntuacionesOrdenadas[i][0]
            puntos = puntuacionesOrdenadas[i][1]
            print(f"{yellow}{i + 1}) {nombre} - {puntos} puntos{reset}")
    
    input(f"{white}Presiona cualquier botón para volver al menú principal.{reset}")


def actualizarRanking(nombreUsuario, puntuacionFinal):
    usuarioEnRanking = False
    i = 0
    while i < len(puntuaciones):
        if puntuaciones[i][0] == nombreUsuario:
            usuarioEnRanking = True
        i += 1
    if usuarioEnRanking:
        print("Ya estás en el ranking. No podés volver a jugar.")
    else:
        puntuaciones.append([nombreUsuario, puntuacionFinal])
