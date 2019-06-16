"""
2.- Se tiene una lista de números ordenados de forma creciente en el que todos los números
(excepto uno) aparecen duplicados. Realiza un programa que encuentre el número que no
está duplicado dentro de la lista.
Ejemplo, para la lista [1, 1, 3, 3, 4, 5, 5, 6, 6, 7, 7], el programa devuelve 4.
"""

# Definiendo la función

def findnotrepeat(inplist1):
    i = 0
    while i < len(inplist1):
        if (i+1) == len(inplist1):
            return inplist1[i]
        elif inplist1[i] != inplist1[i+1]:
            return inplist1[i]
        else:
            i += 2
    

    return "Todos tienen un par dentro de la lista"

# Prueba de la función

testlist = (1, 3, 3, 4, 4, 5, 5)
unrepited = findnotrepeat(testlist)
print("El número sin repetir es: ",unrepited)



