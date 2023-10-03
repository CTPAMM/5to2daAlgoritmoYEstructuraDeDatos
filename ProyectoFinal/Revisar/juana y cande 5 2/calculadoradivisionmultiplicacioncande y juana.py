    #PROBLEMA:un usuario necesita calcular la SUMA y la RESTA de 2 números
    #SOLUCION:crear un algoritmo que solucione su problema.
    #programa: la solucion  va a ser un programa para calcular la suma y resta de 2 numeros 
while True:
    #PASO 1: pedir al usuario que ingrese los numeros a operar

    numero1= int(input("introduzca el primer numero:"))
    numero2=int(input("introduzca el segundo numero"))


    #PASO 2: preguntar al usurio que operacion quiere realizar(menú)

    print("Si desea multiplicar ingrese 1")
    print("si desea dividir ingrese 2 ")


    #paso 3: pedir al usuai¿rio ingrese una opción
    
    opcion=input("ingrese una opcion")
    
    #paso 4: realizar la operacion que selecciono el usurio.

    if opcion ==1:
        resultado=numero1*numero2
        
    else:
        resultado=numero1*numero2
        
        
        
#paso 5:mostrar el resultado de la operacion al usuria print
print(f"la operacion entre {numero1} y {numero2} es:{resultado}")
