#verificar si una palabra dada es un palindromo 
def idf_palindromo(palabra:str)->str:
    txt=palabra[::-1]
    if palabra==txt:
        return f"la palabra ingresada es un palindromo"
    else:
        return f"la palabra ingresada es una palabra normal"

palabra=input("ingrese una palabra si desea saber si es palindromo ")
print(idf_palindromo(palabra))