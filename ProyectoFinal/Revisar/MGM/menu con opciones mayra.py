#PROBLEMA: Un usuario nesecita un menú de opciones para realizar tareas.
#SOLUCIÓN: Crear un algoritmo que permita seleccionar opciones al usuario.
#PROGRAMA: Crear un programa con python 

while True: 
    #PASO 1: Presentar el menú de opciones 
    print("********************menu de  maquillaje ************************")
    print("1-base")
    print("2- corrector")
    print("3- delineador")
    #PASO 2: Pedir al usuario ingrese su opción
    opcion = int(input("ingrese su opcion:"))
    
    #PASO 3: Decidir sobre la opcion del usuario.
    if opcion == 1:
        print("para toda la cara y o cuello .")
    elif opcion == 2:
        print("para sona de las ojeras cubre las ojeras")
    elif opcion == 3:
        print("para delinear el ojo")    
    else: 
        print("¡ opción incorrecta. Vuelve a intertarlo!")    
        
    