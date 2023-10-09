#PROBLEMA: un usuario necesita un menu de  opciones para realizar tareas.
#SOLUCION: crear in algoritmo que permita seleccionar opciones al usuario.
#PROGRAMA: crear un programa con python

while True:
    #PASO 1: presentar el menu de opciones 
    print("**************MENU DE ROPA**************")
    print("1-pantalon mom")
    print("2-top")
    print("3-sueter")
    print("*****************************************")
    
    #PASO 2: pedir al usuario ingrese su opcion
    opcion=int(input("ingrese su opcion:"))
    
    #PASO 3: decidir sobre la opcion del usuario.
    if opcion==1:
        print("es un pantalon ajustado arriba y ancho abajo ")
    elif opcion==2 :
        print("es una remerita corta ")
    elif opcion == 3 :
        print("es un abrigo calentito")
    else:
        print("!opcion incorrecta .vuelve a intentarlo")   