peso= float(input("ingrese su peso en kg "))
altura= float(input("ingrese su altura en metros "))
imc=peso/(altura*altura)
print("su imc es: ", imc)
if imc>25:
    print("usted esta en sobrepeso")
elif imc<18.5:
    print("usted esta en bajo peso")
else:
    print("usted esta normal")
