#problema : crear un usuario necesita un menu de opciones para realizar tareas
#solucion:crear un algoritmo que permita seleccionar opciones al usuario
#programa:crear un programa en python

while True:
    #presentar un menu de opciones 
    print("********menu de frutas********")
    print("1.naranja")
    print("2.manzana")
    print("3.mandarina")
    print("*****************************")
    
    #paso 2: pedir al usuario ingrese una opcion
    opcion= int(input("ingrese la opcion: "))
    
    #paso 3:decidir sobre la opcion del usuario .
    if opcion == 1:
     print("Es una fruta citrica , color naranja medio ovalada ")
    elif opcion == 2:
      print("proporciona vitaminas importantes , es color rojo  con forma parecida a un corazon")
    elif opcion == 3:
      print("Tambien es una fruta citrica , con apariencia parecida a la naranja solo es mas hachatada ")
    else:
      print("opcion incorrecta,vuelve a intentarlo ")  
    
      