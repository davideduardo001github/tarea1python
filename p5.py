"""
5.- Dada una lista de cadenas de diferentes longitudes, crear una función que tome como
entrada dicha lista y la devuelva ordenada de la cadena más pequeña a la más larga.
"""
## Definición de la función
def sortlist(listinp):
    # Se cuentan el número de letra por palabra
    count = []
    for x in range( len(listinp) ):
        i = 0
        for y in listinp[x]:
            i += 1
        count.append(i)
    
    # Se ordena y se hace una copia de la lista
    ocount = count.copy()
    print
    count.sort()
    olistinp = listinp.copy()
    print(ocount)
    print(count)

    # Se reordena según la lista de referencia generada
    for x in range( len(ocount) ):
        for y in range( len(count) ):
            if ocount[x] == count[y]:
                # Se iguala a la lista original en la lista nueva y se destruye el lugar en la lista númerica asignando un valor negativo diferente para evitar el error en caso de repeticion en la longitud
                listinp[y] = olistinp[x]
                count[y] = -1
                ocount[x] = -2


## Prueba de la función
if __name__ == "__main__":
    
    #Prueba 1: Todas las palabras de diferente longitud
    list2 = ["Guajolote","Pez","Salamandra"]
    print("Lista sin ordenar:\n",list2)
    sortlist(list2)
    print("Lista ordenada:\n",list2)

    print()
    #Prueba 3: Dos palabras de la misma longitud
    list2 = ["salsa","mastodonte","mesas"]
    print("Lista sin ordenar:\n",list2)
    sortlist(list2)
    print("Lista ordenada:\n",list2)

    print()
    #Prueba 4: Tidas las palabras de la misma longitud
    list2 = ["mano","papa","gato"]
    print("Lista sin ordenar:\n",list2)
    sortlist(list2)
    print("Lista ordenada:\n",list2)