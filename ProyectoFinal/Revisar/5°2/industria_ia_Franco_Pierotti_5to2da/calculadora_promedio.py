# Franco Pierotti 5to 2da
# Problema: Un estudiante nesecita calcular el promedio de sus notas
# Solucion: crear un algoritmo  de calculadora de promediio de notas

while True:
    # Paso 1: mostrar un menu de opciones
    print("********menu de operaciones********")
    print("0- SALIR")
    print("1- INICIAR APLICACION")
    print("***********************************")
    
    # Paso 2: Pedir al usuario ingrese su opcion
    
    opcion = int(input("ingrese su opcion: "))
    
    # Paso 3: decidir que opcion realizar
    
    if opcion == 0:
        break
    elif opcion == 1:
        lista_materias = []
        contador = 1
        cantidad_materias = int(input("ingrese la cantidad de materia a registrar"))
        suma_notas = 0
        
        while(contador <= cantidad_materias):
            materia = input (f"ingrese el nombre de la materia{contador}. ")
            lista_materias.append(materia)
            contador += 1
            
        for materia in lista_materias:
            nota = float(input(f"ingrese la nota de la materia {materia}: "))
            suma_notas += nota
            
        promedio = suma_notas / cantidad_materias
        print(f" El promedio de sus notas de las materias {lista_materias} es: {promedio}")
    else:
        print("Opcion incorrecta; vuelva a intentarlo")