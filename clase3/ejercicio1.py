#crear una funcion que realize ooperaciones basicas(+,-,*,/)entre dos numeros 
def operaciones_basicas(num1:int,num2:int,op:int)->int:
    if op==1:
        suma=num1+num2

    elif op==2:
        resta=num1-num2
       

    elif op==3:
        mult=num1*num2
       

    if op==4:
        div=num1/num2
        
    return op

num1=int(input("digite un numero "))
num2=int(input("ingrese otro numero "))
operacion= operaciones_basicas(num1,num2)
print("el resultado de su operacion es: ", operacion)



