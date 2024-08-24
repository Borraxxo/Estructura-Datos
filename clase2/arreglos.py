#son un tipo de dato que almacena una secuencia de valores 

arreglo1=[1,2,3,"cuatro","mama"]
print(arreglo1)
#los arreglos se pueden iniciar con corchetes o list()
#durante la ejecucion del codigo, sus calores pueden ser alterados 

arreglo1[3]=4
print(arreglo1)

#para adicionar otro valor al arreglo
arreglo1.append(7)
print(arreglo1)

#para pedir que el usuario ingrese un nuevo valor 
x=input("ingrese valor ")
arreglo1.append(x)
print(arreglo1)

#para agregar valor en una posocion especifica, en este caso en la primera posicion 

arreglo1.insert(0,9)
print(arreglo1)

#TUPLAS es similar solo que se inician con ()y la palabra clave tuple() arreglo1=(1,2,3,"cuatro","mama")
#no se pueden modificar los valores 


