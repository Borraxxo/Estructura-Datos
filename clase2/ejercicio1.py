#crear un sistema de control de ingreso para evitar el sobrecupo 
#(definir cual va a ser el numero a controlar(antes de permitir el ingreso debe solicitar el boleto
#si el boleto no es valido mostrar el mensaje "acceso no permitido", de  lo contrario dejar ingresar y contar el cupo
#cuando el cupo se llene completamente mostrar un mensaje final "no se permiten mas ingreso"

control=0
cupo=int(input("ingrese cupo "))
while control<cupo:
    valido=input("voleto valido?")
    if valido== '1':
        print("ingresa persona")
        control=control+1
    else:
        print("persona no ingresa")

print("cupo lleno: ", control, "capacidad maxima")
