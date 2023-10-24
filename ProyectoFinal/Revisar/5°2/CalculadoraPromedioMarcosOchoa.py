# PROBLEMA: Un estudiante necesita calcular un promedio de sus alumnos.
# SOLUCION: Crear un algoritmo de promedio de notas.

while True:
    # PASO 1: mostrar un menu de opciones al usuario.
    print("*****************MENU DE OPERACIONES****************")
    print("0- SALIR")
    print(" 1- INICIAR APLICACION")
    print("******************************************************")
    
    # PASO 2: Pedir al usuario que ingrese una opcion.
    opcion = int(input("ingrese su opcion"))
    
    # PASO 3 : decidir que operacion realizar.
    
    if opcion == 0:
        break
    elif opcion == 1:
        lista_materias = []
        contador = 1
        cantidad_asignaturas = int(input("ingrese la cantidad de materias que cargara"))
        suma_notas = 0
        
        while(contador <= cantidad_asignaturas):
            materia = input(f"ingrese el nombre de la materia{contador}")
            lista_materias.append(materia)
            contador += 1
            
        for materia in lista_materias:
            nota = float(input(f"ingrese la nota de la materia{materia}"))
            suma_notas += nota
        
        promedio = suma_notas / cantidad_asignaturas
        
        print(f"el promedio de sus notas de las materias:{lista_materias} es: {promedio}")
        
        
    else:
     print("opcion incorrecta, vuelva a intentarlo")
    

        

            
            
