# Ejercicio 2. Escribe un programa que vaya preguntando al usuario los números ganadores
# de la lotería de Navidad, los vaya almacenando en una lista y, cuando
# introduzca un -1 para finalizar, los muestre por pantalla ordenados de menor a mayor.

numeros = list()
num = 0

while (num != -1):
    num = int(input("Introduce un número de la lotería de Navidad (escribe '1' para terminar): "))
    if (num != -1):
        numeros.append(num)

numeros.sort()

for num in numeros:
    print(num)