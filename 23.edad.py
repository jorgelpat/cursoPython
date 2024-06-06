import time

print("Ingrese su fecha de Nacimiento: ")
dia = input("Dia: ")
mes = input("Mes: ")
anno = input("Año: ")

def calcularEdad(fechaNac):
    fechaActual = time.localtime()
    annoActual = fechaActual.tm_year
    mesActual = fechaActual.tm_mon
    diaActual = fechaActual.tm_mday

    dia, mes, anno = fechaNac

    edad = annoActual - anno

    return edad

fechaNac = (dia, mes, anno)

edad = calcularEdad()

print(f"La persona tiene {edad} años")