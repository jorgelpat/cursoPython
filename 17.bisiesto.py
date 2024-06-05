anno = int(input("Ingrese un año: "))

if anno > 1582:
    if anno % 100 == 0 and anno % 400 != 0:
        print(f"{anno} no es bisiesto")
    elif anno % 4 == 0:
        print(f"{anno} es bisiesto")
    else:
        print(f"{anno} no es bisiesto")

if anno <= 1582 and anno % 4 == 0:
    print(f"{anno} es bisiesto")