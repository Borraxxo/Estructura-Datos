#una funcion es un bloque de codifigo encargado de realizar una operacion especifica, es definida por la palabra reservada: def 
#el nombre que no sean numeros ni mayusculas iniciales, no espacios y no caracteres 
# lleva parametros de entrada, los parametros van encerrados en (parentesis) 
#el fin de llamado de la funcion se finaliza con : (dos punto,esto solo en python), en otros lenguajes se cierra con  {llaves}
#la tabulacion derecha indica el bloque de codigo
#la funcion pueden o no retornar un valor 

 
#la -> es para tipar la funcion, para que devuelva un tipo de dato 
#def calcular_promedio(n1:int,n2:int,nombre:str)->int:
#    return 

#crear una funcion que calcule el factorial de un numero, como parametro de entrada, debe recibir el numero a calcular
def calculo_factorial(numero:int)->int|str:
    resultado=1
    if numero<0:
        return "no se puede caalcular el factorial de numeros negativos"
    for n in range(1, numero+1):
        resultado=resultado*n
    return resultado 

factorial = calculo_factorial(int(input("ingrese un numero ")))
print("el resultado es: ", factorial)
