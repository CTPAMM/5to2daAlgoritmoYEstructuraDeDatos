# PROBLEMA: Un usuario necesita un menu descriptivo de tu empresa.
# SOLUCION: Progreso en python con un menu que describa mi empresa:

while True:
    # PASO 1: Mostrar al usario un menu de opciones.
    print("********MENU DESCRIPTIVO DE MI EMPRESA****************")
    print("nombre de la empresa (industrias Ia)")
    print("mision de la empresa (mision)")
    print("vision de la empresa (vision)")
    print("integrantes de la empresa (integrantes)")
    print("******************************************************")
    
    # PASO 2: Pedir que ingrese su opcion.
    opcion = input("ingrese su opcion: ")
    
    # PASO 3: Decidir que operacion realizar (condicional)
    
    if opcion == 'nombre':
        print("Industrias IA")
    elif opcion == 'mision':
        print("transformamos empresas con software inovador y de calidad")
    elif opcion == 'vision':
        print("ser los mejores ayudando a los demas con la IA")
    elif opcion == 'integrantes':
        print("los integrantes somos: Lautaro subiabre, Franco piertti, Josias berengo")
    else:
        print("opcion incorrecta. vuelvalo a intentar. ")
        
    

    
    

