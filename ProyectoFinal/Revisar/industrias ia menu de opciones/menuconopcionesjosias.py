#PROBLEMA: un usuario necesita un menu de opciones para realizar tarea
#SOLUCION: crear un algoritmo que permita seleccionar opciones al usuario.abs
#PROGRAMA: crear un programa con python

while True:
    #PASO 1: presentar el menu de opciones 
    print("********************MENU DE LENGUAJES DE PROGRAMACION*************************")
    print("1-python")
    print("2-HTML")
    print("javascrit")
    print("********************************************************************")
    
    #PASO 2:pedir al usuario ingrse su opcion
    opcion = int(input("ingrese su opcion"))
    
    #PASO 3: DECIDIR SOBRE LA OPCION DEL USUARIO
    if opcion == 1:
        print("se trata de un lenguaje para programar apss de todo tipo")
    elif opcion == 2:
         print("sirve para programar paginas web")
    elif opcion == 3:
         print("sirve para darle dinadismo a las paginas web")
    else:
        print("opcion incorrecta. vuelve a intertarlo!")
    