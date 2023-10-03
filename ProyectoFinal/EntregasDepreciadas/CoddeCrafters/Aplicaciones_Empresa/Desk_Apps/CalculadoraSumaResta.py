#PROBLEMA:un usuario necesita calcular la suma y resta de 2 numeros
#SOLUCION:Crear un algoritmo que solucione su problema.
while True:
    #PASO 1: Pedir al usuario que ingrese los numeros a operar

    numero1= int(input("ingrese el primer numero"))
    numero2= int(input("ingrese el segundo numero"))

    # PASO 2: Preguntar al usuario que opreracion quiere realizar (menu).


    print("menu")
    print("1.-suma")
    print("2.-resta")
    


    #PASO 3: pedir al usuario ingrese una opcion
    opcion = int(input("ingrese su opcion"))


    #PASO 4: realizar la operacionn que selecciono el usuario.
    if opcion ==1:
        resultado=numero1 + numero2
    else:
        resultado=numero1-numero2
        
    #PASO 5: Mostrar el resultao de la operacion al usuario

    print(f"{resultado}")