def inicioSesion():
    usuarios = [
        ["eugeniavarando@gmail.com", "1234", "Eugenia Varando"],
        ["micaelacembal@gmail.com", "1605", "Micaela Cembal"],
        ["nicolasgiordano@gmail.com", "7234", "Nicolas Giordano"],
        ["valentinamannino@gmail.com", "3484", "Valentina Mannino"],
        ["nicolasumansky@gmail.com", "9653", "Nicolas Umansky"]
    ]

    validarMail = lambda mail: any(usuario[0] == mail for usuario in usuarios)
    validarContra = lambda contra: contra.isdigit() and len(contra) == 4
    validarInicio = lambda eleccion:  eleccion.isdigit() and decision in ['1', '2']
    
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
        
        while not any(usuario[0] == mailUsuario and usuario[1] == contraUsuario for usuario in usuarios):
            print("Contraseña incorrecta.")
            contraUsuario = input("Reingrese su contraseña (4 dígitos): ")

        obtenerNombreUsuario = lambda mail: [usuario[2] for usuario in usuarios if usuario[0] == mail][0]
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
        usuarios.append([mailUsuario, contraUsuario, nombreUsuario])
        print(f"¡Hola {nombreUsuario}!")
        return nombreUsuario

