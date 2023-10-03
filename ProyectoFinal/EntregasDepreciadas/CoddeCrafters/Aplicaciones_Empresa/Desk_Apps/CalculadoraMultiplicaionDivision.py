# PROBLEMA:un usuario necesita calcular la MULTIPLICACION y la DIVISION de 2 numeros.
# SOLUCION:Crear un algoritmo que solucione un problema.
# PROGRAMA: La solucion va a ser un programa para calcular la MULTIPLICACION y la DIVISION de 2 numero.
while True:
# PASO 1: Pedir al usuario que ingrese los numeros a operar.

    numero1 = int(input("ingrese el primer numero"))
    numero2 = int(input("ingrese el segundo numero"))
    # paso 2:mostrar menu de operaciones.

    print("menu")
    print("1- multiplicacion")
    print("2- division")




    #PASO 3: Pedir al usuario que ingrese una opcion

    opcion = int(input("ingrese una opcion "))

    # Paso 4: Realizar la operacion que selecciono el usuario
    if opcion ==1:
        resultado=numero1 * numero2
    else:
        resultado= numero1 / numero2
        
    #Paso 5
    print(f"{resultado}")
    