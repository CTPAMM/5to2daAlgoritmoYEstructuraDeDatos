# PROBLEMA: Un usuario necesita un menú de opciones para realizar tareas.
# SOLUCION: Crear un algoritmo que permita sleccionar opciones al usuario.
# PROGRAMA: Crear un programa con phyton.

while True:
    # PASO 1: Presentar el menu de opciones
    print("*************** MENU DE JUEGOS*************")
    print("1-god of war")
    print("2-fifa")
    print("3-the last of us")
    print("*****************************")
     
# PASO 2: Pedir al usuario ingrese su opción:
    opcion = int(input("ingrese su opción:"))
    

# PASO 3: Decidir sobre la opción del usuario.

    if opcion == 1:
        print("se trata de un juego de un semidios que al ser traicionado trata de matar a todo el olimpo como venganza")
    elif opcion == 2:
        print("es el juego mas popular sobre deportes de la historia con gran variedad de modos y con una muy buena jugabilidad")
    elif opcion == 3:
        print("es un juego post apocaliptico donde toda la humanidad esta bajo una infeccion de un hongo que se vuelve huesped de su cuerpo y los atormenta, tu objetivo es sobrevivir")
    else:
        print("opción incorrecta.vuelva a intentarlo no te hagas el pillo")
     
     