#PROBLEMA:un usuario necesita un menu descriptivo de tu empresa.
#SOLUCION: programa en python con un menu que describa mi empresa.

while True:
    #PASO 1: mostrar al usuario un menu de opciones.
    print("***************MENU DESCRIPTIVO DE MI EMPRESA*************")
    print("Nombre de la empresa(nombre)")
    print("Misión de la empresa(mision)")
    print("Vision de la empresa(vision)")
    print("Integrantes de la empresa(integrantes)")
    print("***********************************************************************")
    
    #PASO 2: pedir que ingrese su opcion
    opcion = input("ingrese su opcion")
    
    #PASO 3: decidir con operacion relizar(condicional)
    
    if opcion == "nombre":
       print("industria IA")
    elif opcion == "mision":
        print("nuestra mision.....")  
    elif opcion =="vision":
       print("nuestra vision.....")
    elif opcion == "integrantes":
       print("los integrantes somos....")
    else:
        print("opcion incorrecta vuelvalo a intentar")   
    