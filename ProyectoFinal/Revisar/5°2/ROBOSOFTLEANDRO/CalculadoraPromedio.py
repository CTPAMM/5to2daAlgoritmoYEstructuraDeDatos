# PROBLEMA: Un estudiante necesita calcular el promedios de sus notas.
# SOLUCION: Crear un algoritmo de calculadora de promedios de notas

while True:
    # PASO 1: Mostrar un menucde opciones. 
    print("*******MENU DE OPERACIONES*******")
    print("0- SALIR")
    print("1- INCIAR APLICACION")
    print("*********************************")
    
    # PASO 2: Pedir al ususario ingrese su opcion.
    
    opcion = int(input("ingrese su opcion"))
    
    # PASO 3: Decidimos que operacion realizar.
    
    if opcion == 0:
        break
    elif opcion == 1:
        lista_materias = []
        contador = 1
        cantidad_asignaturas = int(input("Ingrese la cantidad de asignaturas a registrar"))
        suma_notas = 0
        
        while(contador <= cantidad_asignaturas):
            materia = input(f"ingrese el nombre de la materia{contador}:")
            lista_materias.append(materia)
            contador += 1
        for materia in lista_materias:
            nota = float(input(f"ingrese la nota de la materia {materia}: "))
            suma_notas += nota
            
        promedio = suma_notas / cantidad_asignaturas
        
        print(f"El promedio de sus notas de las materias {lista_materias} es: {promedio}")
    else:
        print("OPCION INCORRECTA.Vuelva a intentarlo.")