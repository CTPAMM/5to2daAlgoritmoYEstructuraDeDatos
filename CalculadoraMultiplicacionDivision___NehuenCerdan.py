# PROBLEMA: UN usuario necesita calcular la MULTIPLICACION y la DIVISION de 2 numeros.
# SOLUCION: Crear un algoritmo que solucione su problema.
# PROGRAMA: La solucion va a ser un programa para calcular la multiplicacion y la division de 3 numeros.

while True:
    # PASO 1: Pedir al usuario que ingrese los numeros a operar.

    numero1 = int(input("Ingrese el numero: "))
    numero2 = int(input("Ingrede el otro numero: "))

    # PASO 2: mostrar menu de operaciones.

    print("1. Para multiplicar")
    print("2. Para dividir")


    # PASO 3: Pedir al usuario ingrese una opcion.

    opcion = int(input("ingrese su opcion"))

    # PASO 4: Realizar la opreracion que selecciono el usuario.

    if opcion ==1:
        resultado = numero1 * numero2
    else:
        resultado = numero1 / numero2
        
    # PASO 5: Mostrar el resultado de la opreacion al usuario.

    print(f"{resultado}") 
