#problema: un estudiante necesita calcular el promedio de sus notas.
# solucion: crear un algoritmo de calculadora de promedios

while True:
    #paso 1: mostrar un menu de opciones
    print("*************MENU DE OPERACIONES***************")
    print("0-SALIR")
    print("1-INICIAR APLICACION")
    print("***********************************************")
    #paso 2:pedir al usuario ingrese su opcion
    
    opcion= int(input("ingrese su opcion: "))
    
    #paso 3: decidir que operacion 

    
    if opcion == 0:
        break 
    elif opcion == 1:
        lista_materias = []
        contador = 1
        cantidad_asignaturas = int(input("ingrese la cantidad de materia a cargar"))
        suma_notas = 0
        
        while(contador <=cantidad_asignaturas):
         materia = input(f"ingrese el nombre de la materia")
        lista_materias.append(materia)
        contador += 1
    
        for materia in lista_materias:
            nota = float(input(f"ingrese la nota de la materia"))
            suma_notas += nota 
    
    promedio = suma_notas / cantidad_asignaturas

    print(f"el promedio de sus notas de las materias {lista_materias} es:{promedio}")


else:
    print("opcion incorrecta. vuelve a intentarlo")
    