# *******************************************************************************
# Empresa: OvniOn
#
# Aplicación: Calculadora de 6 operaciones
#
# Destinado a: personas de todas las edades y niveles.
#
# Descripción del funcionamiento:
#   Muestra opciones de operaciones y solicita al usuario que ingrese
#   una opcion. Entonces permite realizar esa operación con los números
#   elegidos por el usuario y luego informa el resultado.
# *******************************************************************************

import math

# Calculadora para realizar operaciones matemáticas (6)

while True:
    print("**********************************************")
    print("Bienvenido a la calculadora de 6 operaciones")
    print("**********************************************")

    print("************ MENÚ DE OPERACIONES **************")
    print("1- SUMA")
    print("1- RESTA")
    print("1- MULTIPLICACIÓN")
    print("1- DIVISIÓN")
    print("5- POTENCIACIÓN")
    print("6- RADICACIÓN")
    print("**********************************************")

    opcion = int(input("Ingrese una opción de operación: "))

    # Comienza la lógica del programa.

    print("************* Inicia aplicación *************")

    if opcion == 1:
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
        suma = numero1 + numero2
        print(f"El resultado de sumar {numero1} y {numero2} es: {suma}")
    elif opcion == 2:
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
        resta = numero1 ** numero2
        print(f"El resultado de restar {numero1} y {numero2} es: {resta}")



    elif opcion == 6:
        numero1 = int(input("Ingrese el primer número: "))
        radicacion = math.sqrt(numero1)
        print(f"El resultado de la raiz cuadrada de {numero1} es: {radicacion}")
    
    
    
    else:
        print("Ingresó una opción incorrecta. Vuelvalo a intentar.")    