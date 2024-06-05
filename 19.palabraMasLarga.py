word1 = input("Palabra 1: ")
word2 = input("palabra 2: ")

def palabraLarga(x,y):
    if len(x) > len(y):
        diferencia = len(x) - len(y)
        return (f"La palabra {x} tiene {diferencia} letras mas que {y}")
    elif len(y) > len(x):
        diferencia = len(y) - len(x)
        return (f"La palabra {y} tiene {diferencia} letras mas que {x}")
    else:
        return("Las 2 palabras tienen el mismo largo")

print(palabraLarga(word1,word2))