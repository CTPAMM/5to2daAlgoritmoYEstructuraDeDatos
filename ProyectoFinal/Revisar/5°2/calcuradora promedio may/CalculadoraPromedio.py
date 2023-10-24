#PROBLEMA: Un estudiante nesecita calcular el promedio de sus notas
#SOLUCIÓN: Crear un algoritmo de calculadora de promedios de notas

while True:
    #PASO 1: Mostrar un menú de opciones.
    
    print("**********MENÚ DE OPERACIONES**********")
    print("0- SALIR")
    print("1- INICIAR APLICACION")
    print("*****************************")
    
    #PASO 2: Pedir al usuario ingrese su opcion.
    
    opcion = int(input("ingrese su opcion"))
    
    #paso 3: decidir que operacion realizar
    
    if opcion == 0:
        break
    elif opcion == 1:
        lista_materias = []
        contador = 1 
        cantidad_asignaturas = int(input("Ingrese la cantidad de materiasa cargar"))
        suma_notas = 0 
        
        while(contador <= cantidad_asignaturas):
            materia = input(f"Ingrese el nombre de la materia {contador} ")
            lista_materias.append(materia)
            contador += 1 
        for materia in lista_materias:
            nota = float(input(f"ingrese la nota de la materia{materia}"))    
            suma_notas += nota 
            
    promedio= suma_notas / cantidad_asignaturas
      
    print (f"El promedio de sus notas de las materias {lista_materias} es :{promedio}") 
else:
    print("opcion incorrecta vuelva a intentarlo.")  
            