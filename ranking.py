puntuaciones = []

yellow = '\x1b[33m'
blue = '\x1b[34m'

def mostrarRanking():
    if not puntuaciones:
        print("No hay puntuaciones para mostrar.")
    else:
        puntuacionesOrdenadas = sorted(puntuaciones, key=lambda x: x[1], reverse=True)
        print(blue + "Ranking:")
        for i, (nombre, puntos) in enumerate(puntuacionesOrdenadas):
            print(yellow + f"{i + 1}. {nombre} - {puntos} puntos")
    input(yellow + "Presiona Enter para volver al menú principal.")

def actualizarRanking(nombreUsuario, puntuacionFinal):
    for puntuacion in puntuaciones:
        if puntuacion[0] == nombreUsuario:
            print("Ya estás en el ranking. No puedes volver a jugar.")
            return
    puntuaciones.append([nombreUsuario, puntuacionFinal])