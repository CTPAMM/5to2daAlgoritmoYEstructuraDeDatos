#problema:un estudiante necesita calcular su promedio de sus notas
#solucion:crear una calculadora de promedio de notas

while True:
    #paso 1: mostrar un menude opciones 
    print("**********menu de operaciones**********")
    print("0- salir")
    print("1- iniciar aplicacion")

    opcion = int(input("que opcion quiere? "))

    if opcion == 0:
        print("vuelva pronto!!!")
        break
    elif opcion == 1:
        lista_mateiras = []
        contador = 1
        cantidad_de_asignaturas = int(input("ingrese la cantidad de materias que a cargar: "))
        suma_notas = 0

        while (contador <= cantidad_de_asignaturas):
            materia = input(f"ingrese el nombre de la materia {contador}")
            lista_mateiras.append(materia)
            contador += 1
        
        for  materia in lista_mateiras:
            nota = float(input(f"ingrese la nota de la asignatura {materia}: "))
            suma_notas += nota


        promedio = suma_notas / cantidad_de_asignaturas

        print(f"el promedio de tus notas de las materias {lista_mateiras} es: {promedio}")
    else:
        print("opcion incorrecta vuelva a intentar!!")