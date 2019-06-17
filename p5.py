"""
5.- Dada una lista de cadenas de diferentes longitudes, crear una función que tome como
entrada dicha lista y la devuelva ordenada de la cadena más pequeña a la más larga.
"""
## Definición de la función
def sortlist(lstinp):
    lstinp.sort(reverse = True)

## Prueba de la función
if __name__ == "__main__":
    list1 = ["Esta es una prueba de ordenamiento","Pato","Hola a todos"]
    print(list1)
    sortlist(list1)
    print(list1)

