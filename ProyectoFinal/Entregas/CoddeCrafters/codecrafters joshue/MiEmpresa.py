# PROBLEMA: un usuario necesita un menu descriptivo de tu empresa.
# SOLUCION: programa en python con un menu que describa mi empresa.

while True:
        # PASO 1: Mostrar al usuario un menu de opciones 
        print("***********MENU DESCRIPTIVO DE MI EMPRESA************")
        print("nombre de la empresa (nombre)")
        print("mision de la empresa (mision)")
        print("vision de la empresa (vision)")
        print("integrantes de la empresa (integrantes)")
        print("******************************************************")
        
        #PASO 2: Pedir que ingrese su opcion
        opcion = input("ingrese su opcion: ")
        
        #PASO 3: Decidir que operacion realizar (condicional)
        
        if opcion == "nombre":
            print=("codecrafters")
        elif opcion == "mision":
         print("nuestra mision Nuestra misión es crear softwares para que cualquier persona pueda programar y crear sus propios proyectos y mejorar en sí mismos")
        elif opcion == "vision":
         print("nuestra vision Ser líderes en innovación tecnológica, creando soluciones que transformen la manera en que las personas viven, trabajan, y se conectan")
        elif opcion == "integrantes":
         print("los Integrantes somos Matias Cañellas, Joshue soler, Jano bagdadi")
        else:
            print ("opcion incorrecta. vuelvalo a intentar.")