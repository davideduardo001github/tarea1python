"""
3.- Escribe una función que cuente el número de vocales en una cadena dad
"""
# Defninición de la función
def vocalcount(cadena):
    n = 0
    for x in cadena:
        if (x == "a" or x == "e" or x== "i" or x== "o" or x == "u"):
            n += 1
        if (x == "A" or x == "E" or x== "I" or x== "O" or x == "U"):
            n += 1
    return n

# Prueba de la función
if __name__ == '__main__':

    input1 = input("Escribe un texto: ")
    nvoc = vocalcount(input1)
    print("El número de vocales es: ",nvoc)