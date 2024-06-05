# Escriba un programa que pregunte al usuario la hora actual t del reloj 
# y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

t = int(input("Hora actual: "))
h = int(input("Cantidad de horas: "))

suma = t+h

while suma > 12:
    suma = suma - 12

print(f"En {h} horas el reloj marcará las {suma}")