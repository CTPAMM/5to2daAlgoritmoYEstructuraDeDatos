# PROBLEMA: Un usuario necesita un menu de opciones para realizar tareas
# SOLUCION: Crear un algoritmo que permita seleccionar opciones al usuario
# PROGRAMA: Crear un programa con python
# FRANCO PIEROTTI 5to 2da


while True:
    # PASO 1: Presentar el menu de opciones
    print("************ MENU DE DEPORTES************")
    print("1- Futbol")
    print("2- Rugby")
    print("3- Golf")
    print("*****************************************")
    
    #PASO 2: Pedir al usuario ingrese su opcion
    opcion = int(input("ingrese su opcion:  "))
    
    #PASO 3: Decidir sobre la opcion del usuario
    if opcion ==1:
        print("Se trata de uno de los mejores deportes del mundo.")
    elif opcion == 2:
        print("Es un buen deporte. ")
    elif opcion == 3:
        print("Es un deporte que no requiere demaciado esfuerzo fisico. ")
    else:
        print("¡ Opcion incorrecta. Vuelve a intentarlo !")