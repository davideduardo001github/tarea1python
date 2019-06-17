"""
6.- Elabora un programa que sea capaz de calcular el IMC (Índice de masa corporal) de una
persona. Los datos deberán ser ingresados por el usuario.
"""

## Definición de la función

def IMC(weight,height):
    imc = (weight*100*100)/(height*height)
    return round(imc,2)

## Prueba de la función

if __name__ == "__main__":
    weight = int(input("Ingrese su peso en KG: "))
    height = int(input("Ingrese su altura en centimetros: "))
    print("Su IMC es: ",IMC(weight,height))