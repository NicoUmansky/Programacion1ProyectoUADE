def inicioSesion():
    mailCorrecto = "eugenia@gmail.com"
    contraCorrecta = "1234"

    validarMail = lambda mail: mail == mailCorrecto
    validarContra = lambda contra: contra.isdigit() and len(contra) == 4
    validarContraCorrecta = lambda contra: contra == contraCorrecta

    mailUsuario = input("Ingrese su mail: ")
    while not validarMail(mailUsuario):
        print("Mail incorrecto.")
        mailUsuario = input("Reingrese su mail: ")

    contraUsuario = input("Ingrese su contraseña (4 dígitos): ")
    while not validarContra(contraUsuario):
        print("Contraseña incorrecta. Debe ser un número de 4 dígitos.")
        contraUsuario = input("Reingrese su contraseña (4 dígitos): ")
    
    while not validarContraCorrecta(contraUsuario):
        print("Contraseña incorrecta.")
        contraUsuario = input("Reingrese su contraseña (4 dígitos): ")
    
    print("¡Bienvenida Eugenia!")

