# Escriba un programa que pida al usuario un entero de tres dígitos, 
# y entregue el número con los dígitos en orden inverso:

def numeroInvertido(x):
    invertido = x[::-1]
    invertido = int(invertido)
    return invertido

numero = input("Indique un numero de 3 digitos: ")
# while len(numero) != 3 and numero.isdigit == True:
#     numero = input("Vuelve a intentar... 3 digitos: ")

print(numeroInvertido(numero))
