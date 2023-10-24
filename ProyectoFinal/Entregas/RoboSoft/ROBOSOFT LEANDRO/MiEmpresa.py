# PROBLEMA: Un usuario necesita un menu descriptivo de tu empresa.
# SOLUCION: Programa en python con un menu que describa mi empresa.

while True:
    # PASO 1: Mostrar un menu de opciones.
    print("*******MENU DESCRIPTIVO DE MI EMPRESA*******")
    print("Nombre de la empresa (nombre)")
    print("Mision de la empresa (mision)")
    print("Vision de la empresa (vision)")
    print("integrantes de la empresa (integrantes)")
    print("********************************************")
    
    # PASO 2: Pedir que ingrese su opcion
    opcion = input("Ingrese su opcion:  ")
    
    # PASO 3: Decidir que operacion realizar (condicional)
    
    if opcion == 'nombre':
        print("RObosoft")
    elif opcion == 'mision':
        print("Nuestra mision: Proteger el futuro con solucionesroboticas inteligentes y eticas.")
    elif opcion == 'vision':
        print("Nuestra vision: Ser lideres en la creacion del futuro con software y robotica innovadora para una vida mejor.")
    elif opcion == 'integrantes':
        print("Los integrantes somos: Gonzalez Leandro, Mugnier Geremias, Cerdan Nehuen")
    else:
        print("Opcion incorrecta. Vuelva a intentar.")