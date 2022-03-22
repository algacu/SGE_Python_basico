# Ejercicio 1. Escribe un programa que vaya pidiendo palabras al usuario hasta que este
# introduzca "FIN" y, tras ello, muestre las palabras en orden alfabético inverso.

from audioop import reverse

palabras = list()
palabra = ""

while (palabra != "FIN" and palabra != "fin"):
    palabra = str(input("Introduce una palabra (escribe 'FIN' para terminar): "))
    if (palabra != "FIN" and palabra != "fin"):
        palabras.append(palabra)

palabras.sort(reverse=True)

for palabra in palabras:
    print(palabra)