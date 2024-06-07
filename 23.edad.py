import time
from datetime import datetime

print("Ingrese su fecha de Nacimiento: ")
dia = input("Dia: ")
mes = input("Mes: ")
anno = input("Año: ")

fechaNac = f"{anno}-{mes}-{dia}"

def calcularEdad(fechaNac):
    fechaNac = datetime.strptime(fechaNac,"%Y-%m-%d")
    fechaActual = datetime.now()
    edad = fechaActual.year - fechaNac.year
    if (fechaActual.month, fechaActual.day) < (fechaNac.month, fechaNac.day):
        edad -= 1
    return edad

edad = calcularEdad(fechaNac)
print(f"Usted tiene {edad} años")