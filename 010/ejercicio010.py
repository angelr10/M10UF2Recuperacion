import random


numeroAdivinar = random.randint(0,100)
insertadoUsuario = int(input("Intenta adivinar el numero que pienso del 0 al 100..."))
while(insertadoUsuario!=numeroAdivinar):
    print("Incorrecto!!!")
    if(insertadoUsuario>numeroAdivinar):
        print("El numero a adivinar es mas pequeño.")
    else:
        print("El numero a adivinar es mas grande.")
    insertadoUsuario = int(input("Intentalo otra vez: "))
print("HAS ACERTADO EL NUMERO ERA ",numeroAdivinar,"!!!")