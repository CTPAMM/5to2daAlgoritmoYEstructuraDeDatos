#PROBLEMA:un usuario necesita un menú de opciones para realizar tareas.
#SOLUCIÓN:crear un algoritmo que permita seleccionar opciones al usuario.
#PROGRAMA:crear un programa con python

while True:
    #PASO 1: prsenta el menú de opciones
    print("****************MENÚ DE MAQUILLAJE********************")
    print("1- paletas de sombras")
    print("2- labial")
    print("3-deliniador")
    print("******************************************************************")
    #paso 2: pedir al usuario ingrese su opcion 
    opcion=int(input("ingrese su opcion:"))
    
    
    #paso3: decidir sobre la opcion del usuario.
    if opcion == 1:
        print("sirve para pintarte los ojos")
    elif opcion == 2:
        print("sirve para pintarte los labios")
    elif opcion==3:
        print("sirve para deliniar el ojo")
    else:
        print("¡opcion incorrecta .vuelva a intentarlo")