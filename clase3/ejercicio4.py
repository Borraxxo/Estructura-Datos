#crear una funcion que genere contraseñas aleatorias, la cantidad de caracteres a generaar se envia por parametro
import random

def contraseña_ale(num:int)->int|str:
    caracteres="abcdefghijklnñmopqrstuvwxyz0123456789"
    contra= "".join((random.choice(caracteres))for _ in range(num))

    return contra
num=int(input("ingrese el numero de caracteres que desea en su contraseña "))
aleatorio=contraseña_ale(num)
print("su contraseña es: ", aleatorio)

