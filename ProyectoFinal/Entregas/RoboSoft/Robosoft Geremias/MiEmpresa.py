# PROBLEMA: Un usuario necesita un menú descriptivo de tu empresa.
# SOLUCION: Programa en Python con un menú que describa mi empresa.
while True:
    # PASO 1: Mostrar al usuario un menú de opciones.
    print("**********MENÚ DESCRIPTIVO DE MI EMPRESA**********")
    print("Nombre de la empresa (nombre)")
    print("Misión de la empresa (mision)")
    print("Visión de la empresa (vision)")
    print("Integrantes de la empresa (integrantes)")
    print("**************************************************")
    
    # PASO 2: Pedir que ingrese su opción.
    opcion = input("Ingrese su Opción:")
    
    # PASO 3: Decidir que operacion realizar (Condicional)
     
    if opcion =="nombre":
        print("Robosoft")
    elif opcion == "mision":
        print("Potenciar el futuro con soluciones rooticas inteligentes y eticas.")
    elif opcion == "vision":
        print("Ser lideres en la creación del futuro con software y robotica innovadora para una vida mejor.")
    elif opcion == "integrantes":
        print("Los Integrantes somos: Mugnier Geremias, Gonzalez Leandro y Cerdan Nehuen") 
    else:
        print("Opcion Incorrecta. Vuelva a Intentar.")