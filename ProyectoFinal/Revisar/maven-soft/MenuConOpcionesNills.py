# PROBLEMA: Un usuario necesita un menu de opciones para realiyar tareas.
# SOLUCION: Crear un algoritmo que permita seleccionar opciones al usuario.
# PROGRAMA: Crear un programa con Python

while True:
    # PASO 1: Presentar el menu de opciones
    print("********Mende tu equipo de futbol favorito********")
    print("1- Boca")
    print("2- River")
    print("3- Young Boys")
    print("*************************************************")
     
    # PASO 2: Pedir al usuario ingrese su opcion
    opcion = int(input("Ingrese su opcion:"))   
    
    #PASO 3: Decidir sobre la opcion del usuario.
    if opcion == 1:
        print("es el mejor equipo del pais")
    elif opcion == 2:
        print("Sos un boludo")
    elif opcion == 3:
        print("Dale Young Boys Dale")
    else:
        print("¡ opcion incorrecta. Vuelva a intentarlo !")

