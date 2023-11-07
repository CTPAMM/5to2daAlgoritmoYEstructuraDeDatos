#*******************************************************************************
# Empresa: OvniOn
# 
# Aplicación de escritorio: Calculadora de consola de superficies de figuras
# 
# Destinado a: estudiantes de todas las edades y niveles.
# 
# Descripción del funcionamiento:
#   Muestra opciones de cálculo de superficies y solicita al usuario que 
#   ingrese una opcion. Entonces permite realizar esa operación con los 
#   valores de los lados elegidos por el usuario y luego informa el 
#   resultado.
#*******************************************************************************

while True:
    print("*****************************************************")
    print("Bienvenido a la calculadora de superficies de figuras")
    print("                                                     ")
    print("                                    creado por OvniOn")
    print("*****************************************************")

    print("************ MENÚ DE FIGURAS **************")

    print("1- CUADRADO")
    print("2- RECTÁNGULO")
    print("3- TRIÁNGULO")
    print("4- CÍRCULO")
    print("0- SALIR")

    print("**********************************************")

    opcion = int(input("Ingrese una opción de figura: "))

    # Comienza la lógica del programa.

    if opcion == 0:
        print("**********************************************")
        print("¡ Gracias por utilizar nuestra calculadora !"  )
        print("                                              ")
        print("Conozca más sobre nosotros en nuestra web:    ")
        print("                 ovnion.com"                   )
        break

    elif opcion >= 1 and opcion <= 6:

        print("************* Inicia aplicación *************")

        if opcion == 1:
            lado = int(input("Introduzca el valor del lado: "))
            
            respuesta = lado ** 2
            
            print("**********************************************")
            print(f"La superficie del cuadrado es: {respuesta}")
        
        elif opcion == 2:
            base = int(input("Introduzca el valor de la base: "))
            altura = int(input("Introduzca el valor de la altura: "))
            
            respuesta = base * altura
            
            print("**********************************************")
            print(f"La superficie del rectángulo es: {respuesta}")
        
        elif opcion == 3:
            base = int(input("Introduzca el valor de la base: "))
            altura = int(input("Introduzca el valor de la altura: "))
            
            respuesta = (base * altura)/2
            
            print("**********************************************")
            print(f"La superficie del triángulo es: {respuesta}")
        
        elif opcion == 3:
            radio = float(input("Introduzca el valor del radio: "))
            
            respuesta = 3.14 * radio **2
            
            print("**********************************************")
            print(f"La superficie del círculo es: {respuesta}")
            
        else:
            print("¡ ATENCIÓN ! Ingresó una opción incorrecta. Vuelvalo a intentar.")
