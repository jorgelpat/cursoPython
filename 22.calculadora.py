operando1 = input("Operando: ")

while operando1.isdigit() == False:
    print(f"{operando1} no es un digito, vuelve a intentarlo: ")
    operando1 = input("Operando: ")
    if operando1.isdigit():
        break

operator = input("Operador: ")

while operator != "+" or operator != "-" or operator != "*" or operator != "/":
        print(f"{operator} no es un operador básico, vuelve a intentarlo: ")
        operator = input("Operador: ")
        if operator == "+" or operator == "-" or operator == "*" or operator == "/":
             break


operando2 = input("Operando: ")

while operando2.isdigit() == False:
    print(f"{operando2} no es un digito, vuelve a intentarlo: ")
    operando2 = input("Operando: ")
    if operando2.isdigit():
        break

def operacion(x,y,z):
    if y == "+":
        return x+z
    elif y == "-":
        return x-z
    elif y == "*":
        return x*z
    else:
        return x/z
    
print(f"{operando1} {operator} {operando2} = {operacion(operando1,operator,operando2)}")

# Solucionar problema