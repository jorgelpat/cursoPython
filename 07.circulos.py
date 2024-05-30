# Escriba un programa que reciba como entrada el radio de un círculo y 
# entregue como salida su perímetro y su área:

import math

radio = float(input("Indique el radio del circulo en cm:\n"))
area = math.pi*((radio)**2)
perimetro = 2*(math.pi)*radio
print(f"El area del ciruclo es {area}cm cuadrados")
print(f"El perimetro del circulo es {perimetro}cm")