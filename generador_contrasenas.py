import random
import string

def generar_contrasena(longitud, mayusculas, caracteres_especiales, puntuacion):
    # Conjunto de caracteres permitidos para la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Si el usuario ha indicado que se deben incluir mayúsculas, añadimos las letras mayúsculas al conjunto de caracteres
    if mayusculas:
        caracteres += string.ascii_uppercase

    # Si el usuario ha indicado que se deben incluir caracteres especiales, añadimos los caracteres especiales al conjunto de caracteres
    if caracteres_especiales:
        caracteres += string.punctuation
        
    if puntuacion:
        caracteres += string.punctuation

    # Generamos la contraseña al azar
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))

    # Mostramos la contraseña generada
    print(contrasena)

# Bucle principal del programa
while True:
    # Pedimos al usuario que indique la longitud de la contraseña
    longitud = int(input("Introduce la longitud de la contraseña: "))

    # Pedimos al usuario si desea incluir mayúsculas en la contraseña
    mayusculas = input("¿Desea incluir mayúsculas en la contraseña? (s/n)")
    if mayusculas.lower() == "s":
        mayusculas = True
    else:
        mayusculas = False

    # Pedimos al usuario si desea incluir caracteres especiales en la contraseña
    caracteres_especiales = input("¿Desea incluir caracteres especiales en la contraseña? (s/n)")
    if caracteres_especiales.lower() == "s":
        caracteres_especiales = True
    else:
        caracteres_especiales = False

    puntuacion = input("¿Desea incluir puntuacion en la contrasena? (s/n)")
    if puntuacion.lower() == "s":
        puntuacion = True
    else:
        puntuacion = False
        
    # Generamos una contraseña nueva
    generar_contrasena(longitud, mayusculas, caracteres_especiales, puntuacion)

    # Preguntamos al usuario si desea generar una nueva contraseña
    opcion = input("¿Desea generar una nueva contraseña? (s/n)")
    if opcion.lower() == "n":
        break
