rutaArchivo1 = r"Programacion1ProyectoUADE\Files\usuarios.csv" 
rutaArchivo2 = r"Files\usuarios.csv"

rutaElegida = rutaArchivo2

cyan = '\x1b[36m'
yellow = '\x1b[33m'
white = '\x1b[37m'
green = '\x1b[32m'
red = '\x1b[31m'
blue = '\x1b[34m'
reset = '\x1b[0m'

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
        nombreUsuario = input("Ingrese su nombre de usuario: ")
        while validarNombreUsuario(nombreUsuario):
            print("Nombre ya existente!")
            nombreUsuario = input("Reingrese su nombre de usuario: ")
        equipos = ["Argentinos Juniors", "Atlético Tucuman", "Banfield", "Barracas Central", "Belgrano", "Boca Juniors", "Deportivo Riestra", "Defensa y Justicia", "Estudiantes", "Gimnasia", "Godoy Cruz", "Huracan", "Independiente", "Independiente de Rivadavia", "Instituto", "Lanus", "Newell's Old Boys", "Platense", "Racing", "River Plate", "Rosario Central", "Sarmiento", "San Lorenzo", "Talleres", "Tigre", "Union", "Velez", "Central Cordoba"]

        equiposPorPagina = 7
        paginaActual = 0

        def mostrarEquipos(pagina):
            inicio = pagina * equiposPorPagina
            fin = inicio + equiposPorPagina
            for i, equipo in enumerate(equipos[inicio:fin], start=1):
                print(f"{white}{i}. {equipo}{reset}")
                
        while True:
            print("\n" + white + "Equipos:")
            mostrarEquipos(paginaActual)
            
            opcion = input("\nElige un equipo (1-7), 'n' para siguiente página, 'p' para anterior: ").lower()
            
            if opcion == 'n' and (paginaActual + 1) * equiposPorPagina < len(equipos):
                paginaActual += 1
            elif opcion == 'p' and paginaActual > 0:
                paginaActual -= 1
            else:
                try:
                    eleccion = int(opcion) - 1
                    if 0 <= eleccion < equiposPorPagina:
                        equipo = equipos[paginaActual * equiposPorPagina + eleccion]
                        print(f"\nHas elegido: {green}{equipo}{reset}")
                        break
                except ValueError:
                    print(red + "Opción no válida, intenta de nuevo."+ reset)

        sexo = input("Ingrese su sexo. M para Masculino, F para Femenino o X para otros: ")
        while not validarSexo(sexo):
            sexo = input("Sexo incorrecto, ingrese su sexo nuevamente. M para Masculino, F para Femenino o X para otros: ")
        
        registroCSV(mailUsuario, nombreUsuario, contraUsuario, equipo, sexo.upper())
        
        print(f"¡Hola {nombreUsuario}, a llevar a {equipo} a la gloria!")
        return nombreUsuario, equipo

def registroCSV (mail, user, contra, team, sex):
    try:
        arch = open(rutaElegida, "at")
    except IOError:
        print("Error al abrir el archivo")
    else:
        arch.write(f"{mail};{user};{contra};{team};{sex}\n")
        arch.close()
    
def validarMailExistente(mail):
    try:
        arch = open(rutaElegida, "rt")
    except IOError:
        print("Error al abrir el archivo")
    else:
        for linea in arch:
            mailArchivo, x1, x2, x3, x4 = linea.strip().split(";")
            if mail.lower() == mailArchivo.lower():
                return True
        arch.close()
        return False

def validarNombreUsuario(nombreUsuario):
    try:
        arch = open(rutaElegida, "rt")
    except IOError:
        print("Error al abrir el archivo")
    else:
        for linea in arch:
            x0, nombreUsuarioArchivo, x2, x3, x4 = linea.strip().split(";")
            if nombreUsuario.lower() == nombreUsuarioArchivo.lower():
                return True
        arch.close()
        return False
    
    
def validarInicioSesion(mail, contra):
    try:
        arch = open(rutaElegida, "rt")
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
       arch = open(rutaElegida, "rt")
    except IOError:
        print("Error al abrir el archivo")
    else:
        for linea in arch:
            mailArchivo, userArchivo, x1, equipo, x3 = linea.strip().split(";")
            if mail == mailArchivo:
                return userArchivo,equipo
        arch.close()






