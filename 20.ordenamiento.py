# Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:

numero1 = input("Ingrese numero: ")
numero2 = input("Ingrese numero: ")

if int(numero1) > int(numero2):
    print(f"{numero2} {numero1}")
elif int(numero1) < int(numero2):
    print(f"{numero1} {numero2}")
else:
    print(f"{numero1} y {numero2} son iguales")