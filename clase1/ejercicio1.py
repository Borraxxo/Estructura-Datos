# Suggested code may be subject to a license. Learn more: ~LicenseLog:3403999852.
numero1= int(input("ingrese el primer numero: "))
numero2= int(input("ingrese el segundo numero: "))
numero3= int(input("ingrese el tercer numero: "))
if numero1>numero2:
    if numero1>numero3:
        print("el numero mayor es: ",numero1)
    else:
        print("el numero mayor es: ",numero3)
elif numero2>numero3:
    print("el numero mayor es el: ", numero2)

if numero1<numero2:
    if numero1<numero3:
        print("el numero menor es: ",numero1)
    else:
        print("el numero menor es: ",numero3)
elif numero2<numero3:
    print("el numero menor es el: ", numero2)
