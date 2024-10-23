rutaArchivo1 = r"Programacion1ProyectoUADE\Files\usuarios.csv" 
rutaArchivo2 = r"Files\ranking.csv"

rutaElegida = rutaArchivo2


def actualizarRanking(ranking):
    try:
        arch = open(rutaElegida, "wt")
    except IOError:
        print("Error al abrir el archivo")    
    else:
        for username,equipo,puntaje in ranking:
            arch.write(f"{username};{equipo};{puntaje}\n")
        arch.close()
    
def cargarRanking():
    ranking = []
    try:
        arch = open(rutaElegida, "rt",encoding='latin-1')
    except IOError:
        print("Error al abrir el archivo")  
    else:
        for register in arch:
            username, equipo, puntaje = register.strip().split(";")
            ranking.append([username,equipo,puntaje])
        arch.close()
    return ranking
        
def chequeoRanking(username,equipo,puntaje):
    ranking = cargarRanking()
    encontrado = False
    for register in ranking:
        if username == register[0]:
            encontrado = True
            if int(register[2]) < puntaje:
                register[2] = puntaje
    if not encontrado:
        ranking.append([username,equipo,puntaje])
    actualizarRanking(ranking)
    
# Función recursiva que verifica si el ranking está ordenado por puntaje de mayor a menor
def estaOrdenada(ranking):
    '''Retorna True si está ordenada en forma descendente según los puntajes, False caso contrario. Recursiva'''
    if len(ranking) < 2:
        return True
    else:
        if int(ranking[0][2]) >= int(ranking[1][2]):
            return estaOrdenada(ranking[1:])
        else:
            return False
        
def mostrarRanking(username=None):
    ranking = cargarRanking()

    # Verifica si el ranking está ordenado
    if not estaOrdenada(ranking):
        ranking = sorted(ranking, key=lambda x: int(x[2]), reverse=True)
        actualizarRanking(ranking)

    # Mostrar solo el top 10
    top10 = ranking[:10]

    # Variable para almacenar si el usuario está fuera del top 10
    usuarioFueraTop10 = None

    # Mostrar el top 10
    print("Top 10 del ranking:")
    for i, register in enumerate(top10, start=1):
        print(f"{i}. {register[0]} - {register[1]} - {register[2]}")
    print("\n")

    # Si el username es especificado y no está en el top 10
    if username:
        for i, register in enumerate(ranking):
            if register[0] == username and i >= 10:
                usuarioFueraTop10 = register
                posicionUsuario = i + 1
                break

    # Mostrar la posición del usuario si está fuera del top 10
    if usuarioFueraTop10:
        print(f"El usuario {usuarioFueraTop10[0]} está en la posición {posicionUsuario}.")
        print(f"{posicionUsuario}. {usuarioFueraTop10[0]} - {usuarioFueraTop10[1]} - {usuarioFueraTop10[2]}")
