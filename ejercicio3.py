# Ejercicio 3. Escribe un programa que almacene los módulos de 2º DAM (PSP, AAD, PMM,
# DIN, SGE, etc.) en una lista, pregunte al usuario la nota que ha sacado en cada
# módulo y elimine de la lista los módulos aprobados. Al final, el programa debe
# mostrar por pantalla los módulos que el usuario tiene que recuperar en junio.

modulos = ["SYP", "ADD", "PMM", "DIN", "SGE", "EIE"]
notas = list()
aprobados = list()

for modulo in modulos:
    nota = int(input("Introduce la nota que has sacado en " + modulo + ": "))
    if (nota >= 5):
        aprobados.append(modulo)

for moduloAprobado in aprobados:
    for modulo in modulos:
        if (moduloAprobado == modulo):
            modulos.remove(modulo)

print("\nMódulos a recuperar en junio:")
for modulo in modulos:
    print(modulo)