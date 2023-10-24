#PROBLEMA: Un usuario nesecita un menú descriptivo de tu empresa.
#SOLUCION: Programa en Python con un menú que describa mi empresa.

while True:
    # PASO 1:Mostrar al usuario un menú de opciones.
    print("***********MENÚ DESCRIPTIVO DE MI EMPRESA***********")
    print("Nombre de la empresa(nombre)")
    print("Misión de la empresa(mision)")
    print("Vision de la empresa(vision)")
    print("Integrantes de la empresa (integrantes)")
    print("**************************************")
    
    # PASO 2: Pedir que ingrese su opcion 
    opcion = input("Ingrese su opcion: ")
    # PASO 3: Decidir que operacion realizar(condicional)
    
    if opcion =='nombre':
        print("TechArg")
    elif opcion == 'mision':
        print("Nuestra misión...")   
    elif opcion  =='vision':
        print ("Nuestra vision...")
    elif opcion =='integrantes'
      print ("los integrantes somos:....")  
    else:
        print("Opcion incorrecta. vuelvalo a intentar")    
        