# FRANCO PIEROTTI 5to 2da
# PROBLEMA: Un usuario necesita calcualr la multiplicacion y division de 2 numeros
# SOLUCION: Crear un algoritmo que soluciones su problema
# PROGRAMA: la solucion va a ser un programa para calcular la multiplicacion y division de 2 numeros

while True:
    # PASO 1: Pedir al usuario que ingrese los numeros a operar

    numero1 = int(input("ingrese el 1er numero"))
    numero2 = int (input("ingrese el 2do numero"))

    # PASO 2: Mostrar menu de opciones

    print("1_multiplicacion")
    print("2_division")

    # PASO 3: Pedir al usuario que ingrese una opcion

    opcion = input("ingrese una operacion = ")

    # PASO 4: Realizar la operacion que selecciono el usuario

    if opcion ==1:
        resultado = numero1 * numero2
    else:
        resultado = numero1 / numero2
        
    # PASO 5: Mostrar el resultado de la operacion al usuario 

    print(f"{resultado}") 