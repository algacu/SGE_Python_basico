# Ejercicio 5. Escribe un programa en el que el usuario introduzca un número entero y el
# programa genere una frase con las palabras correspondientes a cada cifra. Por
# ejemplo, 547 devolvería "cinco cuatro siete". Las palabras desde el "cero"
# hasta el "nueve" están almacenadas en una lista

palabras = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]

numero = str(input("Introduce un número: "))

numeros = list(numero)

frase = ""

for numero in numeros:
    frase += palabras[int(numero)] + " "

print(frase)
