edad = 22
print(edad)
edad = int(input("Introduce tu edad: "))  # Ask the user for their age

if edad < 18:
    print("No puedes entrar.")  # Message if they are under 18
else:
    print("Puedes entrar.")   # Message if they are 18 or older  
    
nombre = input("Introduce tu nombre: ")  # Ask for the name
edad = int(input("Introduce tu edad: "))   # Ask for the age

print("Hola", nombre + ", tienes", edad, "años.")  # Display name and age 

