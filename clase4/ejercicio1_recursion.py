#realizar una multiplicacion de dos numeros por medio de sumas
#a=2
#b=3
#suma=0
#while a>0: #control del ciclo
  #  suma=suma+b  #operacion de suma 
 #   a=a-1  #reduce la variable de control a 0
#print(suma)

#ahora pasar esto a recursion 

def multiplicacion(a:int, b:int)->int:
    if a==0:
        return 0
    return b +multiplicacion(a-1,b) 

print(multiplicacion(4,5))

#