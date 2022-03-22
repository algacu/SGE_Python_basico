# Ejercicio 6. Escribe un programa que indique cuántas palabras diferentes hay en El
# Quijote (archivo el_quijote.txt), mostrándolas antes en orden
# alfabético.

import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'hola.txt')

with open(my_file, encoding="utf8") as f:
    contenido = f.read()

caracteres = ",.;-¿?¡!:«»–‘‘“()''[]/\"0123456789"
contenido = ''.join( x for x in contenido if x not in caracteres)    

contenido = contenido.split()
palabras = list()

for palabra in contenido:
    palabras.append(palabra.lower())

palabras.sort()

noRepetidas = list()
total = list()

for palabra in palabras:
    if palabra not in noRepetidas:
        noRepetidas.append(palabra)


print(palabras)
print("\nEl Quijote contiene un total de " + str(len(palabras)) + " palabras, de las que " + str(len(noRepetidas)) + " son diferentes.")