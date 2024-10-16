def inicioSesion():

    #mails = ["eugeniavarando@gmail.com","micaelacembal@gmail.com", "nicolasgiordano@gmail.com", "valentinamannino@gmail.com", "nicolasumansky@gmail.com"]
    #userName = ["Eugenia Varando", "Micaela Cembal", "Nicolas Giordano", "Valentina Mannino", "Nicolas Umansky"]
    #contraseñas= ["1234","1605","7234","3484","9653"]
    
    validarInicio = lambda eleccion:  eleccion.isdigit() and decision in ['1', '2']
    validarMail = lambda mail: any(usuario == mail for usuario in mails)
    validarContra = lambda contra: contra.isdigit() and len(contra) == 4    
    obtenerNombreUsuario = lambda mail: [userName[i] for i in range(len(userName)) if mails[i] == mail][0] # Lista por comprensión con el nombre del usuario ingresado. 
    #validarUsuarioExistente = lambda mail, contra: any(mails[i] == mail and contraseñas[i] == contra for i in range(len(contraseñas)))
    validarSexo = lambda sex: sex.upper() == "M" or sex.upper() == "F" or sex.upper() == "X"

    decision = input("Presione 1 para Iniciar Sesión o 2 para Registrarse en su cuenta: ")
    while not validarInicio(decision):
        print("Opción incorrecta.")
        decision = input("Presione 1 para Iniciar Sesión o 2 para Registrarse en su cuenta: ")
   
    # Inicia Sesión
    if decision == '1':    
        mailUsuario = input("Ingrese su mail: ")
        while not validarMail(mailUsuario):
            print("Mail incorrecto.")
            mailUsuario = input("Reingrese su mail: ")
        contraUsuario = input("Ingrese su contraseña (4 dígitos): ")
        while not validarContra(contraUsuario):
            print("Contraseña incorrecta. Debe ser un número de 4 dígitos.")
            contraUsuario = input("Reingrese su contraseña (4 dígitos): ")
        
        #while not validarUsuarioExistente(mailUsuario, contraUsuario):
            #print("Contraseña incorrecta.")
            #contraUsuario = input("Reingrese su contraseña (4 dígitos): ")

        nombreUsuario = obtenerNombreUsuario(mailUsuario)
        print(f"¡Hola {nombreUsuario}!")
        return nombreUsuario 
    
    # Registro de usuario

    else: 
        mailUsuario = input("Ingrese su mail: ")
        while validarMail(mailUsuario):
            print("Mail ya registrado!")
            mailUsuario = input("Reingrese su mail: ")
        contraUsuario = input("Ingrese su contraseña (4 dígitos): ")
        while not validarContra(contraUsuario):
            print("Contraseña incorrecta. Debe ser un número de 4 dígitos.")
            contraUsuario = input("Reingrese su contraseña (4 dígitos): ")
        nombreUsuario = input("Ingrese su nombre: ")
        equipo = input("Ingrese con que equipo va a jugar: ")
        while not validarSexo(sexo):
            sexo = input("Sexo incorrecto, ingrese su sexo nuevamente. M para Masculino, F para Femenino o X para otros: ")

        # mails.append(mailUsuario)
        # userName.append(nombreUsuario)
        # contraseñas.append(contraUsuario)
        registroCSV(mailUsuario, nombreUsuario, contraUsuario,equipo,"F" )
        
        print(f"¡Hola {nombreUsuario}, a llevar a {equipo} a la gloria!")
        return nombreUsuario, equipo

def registroCSV (mail, user, contra, team, sex):
    try:
        arch = open(r"c:\Users\Pc\Documents\UADE - 1ER AÑO - 1ER CUATRIMESTRE\GitHub\Programacion1ProyectoUADE\Files\usuarios.csv", "at")
    except IOError:
        print("Error al abrir el archivo")
    else:
        arch.write(f"{mail};{user};{contra};{team};{sex}\n")
        arch.close()
    
