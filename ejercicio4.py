# Ejercicio 4. Escribe un programa que pida al usuario una frase y muestre por pantalla el
# número de veces que contiene cada vocal


frase = str(input("Introduce una frase: "))

frase = list(frase)


print(frase)

print("\n")

vecesA = frase.count("a") + frase.count("A") + frase.count("á") + frase.count("Á")
vecesE = frase.count("e") + frase.count("E") + frase.count("é") + frase.count("É")
vecesI = frase.count("i") + frase.count("I") + frase.count("í") + frase.count("Í")
vecesO = frase.count("o") + frase.count("O") + frase.count("ó") + frase.count("Ó")
vecesU = frase.count("u") + frase.count("U") + frase.count("ú") + frase.count("Ú")

print("Número de veces que aparece la letra A: " + str(vecesA))
print("Número de veces que aparece la letra E: " + str(vecesE))
print("Número de veces que aparece la letra I: " + str(vecesI))
print("Número de veces que aparece la letra O: " + str(vecesO))
print("Número de veces que aparece la letra U: " + str(vecesU))
