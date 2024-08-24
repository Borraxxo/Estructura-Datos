#ejercicio 3 crear un arreglo con 10 numeros aleatorios imprimir en pantalla el promedio de estos numeros 

import random
numero=random.randint(1,30)
suma=0

for i in range(1,11):
    numero=random.randint(1,30)
    print(f"numero aleatorio #{i}: ", numero)
    suma+=numero
prom=(suma/10)
print("el promedio de las 10 notas es: ", prom)
