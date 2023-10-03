#PROBLEMA: Un usuario necesita calcular la SUMA y la RESTA de 2 numeros.
#SOLUCION: Crear un algoritmo que solucione su problema.
#PROGRAMA: La solucion va a ser un programa para calcular la suma y la resta de 2 numeros.

while True:
    #PASO 1: Pedir al usuario que ingrese los numeros a operar.

    numero1 = int(input("ingrese numero: "))
    numero2 = int(input("ingrese numero: "))



    #PASO 2: Pregunttar al usuario que operacion quiere realizar.
    print("que operacion quiere realizar?")
    print("si queres sumar pone 1")
    print("si queres restar pone 2")

    #PASO 3: Pedir al usuario que ingrese una opcion.

    opcion = int(input("ingresar opcion: "))

    #PASO 4: Realizar la operacion que selecciono el usuario.

    if opcion ==1:
        resultado = numero1 + numero2  
        print(f"el resultado de la suma de {numero1} y {numero2} es: {resultado} ")
    else:
        Resultado1 = numero1 - numero2 
        print(f"el resultado de la resta de {numero1} y {numero2} es: {Resultado1} ")
        

