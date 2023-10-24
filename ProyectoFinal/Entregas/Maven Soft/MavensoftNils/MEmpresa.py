# PROBLEMA: Un usuario necesita un menu descriptivo de tu empresa.
# SOLUCION: Programa en Python con un menu que describa mi empresa. 
while True:
    # PASO 1: Mostrar al usuario un menu de opciones.
    print("********MENU DESCRIPTIVO DE MI EMPRESA********************")
    print("Nombre de la empresa (nombre)")
    print("Mision de la empresa (mision)")
    print("Vision de la empresa (vision)")
    print("Integrantes de la empresa (integrantes)")
    print("***********************************************************")
    
    #PAso 2: Pedir que ingrese su opcion
    opcion = input("Ingrese su opcion:")
    
    #Paso 3: Decidir que operacion realizar (Condicional)
    
    if opcion == 'nombre':
        print("Mavensoft")   
    elif opcion == 'mision':
        print("Buiding a Website")    
    elif opcion == 'vision':
        print("Making learning easier")
    elif opcion == 'integrantes':
        print("Nils, Agustin, Marcos, Tommy")
    else:
        print("Opcion incorrecta. Vuelvalo a inntentar.")
        
    
    
    