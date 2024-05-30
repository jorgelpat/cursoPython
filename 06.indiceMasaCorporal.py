# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, 
# y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde 
# <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso = float(input("Indique su peso en Kg: \n"))
estatura = float(input("Indique su estatura en metros: \n"))
imc = (peso/(estatura)**2)
print(f"El indice de masa corporal es de {imc}")

