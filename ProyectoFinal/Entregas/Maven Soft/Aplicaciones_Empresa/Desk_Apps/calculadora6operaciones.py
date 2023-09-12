while True:
    print("**********************************************************************************")
    print("bienvenido a la calculadora de 6 operaciones")
    print("**********************************************************************************")

    print("*************************** menu de operaciones ********************************")
    print("1- suma")
    print("2- resta")
    print("3- multiplicacion")
    print("4- division")
    print("5- potenciadores")
    print("6- radicaciones")
    print("*********************************************************************************")

    opcion = int(input("ingrese una opcion de operacion: "))

    # comienza la logica 

    print("**************** inicia la operacion *********************")

    numero1 = int(input("ingrese un numero: "))
    numero2 = int(input("ingrese otro numero: "))

    if opcion == 1:
        suma = numero1 + numero2
        print(f"el resultado de la suma de {numero1} y {numero2} es: {suma} ")
    elif opcion == 2:
        resta = numero1 - numero2
        print(f"el resultado de la resta de {numero1} y {numero2} es: {resta}")
    elif opcion == 3:
        multiplicacion = numero1 * numero2
        print(f"el resultado de la multiplicacion de {numero1} y {numero2} es: {multiplicacion}")
    elif opcion == 4:
        division = numero1 / numero2
        print(f"el resultado de la division de {numero1} y {numero2} es: {division}")
    elif opcion == 5:
        potencia = numero1 ** numero2
        print(f"el resultado de la potencia de {numero1} y {numero2} es: {potencia}")
    elif opcion == 6:
        radicacion = (numero1+numero2)/2
        print(f"el resultado de la radicacion de {numero1} y {numero2} es: {radicacion}")
    else:
        print("opcion incorrecta intentelo de nuevo")