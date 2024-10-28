rutaArchivo1 = r"Programacion1ProyectoUADE\Files\usuarios.csv" 
rutaArchivo2 = r"Files\ranking.csv"

rutaElegida = rutaArchivo2
cyan = '\x1b[36m'
yellow = '\x1b[33m'
white = '\x1b[37m'
green = '\x1b[32m'
red = '\x1b[31m'
blue = '\x1b[34m'
reset = '\x1b[0m'

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
        
def buscarUsuarioRecursiva(ranking, username, index=0):
    '''Función recursiva que busca un usuario específico en el ranking.'''
    if index >= len(ranking):  # Si llegamos al final del ranking
        return None, None  # Usuario no encontrado
    if ranking[index][0] == username:  # Si encontramos el usuario
        return ranking[index], index + 1  # Devuelve el registro y su posición (index+1)
    return buscarUsuarioRecursiva(ranking, username, index + 1)  # Sigue buscando en el resto del ranking

def mostrarRanking(username=None):
    ranking = cargarRanking()

    # Verifica si el ranking está ordenado y sino lo ordena
    if not estaOrdenada(ranking):
        ranking = sorted(ranking, key=lambda x: int(x[2]), reverse=True)
        actualizarRanking(ranking)

    # Mostrar solo el top 10
    top10 = ranking[:10]
    print("\n")
    print(yellow + "Top 10 del ranking:" + reset)
    for i, register in enumerate(top10, start=1):
        print(f"{cyan}{i}. {white}{register[0]} - {cyan}{register[2]}{reset}")
    print("\n")

    # Si se especifica un usuario, buscamos recursivamente su posición
    if username:
        usuario, posicion = buscarUsuarioRecursiva(ranking, username)
        if usuario and posicion > 10:
            print(f"{yellow}El usuario {usuario[0]} está en la posición {posicion}.{reset}")
            print(f"{cyan}{posicion}. {white}{usuario[0]} - {cyan}{usuario[2]}{reset}")
        elif not usuario:
            print(f"El usuario {username} no se encontró en el ranking.")

