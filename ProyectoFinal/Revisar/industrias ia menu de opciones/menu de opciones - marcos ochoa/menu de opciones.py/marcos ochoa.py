# PROBLEMA: un usuario necesita un enu de opciones para realizar tareas.
# SOLUCION: crear un algoritmo que permita seleccionar opciones al usuario.
# PROGRAMA: crear un programa con phyton

while True:
    # PASO 1: presentar el menu de opciones 
    print("**************MENU DE LENGUAJES DE PROGRAMACION*************")
    print("1-voley")
    print("2-futbol")
    print("3-tenis")
    print("**************************************************")
    
    # PASO 2: pedir al usuario ingrese su opcion
    opcion = int(input("ingrese su opcion: "))
    
    # PASO 3: decidir sobre la opcion del usuario.
    if opcion == 1:
        print("es un deporte que se juega con las manos.")
    elif opcion == 2:
        print("es un deporte que se juega con los pies.")
    elif opcion == 3:
        print("es un juego con una pelota pequeña y se juega con raquetas")
    else:
        print("¡opcion incorrecta. vuelva a intentarlo!") 