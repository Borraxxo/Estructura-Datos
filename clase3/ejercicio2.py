#crear una funcion que convierta temperatura celcius a farenheit 
def temperatura(celcius:float)->float:
    farenheit=((celcius*9)/5)+32
    return farenheit
farenheit=temperatura(float(input("ingrese temperatura en celcius para convertirla a farenheit ")))
print("la conversion a farenheit es: ", farenheit)