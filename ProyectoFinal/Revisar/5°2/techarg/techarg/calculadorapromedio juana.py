#PROBLEMA: un estudiante necesita calcular el promedio de sus notas.
#SOLUCION: crear un algoritmo de calculadora de promedios de notas.

while True:
    #PASO: mostrar un menu de operaciones.
    print("**************MENU DE OPERACIONES*************")
    print("0-SALIR")
    print("1-INICIAR APLICACION")
    print("******************************************")
    
    
    #PASO 2:pedir al usuario ingrese su opcion.
    opcion=int(input("ingrese se opcion "))
    
    #PASO 3: decidir que operacion realizar.
    
    if opcion==0:
        break
    elif opcion== 1:
        lista_materias =[] 
        contandor=1
        cantidad_asignaturas=int(input("ingrese la cantidad de materias a cargar"))
        suma_notas=0
        
        while(contandor <= cantidad_asignaturas):
            materia=input(f"ingrese el nombre de la materia{contandor}:")
            lista_materias.append(materia)
            contandor +=1
            
        for materia in lista_materias:
            nota=float(input(f"ingrese la nota de la materia{materia}:"))
            suma_notas +=nota 
            
        promedio=suma_notas/cantidad_asignaturas
        
        print(f"el promedio de sus notas de las materias {lista_materias} es:{promedio}") 
        
            
    else: 
        print("opcion incorrecta.vuelva a intentarlo.")
        
            
        
            
        
    
    
    