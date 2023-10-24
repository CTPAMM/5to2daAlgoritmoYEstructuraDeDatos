# Problema: Un estudiante necesita calcular el promedio de sus notas.
# Solución: Crear un algoritmo de calculadora de promedios de sus notas

while True:
    # Paso 1: Mostrar un menú de opciones
    print("**********MENU DE OPERACIONES**********")
    print("0- Salir")
    print("1- Iniciar aplicación")
    print("****************************************")
    
    # Paso 2: Pedir al usuario ingrese su opción
    
    opcion = int(input("Ingrese su opción: "))
    
    # Paso 3: Decidir que operación realizar
    
    if opcion == 0:
        break
    elif opcion == 1:
        lista_materias = []
        contador = 1
        cantidad_asignaturas = int(input("Ingrese la cantidad de materias a cargar: "))
        suma_notas = 0
        
        while(contador <= cantidad_asignaturas):
            materia = input(f"Ingrese el nombre de la materia {contador}: ")
            lista_materias.append(materia)
            contador += 1 
            
        for materia in lista_materias:
            nota = float(input(f"Ingrese la nota de la materia {materia}: "))
            suma_notas += nota
            
        promedio = suma_notas / cantidad_asignaturas
        
        print(f"El promedio de sus notas de las materias {lista_materias} es: {promedio}")
            
    else:
        print("Opción incorrecta. Vuelva a intentarlo")