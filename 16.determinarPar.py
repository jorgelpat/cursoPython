# Escriba un programa que determine si el número entero ingresado por el usuario es par o no.

numero = int(input("Ingrese un número: "))
if numero % 2 == 0 and numero != 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} no es par")