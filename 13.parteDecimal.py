# Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

numero = float(input("Ingrese un numero: "))
parteDecimal = numero - int(numero)
print(parteDecimal)