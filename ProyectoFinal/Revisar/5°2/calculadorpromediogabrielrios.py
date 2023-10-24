# PROBLEMA: Un estudiante necesita calcular un promedio de sus alumnos.
# SOLUCIÓN: Crear un algoritmo de promedio de notas.

while True:
    # PASO 1: mostrar un menu de opciones al usuario.
    print("*******************MENU DE OPERACIONES*************")
    print("0- SALIR")
    print("1- INICIAR APLICACIÓN")
    print("**********************************************")
    
    # PASO 2: Pedir al usuario que ingrese una opción.
    opción = int(input("ingrese su opción:"))
    
    # PASO 3: Decidir que operación realizar.
    
    if opción == 0:
        break
    elif opción == 1:
        lista_materias = []
        contador = 1
        cantidad_asignaturas = int(input("ingrese la cantidad de materias que cargara:"))
        suma_notas = 0
        
        while(contador <= cantidad_asignaturas):
            materia = input(f"ingrese el nombre de la materia{contador}")
            lista_materias.append(materia)
            contador += 1
            
        for materia in lista_materias:
            nota = float(input(f"ingrese la nota de la asignatura {materia}:"))
            suma_notas += nota
            
        promedio = suma_notas / cantidad_asignaturas
        
        print(f"el promedio de las materias {lista_materias} es: {promedio}")
        
        
    else:
        print("opción incorrecta, vuelva a intentarlo")
    