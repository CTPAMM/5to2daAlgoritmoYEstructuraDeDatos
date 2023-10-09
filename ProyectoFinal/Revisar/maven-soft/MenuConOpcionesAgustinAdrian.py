#PROBLEMA: Un usuario necesita un menu de opciones para realizar tareas.
#SOLUCION: Crear un algoritmo que permita seleccionar opciones al usuario.
#PROGRAMA: Crear un programa con python.

while True:
    # PASO 1: Presentar el menu de opciones
    print("**********************Menu De Armas***********************")
    print("1- Ak 47")
    print("2- Barret")
    print("3- Mp5")
    print("***********************************************************")
  
    #PASO 2: Pedir al usuario que ingrese su opcion  
    opcion = int(input("Ingrese su opcion:"))
    
    #PASO 3: Decidir sobre la opcion del usuario
    if opcion == 1:
        print("Rifle de Asalto de alto calibre y facil de manipular")
    elif opcion == 2:
        print("Francotirador pesado de muy alto calibre y exelente presicion")
    elif opcion== 3:
        print("Subfusil de Bajo calibre pero alta cadencia")
    else:
        print("¡Vuelva a intentarlo!")