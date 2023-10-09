# PROBLEMA:Un usuario necesita calcular la SUMA y la RESTA de 2 números.
# SOLUCIÓN:Crear un algoritmo que solucione el problema.
# PROGRAMA:La solucion va a ser un programa para calcular la suma y la resta de 2 números.

while True:
    # PASO 1: Pedir al usuario que ingrese los numeros a operar.

    numero1 = int(input("Ingrese El Número 1:"))
    numero2 = int(input("Ingrese el Número 2: "))
    
    # PASO2: Mostrar el menu de  operacion.
    
    print("Ingrese La Opcion que desea Realizar:")
    print("Para suma es Opcion 1.")
    print("Para resta es Opcion 2.")



    # PASO3: Pedir al usuario ingrese una opcion.

    opcion = int (input("Ingrese su opcion:"))


    #PASO4: Realizar la operación que selecciono el usuario.

    if opcion==1:
        resultado=numero1+numero2
    else: opcion==2
    resultado=numero1-numero2


    #PASO5: Mostrar el resultado de la operacion que eligio el usuario.
    print(f"{resultado}")

 