#PROBLEMA:un usuario necesita un menú descriptivo de tu empresa.
#SOLUCION:propaganda en phyton con un menu que describa mi empresa.



while True:
    #PASO 1: mostrar al usuario un menú de opciones.
    print("*************MENÚ DESCRIPTIVO DE MI EMPRESA**************")
    print("Nombre de la empresa(nombre)")
    print("mision de la empresa (mision)")
    print("vision de la empresa(vision)")
    print("integrantes de la empresa(integrantes)")
    print("********************************************")
    
    #PASO 2:pedir que ingrese su opcion
    opcion=input("ingrese su opcion:")
    
    #PASO 3: DECIDIR QUE OPERACION REALIZAR (condicional)
    
    if opcion=="nombre":
        print("techArg")
        
    elif opcion=="mision":
        print("nuestra mision Ofrecer a nuestros clientes aplicaciones de escritorio y web que se ajusten a sus necesidades específicas, impulsando su eficiencia y competitividad en un mundo digital en constante evolución.")
        
    elif opcion=="vision":
        print("nuestra vision Ser líderes en la creación de soluciones digitales personalizadas que impacten positivamente en diversos sectores, brindando innovación y calidad en cada proyecto.")
    elif opcion=="integrantes":
        print("los integrantes somos juana rios y cande escobar")
       
        
    else:
        print("opcion incorrecta.Vuelve a intentarlo")
    

    
