import math

t = 0
m = 47
p = 1.038
c = 3.7
k = (5.4)*(10**-3) #math.pow(10,-3)
tW = 100
tO = float(input("Ingrese la temperatura original del huevo: "))
tY = 70

t = ((math.pow(m,2/3)*c*(math.pow(p,1/3)))/(k*math.pow(math.pi,2)*math.pow((4*math.pi)/3,2/3)))*math.log(0.76*((tO-tW)/(tY-tW)))

print(f"El tiempo que le toma en alcanzar la temperatura maxima es de {int(t)} segundos")