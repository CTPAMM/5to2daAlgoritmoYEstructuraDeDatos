#PROBLEMA: Un estudiante necesita calcular el promedio de sus...
#SOLUCION:

while True:
    #PASO 1: Mostrar un menu de opciones.
    
    print("*****MENU DE OPERACIONES*****")
    print("1-INICIAR APLICACION")
    print("*****************************")
    
    #PASO 2: Pedir al usuario ingrese su opcion.
    
    opcion = int(input("Ingrese su opcion:"))
    
    #PASO 3: Decidir que operacion realiar.
    
    if opcion == 0:
        break
    elif opcion == 1:
        lista_materias = []
        contador = 1
        cantidad_asignaturas = int(input("Ingrese la cantidad de materias a registrar:"))
        suma_notas = 0
        
        while (contador <= cantidad_asignaturas):
            materia = input(f"Ingrese el nombre de la materia {contador}:")
            lista_materias.append(materia) 
            contador += 1
            
        for materia in lista_materias:
            nota = float(input(f"Ingrese la nota de la materia {materia}"))
            suma_notas += nota
    
        promedio = suma_notas / cantidad_asignaturas
        
        print(f"El promedio sus notas de las materias {lista_materias} es: {promedio}")
        
        
    else:
        print("Opcion incorrecta. Vuelva a intentarlo.")
        
        
        
        

            
    