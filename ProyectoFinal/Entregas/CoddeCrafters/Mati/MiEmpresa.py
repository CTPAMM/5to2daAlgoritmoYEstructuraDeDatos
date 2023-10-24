# Problema: Un usuario necesita un menú descriptivo de tu empresa.
# Solución: Programa en Python cpn un menú que describa mi empresa.

while True:
    # Paso 1: Mostrar al usuario un menú de opciones.
    print("***************MENÚ DESCRIPTIVO DE MI EMPRESA***************")
    print("Nombre de la empresa (nombre)")
    print("Misión de la empresa (mision)")
    print("Visión de la empresa (vision)")
    print("Integrantes de la empresa (integrantes)")
    print("************************************************************")
    
    # Paso 2: Pedir que ingrese su opción.
    opcion = input("Ingrese su opción: ")
    
    # Paso 3: Decidir que operación realizar (condicional)
    
    if opcion == 'nombre':
        print("CodeCrafters") 
    elif opcion == 'mision':
        print("Nuestra misión es crear softwares para que cualquier persona pueda programar y crear sus propios proyectos y mejorar en sí mismos.")
    elif opcion == 'vision':
        print("Nuestra visión es ser líderes en innovación tecnológica, creando soluciones que transformen la manera en que las personas viven, trabajan, y se conectan.")
    elif opcion == 'integrantes':
        print("Los integrantes son: Matias Cañellas, Joshue Soler, Jano Bagdadi")
    else :
        print("Opción incorrecta, vuelva a intentarlo.")