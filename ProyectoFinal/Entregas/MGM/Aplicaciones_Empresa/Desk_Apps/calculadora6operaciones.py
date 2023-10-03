#clacluladora para realizar operaciones matematicas (6)

# Iterar infinitamente todo el programa

while True:
    # Imprimir en pantalla el menú de opciones
    
    print("*******************************")
    print("bienvenido a la calculadora de 6 operaciones")
    print("*******************************")

    print("********** MENU DE OPERACIONES ***************")
    print("1- SUMAR")
    print("2- RESTA")
    print("3- MULTIPLICACIÓN")
    print("4- DIVISIÓN")
    print("5- POTENCIACIÓN")
    print("6- RADICACIÓN")
    print("*******************************")

    # Pedir al usuario ingrese una opción del menú

    opción = int(input("ingrese una opción de operación"))

    # Pedir al usuario ingrese los números a operar

    numero1 = input("ingrese el primer número: ")  # Profe: convertir el input a int
    numero2 = input("ingrese el segundo número: ")

    # Decidir la operación a realizar según la opción ingresada por el usuario

    if opción == 1:
        suma = numero1 + numero2
        print(f"el resultado de sumar {numero1} y {numero2} es: {suma}")
    elif opción == 2:
        resta= numero1 - numero2
        print(f"el resultado de restar {numero1} y {numero2} es: {resta}")
    elif opción == 3:
        multiplicación= numero1 * numero2
        print(f"el resultado de multiplicar {numero1} y {numero2} es: {multiplicación}")
    elif opción == 4:
        división= numero1 / numero2
        print(f"el resultado de dividir {numero1} y {numero2} es: {división}")
    elif  # Profe: Faltan agregar la lógica para las opciones 5 y 6.
    
    elif
    
    else:
        print("ingresó una opción incorrecta. Vuelva a intetarlo")
