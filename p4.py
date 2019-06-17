"""
4.- Elabora un programa que me permita realizar la suma de dos matrices de 3x3. Cada uno
de los elementos de la matriz deberá ser ingresado por el usuario. Una matriz en Python puede
implementarse con listas dentro de listas.
"""
## DECLARACIÓN DE MÉTODOS

# Impresión de matrices nxn
def printmatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end = " ")
        print("\n")

# Generación de matrices por usuario
def genmatrix(rows, columns):
    mat = [[0] * rows for i in range(columns)]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = int(input("Ingresa el valor {0}x{1}: ".format(i+1,j+1)))
    return mat

# Suma de matrices
def summatrix(a,b):
    if ( len(a)==len(b) and len(a[0])==len(b[0]) ):
        rows = len(a)
        columns= len(a[0])
        matout = [[0] * rows for i in range(columns)]
        for i in range(rows):
            for j in range(columns):
                matout[i][j] = a[i][j] + b[i][j]
        return matout
    else:
        print("Las mátrices no son compatibles en suma")

# PRUEBA DEL MÉTODO
if __name__ == '__main__':
    print("Ingresa la matriz A")
    mat1 = genmatrix(2,2)
    print("Ingresa la matriz B")
    mat2 = genmatrix(2,2)
    print("La suma de las matrices es: ")
    printmatrix(summatrix(mat1,mat2))