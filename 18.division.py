# Escriba un programa que pida dos números enteros y que calcule la división, 
# indicando si la división es exacta o no.

dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

cociente = int(dividendo / divisor)
resto = dividendo % divisor

if dividendo % divisor == 0:
    print("La division es exacta")
    print(f"Cociente: {cociente}")
    print(f"Resto: {resto}")
else:
    print("La division no es exacta")
    print(f"Cociente: {cociente}")
    print(f"Resto: {resto}")