#problema: un estudiante necesita calcular el promedio de sus notas 
# solucion : crear un algoritmo de calculadora de promedios de notas

while True:
  #paso 1: mostrar un menu de opciones 
    
    print("********menu de opciones*********") 
    print("0. salir")
    print("1. iniciar aplicacion")
    print("***************************")
    
     #paso2 :pedir al usuario ingrese una opcion
  
    opcion = int(input("ingrese su opcion : "))
     
     #paso3 : decidir que operacion realizar 
     
    if opcion== 0:
         break
    elif opcion==1:
         lista_materias= []
         contador =1
         cantidad_asignaturas = int (input("ingrese la cantidad de materias: "))
         suma_notas= 0
         
         while(contador <=cantidad_asignaturas):
             materias = input (f"ingrese el nombre de la materia {contador}: ")
             lista_materias.append (materias)
             contador= 1
         for materias in lista_materias:
             nota = float(input(f"ingrese la nota de las materias {materias}: "))
             suma_notas += nota
             
             promedio = suma_notas / cantidad_asignaturas 
             
             print(f"el promedio de sus notas de las materias {lista_materias}: ")
    else:
        print("opcion incorrecta , vuelva a intentarlo")         