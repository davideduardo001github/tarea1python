"""
7.- Con ayuda de diccionarios y listas, elabora un programa que simule una agenda de
contactos. El programa debe preguntar al usuario si desea agregar un nuevo contacto a su
agenda; si el usuario responde que sí, deberá pedir datos como “nombre” y “teléfono”; en
caso contrario deberá mostrar todos los usuarios agregados en la agenda y termina la
ejecución del programa.
"""
## DESARROLLO DEL CÓDIGO

# Variables globales
agenda = {}

# Funciones del programa

# Agregar contacto
def addcontact(dicinp):
    nombre = input("Escribe el nombre del contacto: ")
    telefono = int( input("Escribe el télefono de {0}: ".format(nombre)) )
    dicinp[nombre] = telefono
    print("Contacto agregado exitosamente")
    print()

# Ver agenda
def printcontacts(dicinp):
    print("Nombre\t\tTeléfono")
    for x,y in dicinp.items():
        print (x,"\t->\t",y)


## EJECUCIÓN DEL PROGRAMA
while True:
    print("\n Bienvenido a tu agenda\n")
    print("1) Agregar un contacto")
    print("2) Ver la agenda completa")
    print("3) Salir")
    option = int(input("\nElige una opción: "))
    if option == 1:
        addcontact(agenda)
    elif option == 2:
        printcontacts(agenda)
    elif option == 3:
        break
    else:
        print("Escribe una opción válida")
print("Vuelve pronto!")