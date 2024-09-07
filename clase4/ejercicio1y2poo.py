#"  Crear una clase llamada Vehículo, esta clase debe recibir 2 parámetros, marca y combustible; 
# la clase también debe contener dos métodos encender y arrancar. 
# Instanciar la clase y usar el método mágico __str__ para imprimir la marca y el combustible usado "

class Vehiculo:
    def __init__(self,marca:str,combustible:str):
        self.marca=marca
        self.combustible=combustible
    def encender(self):
        pass
    def arrancar(self):
        pass
    #metodo magico str
    def __str__(self):
        return f"el vehiculo {self.marca} utiliza combustible {self.combustible}"
    #instanciar una clase
carro=Vehiculo("bmw","extra")
print(carro)
print(type(carro))


#ejercicio 2 
#"Crear dos clases, Moto y Carro, estas clases deben estar heradadas de la clase Vehiculo.
# Realizar dos instancias de las nuevas clases creadas e imprimir el objeto instanciado"

class Moto(Vehiculo):
    def __init__(self,marca:str,combustible:str):
        super(). __init__(marca,combustible)    #no es necesario porque son los mismos parametros entonces con un pass es suficiente, pero si se le desea agregar un nuevo parametro toca hacerlo de nuevo


class Carro(Vehiculo):
    pass     #aqui solo se pone pass, es la otra forma lo que dije en el comentario de super en moto 
     
motora=Moto("yamaha","corriente")
mi_carro=Carro("mercedez", "extra")
print(motora)
print(mi_carro)
