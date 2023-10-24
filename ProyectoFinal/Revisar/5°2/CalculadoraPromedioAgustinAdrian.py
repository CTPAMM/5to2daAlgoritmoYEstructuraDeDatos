#PROBLEMA: Un estudiante necesita calcular el promedio de sus
#SOLUCION: Crear un algoritmo de calculadora 

while True:
    # PASO 1: Mostrar un menu de opciones.
    
    print("**********Menu De Opciones***********")
    print("0- SALIR")
    print("1- INICIAR APLICACION")
    print("*************************************")
    
    #PASO 2: pedir al usuario que ingrese su opcion
    
    opcion= int(input("ingrese su opcion:"))
    
    # PASO 3 Decidir que operacion realizar.
    
    if opcion == 0:
        break
    elif opcion == 1:
        lista_materias = []
        contador = 1
        cantidad_asignaturas = int(input("ingrese la cantidad de materias a registrar"))
        suma_notas = 0
        
        while(contador <= cantidad asignaturas):
            materia = input("Ingrese nombre de la materia {contador}:") 
            lista_materias.append(materia)
            contador += 1
            
        for materia in lista_materias:
            nota = float(input{f"Ingrese la nota de la materia{materia}"})
            suma_notas += nota
            
            promedio = suma_notas / cantidad_asignaturas
            
            print(f"el prmedio de sus notas de las materias {lista_materias}")
                
    else:
        print("opcion incorrecta. vuelva a intentarlo")