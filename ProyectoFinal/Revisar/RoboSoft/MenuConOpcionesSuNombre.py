# PROBLEMA: Un usuario necesita un menu de opciones para realizar tareas.
# SOLUCION: Crear un algoritmo que permita seleccionar opciones al usuario.
# PROGRAMA: crear un programa con Python.

while True:
    # PASO : Presentar el menu de opciones
    print("******MENU DE AUTOS******")
    print("1- Skyline")
    print("2- Evo X")
    print("3- Supra")
    print("*************************")
    
    # PASO 2: Pedir al usuario ingrese su opcion
    opcion = int(input("ingrese su opcion"))
    
    # PASO 3: Decidir sobre la opcion del usuario.
    
    if opcion == 1:
        print("Se trata del Nissan GTR Skyline, un auto muy iconico en el cine")
    elif opcion == 2:
        print("Se trata del Mitsubishi Evolution X, Otro auto iconico del cine")
    elif opcion == 3:
        print("Se trata del Toyora Mk4 Supra, Otro auto iconico del cine ")
    else:
        print("¡ opcion incorrecta. Vuelva a intentarlo !")