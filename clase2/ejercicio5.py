#calcular la factorial de un numero dado 
factorial=int(input("ingrese un numero "))
x=1
for i in range(1,factorial+1):
    x *=i
print(x)
