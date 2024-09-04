
def inicioSesion():
    mailCorrecto = "eugenia@gmail.com"
    contraCorrecta = "1234"

    mailUsuario = input("Ingrese su mail: ")
    while mailUsuario != mailCorrecto:
        print("Mail incorrecto.")
        mailUsuario = input("Reingrese su mail: ")

    contraUsuario = input("Ingrese su contraseña (4 dígitos): ")
    while not (contraUsuario.isdigit() and len(contraUsuario) == 4):
        print("Contraseña incorrecta. Debe ser un número de 4 dígitos.")
        contraUsuario = input("Reingrese su contraseña (4 dígitos): ")
    
    while contraUsuario != contraCorrecta:
        print("Contraseña incorrecta.")
        contraUsuario = input("Reingrese su contraseña (4 dígitos): ")
    
    print("¡Bienvenida Eugenia!")
