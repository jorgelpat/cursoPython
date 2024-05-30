# Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:

cantidad = 4
suma = 0
for i in range(cantidad):
    nota = float(input("nota: "))
    suma = nota + suma

promedio = suma/4
print(f"promedio es = {promedio}")