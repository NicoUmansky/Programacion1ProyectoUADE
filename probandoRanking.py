def actualizarRanking(username,equipo,puntaje):
    try:
        arch = open(r"Programacion1ProyectoUADE\Files\ranking.csv", "at")
    except IOError:
        print("Error al abrir el archivo")    
    if chequeoRanking(username,equipo,puntaje):
        arch.write(f"{username};{equipo};{puntaje}\n")
        arch.close()
    
def chequeoRanking(username,equipo,puntaje):
    try:
        arch = open(r"Programacion1ProyectoUADE\Files\ranking.csv", "rt")
    except IOError:
        print("Error al abrir el archivo")
    else:
        encontrado = True
        for linea in arch:
            userArchivo, equipoArchivo, puntajeArchivo = linea.strip().split(";")
            if username == userArchivo:
                if puntaje < puntajeArchivo:
                    encontrado = False
                    # actualizarRanking(username,equipo,puntaje)    
        arch.close()
        return encontrado
    
def mostrarRanking(username):
    try:
        arch = open(r"Programacion1ProyectoUADE\Files\ranking.csv", "rt")
    except IOError:
        print("Error al abrir el archivo")
    else:
        ranking = []
        for linea in arch:
            userArchivo, equipoArchivo, puntajeArchivo = linea.strip().split(";")
            ranking.append((userArchivo, equipoArchivo, int(puntajeArchivo)))
        arch.close()
        
        # Sort the ranking by score in descending order
        ranking.sort(key=lambda x: x[2], reverse=True)
        
        # Find the user's position
        user_position = None
        for i, v in enumerate(ranking):
            if v[0] == username:
                user_position = i
                break
        
        # Print the top 10 or all if less than 10
        print("Ranking:")
        for i, (userArchivo, equipoArchivo, puntajeArchivo) in enumerate(ranking[:10]):
            print(f"{i + 1}. {userArchivo} - {equipoArchivo} - {puntajeArchivo}")
        
        # If the user is not in the top 10, print their position
        if user_position is not None and user_position >= 10:
            user_data = ranking[user_position]
            print(f"...\n{user_position + 1}. {user_data[0]} - {user_data[1]} - {user_data[2]}")