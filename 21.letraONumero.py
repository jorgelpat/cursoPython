caracter = input("Ingrese caracter: ")

while len(caracter) != 1:
    caracter = input("Un solo caracter, por favor. Intente de nuevo: ")
    if len(caracter) == 1:
        break

def caracterType(carac):
    if carac.isdigit():
        return "Es número"
    elif carac.isalpha() and carac.isupper():
        return "Es una letra mayúscula"
    elif carac.isalpha() and carac.islower():
        return "Es una letra minúscula"
    else:
        return "No es letra ni número"

print(caracterType(caracter))
