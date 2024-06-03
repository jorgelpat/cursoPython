import math

# def raizCuadrada(x):
#     return math.sqrt(x)

catetoA = int(input("Ingrese cateto a: "))
catetoB = int(input("Ingrese cateto b: "))

hipotenusa = math.sqrt((catetoA**2)+(catetoB**2))

print(f"la hipotenusa es {hipotenusa}")