import math

nc = 0

c1 = int(input("Nota certamen 1: "))
c2 = int(input("Nota certamen 2: "))
lab = int(input("Nota laboratorio: "))

nf = 60
nc = (nf-(lab*0.3))/0.7
c3 = (nc*3)-(c1+c2)

# redondeamos el flotante al siguiente entero con math.ceil()
print(f"Necesita nota {math.ceil(c3)} en el certamen 3")
