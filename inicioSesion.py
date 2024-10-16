def inicioSesion():
    validarInicio = lambda eleccion:  eleccion.isdigit() and decision in ['1', '2']
    validarContra = lambda contra: contra.isdigit() and len(contra) == 4    
    validarSexo = lambda sex: sex.upper() == "M" or sex.upper() == "F" or sex.upper() == "X"

    decision = input("Presione 1 para Iniciar Sesión o 2 para Registrarse en su cuenta: ")
    while not validarInicio(decision):
        print("Opción incorrecta.")
        decision = input("Presione 1 para Iniciar Sesión o 2 para Registrarse en su cuenta: ")
   
    # Inicia Sesión
    if decision == '1':    
        mailUsuario = input("Ingrese su mail: ")
        while not validarMailExistente(mailUsuario):
            print("Mail no registrado.")
            mailUsuario = input("Ingrese un mail registrado: ")
        contraUsuario = input("Ingrese su contraseña (4 dígitos): ")
        while not validarContra(contraUsuario):
            print("Contraseña incorrecta. Debe ser un número de 4 dígitos.")
            contraUsuario = input("Reingrese su contraseña (4 dígitos): ")
        while not validarInicioSesion(mailUsuario, contraUsuario):
            print("Contraseña incorrecta.")
            contraUsuario = input("Reingrese su contraseña (4 dígitos): ")
        

        nombreUsuario,equipo = obtenerDatosUsuario(mailUsuario)
        print(f"¡Hola {nombreUsuario}!")
        return nombreUsuario, equipo    
    # Registro de usuario

    else: 
        mailUsuario = input("Ingrese su mail: ")
        while validarMailExistente(mailUsuario):
            print("Mail ya registrado!")
            mailUsuario = input("Reingrese su mail: ")
        contraUsuario = input("Ingrese su contraseña (4 dígitos): ")
        while not validarContra(contraUsuario):
            print("Contraseña incorrecta. Debe ser un número de 4 dígitos.")
            contraUsuario = input("Reingrese su contraseña (4 dígitos): ")
        nombreUsuario = input("Ingrese su nombre: ")
        equipos = ["Argentinos Juniors", "Atlético Tucumán", "Banfield", "Barracas Central", "Belgrano", "Boca Juniors", "Deportivo Riestra", "Defensa y Justicia", "Estudiantes", "Gimnasia", "Godoy Cruz", "Huracán", "Independiente", "Independiente de Rivadavia", "Instituto", "Lanús", "Newell's Old Boys", "Platense", "Racing", "River Plate", "Rosario Central", "Sarmiento", "San Lorenzo", "Talleres", "Tigre", "Unión", "Vélez", "Central Córdoba"]

        equipos_por_pagina = 7
        pagina_actual = 0

        def mostrar_equipos(pagina):
            inicio = pagina * equipos_por_pagina
            fin = inicio + equipos_por_pagina
            for i, equipo in enumerate(equipos[inicio:fin], start=1):
                print(f"{i}. {equipo}")
                
        while True:
            print("\nEquipos:")
            mostrar_equipos(pagina_actual)
            
            opcion = input("\nElige un equipo (1-7), 'n' para siguiente página, 'p' para anterior").lower()
            
            if opcion == 'n' and (pagina_actual + 1) * equipos_por_pagina < len(equipos):
                pagina_actual += 1
            elif opcion == 'p' and pagina_actual > 0:
                pagina_actual -= 1
            else:
                try:
                    eleccion = int(opcion) - 1
                    if 0 <= eleccion < equipos_por_pagina:
                        equipo = equipos[pagina_actual * equipos_por_pagina + eleccion]
                        print(f"\nHas elegido: {equipo}")
                        break
                except ValueError:
                    print("Opción no válida, intenta de nuevo.")

        sexo = input("Ingrese su sexo. M para Masculino, F para Femenino o X para otros: ")
        while not validarSexo(sexo):
            sexo = input("Sexo incorrecto, ingrese su sexo nuevamente. M para Masculino, F para Femenino o X para otros: ")
        
        registroCSV(mailUsuario, nombreUsuario, contraUsuario, equipo, sexo)
        
        print(f"¡Hola {nombreUsuario}, a llevar a {equipo} a la gloria!")
        return nombreUsuario, equipo

def registroCSV (mail, user, contra, team, sex):
    try:
        arch = open(r"Programacion1ProyectoUADE\Files\usuarios.csv", "at")
    except IOError:
        print("Error al abrir el archivo")
    else:
        arch.write(f"{mail};{user};{contra};{team};{sex}\n")
        arch.close()
    
def validarMailExistente(mail):
    try:
        arch = open(r"Programacion1ProyectoUADE\Files\usuarios.csv", "rt")
    except IOError:
        print("Error al abrir el archivo")
    else:
        for linea in arch:
            mailArchivo, x1, x2, x3, x4 = linea.strip().split(";")
            if mail == mailArchivo:
                return True
        arch.close()
        return False

def validarInicioSesion(mail, contra):
    try:
        arch =  open(r"Programacion1ProyectoUADE\Files\usuarios.csv", "rt")
    except IOError:
        print("Error al abrir el archivo")
    else:
        for linea in arch:
            mailArchivo, x1, contraArchivo, x2, x3 = linea.strip().split(";")
            if mail == mailArchivo and contra == contraArchivo:
                return True
        arch.close()
        return False
    
def obtenerDatosUsuario(mail):
    try:
        arch = open(r"Programacion1ProyectoUADE\Files\usuarios.csv", "rt")
    except IOError:
        print("Error al abrir el archivo")
    else:
        for linea in arch:
            mailArchivo, userArchivo, x1, equipo, x3 = linea.strip().split(";")
            if mail == mailArchivo:
                return userArchivo,equipo
        arch.close()






