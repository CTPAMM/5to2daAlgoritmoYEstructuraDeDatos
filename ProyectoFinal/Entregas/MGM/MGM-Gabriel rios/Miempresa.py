


while True:
    #Paso 1 : Mostrar al usuario menu de opciones:
    print("*************** MENU DESCRIPTIVO DE MI EMPRESA***********")
    print("nombre de la empresa(nombre)")
    print("mision de la empresa (mision)")
    print("vision de la empresa(vision)")
    print("integrantes de la empresa (integrantes)")
    print("*****************************************************************")
    
    # Paso 2: Pedir que ingrese una opción
    opcion = input("ingrese una opcion:")
    
    #paso 3: decidir que operacion realizar (condicion)
    
    if opcion == "nombre":
        print("MGM")
    elif opcion == "mision":
        print("nuestra mision es protger las contraseñas de todas las cuentas que esten a disposicion o recuperarlas, a veces estas cuentas que se pierden son muy importantes para lo que se dedican los usuarios ventas,influencers,emprendimientos")
    elif opcion == "vision":
        print("nuestra vision es ser el programa n°1 del mundo en nuestro rubro y proteger todas las cuentas de hackeos y perdidas de contraseñas")     
    elif opcion == "integrantes":
        print("Los integrantes son: MARCOS TASTACA,MAYRA CANO,SOFIA SARACHAGA Y GABRIEL RIOS")
    else:
        print("Opción incorrecta. Vuelvalo a inentar.")        