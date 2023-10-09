# PROBLEMA: Un usuario necesita un menu de opciones para realizar tareas.
# SOLUCION: Crear un algoritmo que permita seleccionar opciones al usuario.abs
# PROGRAMA: Crear un programa con python

while True:
    # PASO 1: Presentar el menu de opciones
    print("******************** MENU DE LENGUAJES DE PROGRAMACION*************************")
    print("1- fortnite")
    print("2- warzone")
    print("3- fifa")
    print("*******************************************************************************")
    
    # PASO 2: Pedir al usuario ingrese su opcion
    opcion = int(input("ingrese su opcion: "))
    
    # PASO 3: Decidir sobre la opcion del usuario.
    if opcion == 1: 
        print("Se trata de un juego battle royale lanazado en 2017 creado por Tim Sweeney siendo el juego mas popular por varios años")
    elif opcion == 2:
        print("Se trata de una franquicia muy conocida que es call of duty que en 2020 se dio a conocer warzone que es un battle royale.")
    elif opcion == 3:
        print("se trata del famoso juego de deporte futbol que se primer entrega fue en 1993 y que hasta lla fecha es un juego muy conocido")
    
    else:
        print("¡opcion incorrecta. vuelve a intentarlo!")