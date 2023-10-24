#PROBLEMA: Un estudiante necesita calcular el promedio de sus notas
#SOLUCION: Crear un algoritmo de calculadora de promedios de notas

while True:
    #PASO 1: Mostrar un menu de opciones.
    print("***********MENU  DE OPERACIONES**************")
    print("0- SALIR")
    print("INICIAR APLICACION")
    print("************************************************")

    #PASO 2:

    opcion = int(input("ingrese su opcion: "))

    #PASO 3: Decidir que operacion realizar.

    if opcion == 0:
        break
    elif opcion ==1:
        lista_materias = []
        contador = 1
        cantidad_asignatura = int(input("ingrese la cantidad de materias a registrar"))
        suma_notas = 0

        while(contador <= cantidad_asignatura):
            materia = input(f"ingrese el nombre de la materia {contador}: ")
            lista_materias.append(materia)
            contador += 1

        for materia in lista_materias:
            nota = float(input(f"ingrese la nota de la materia {materia}:  "))
            suma_notas += nota

            promedio = suma_notas / cantidad_asignatura

            print(f"El promedio de sus notas de las materias {lista_materias} es:{promedio} ")

        else:
            print("opcion incorrecta. vuelva a intentarlo")

            

        
             


    

