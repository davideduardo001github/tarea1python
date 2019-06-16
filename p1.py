"""
1.- Crear una función que reciba dos números como parámetros y que indique si el primer
número es múltiplo del segundo. Esta función debe ejecutarse en el flujo principal y debe
pedir los números al usuario.
"""

# Definición de la función

def multiplo(inp1,inp2):
    residuo = inp1%inp2
    if residuo == 0:
        return True
    else:
        return False


# Prueba de la función

inp1 = int(input("Escribe el primer número: "))
inp2 = int(input("Escribe el segundo número: "))
out1 = multiplo(inp1,inp2)
print("El número {0} es múltiplo de {1}: {2}".format(inp1,inp2,out1))
