# problema: un usuario necesita calcular la multiplicacion y division  de dos numeros
#solucion: crear un algoritmmo que solucione el problema
#programa: la solucion es crear un programa que le calcule la multiplicacion y division de dos numeros
while True:
    #paso 1: pedir al usuario que ingrese los numeros

    numero1=int(input("ingrese un numero"))
    numero2=int(input("ingrese un numero"))

    #paso 2: preguntar al usuario que operacion quiere realizar

    print("que operacion quiere realizar?")
    print("para multiplicar pone 1")
    print("para dividir pon 2")

    operacion= int(input("que operacion quiere realizar"))

    #paso 3: realizar la operacion que presisa el usuario

    if operacion == 1:
        resultado= numero1*numero2
        print(f"el resultado de la multiplicacion de {numero1} y {numero2} es: {resultado}")
    else:
        resultado1= numero1/numero2
        print(f"el resultado de la division de {numero1} y {numero2} es: {resultado1}")



