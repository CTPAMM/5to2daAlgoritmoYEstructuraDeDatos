#----------------------------------------------
# Título: Menú para operar una Lista
# Estudiante: Su Nombre
# Curso: 4° 2°
# ----------------------------------------------

# Declaro una lista de 8 elementos

lista_marcas = ['Fiat', 'Peugeot', 'Citroen', 'Ds', 'Kia', 'Ford', 'Audi', 'Renault']

while(True):

    print('*********************** Menú ********************************')

    print('1- Imprimir toda la lista con la función print')
    print('2- Imprimir toda la lista con el bucle FOR')
    print('3- Imprimir un elemento concreto de la lista')
    print('4- Agregar un elemento a la lista en la última ubicación')
    print('5- Agregar un elemento a la lista en una ubicación concreta')
    print('6- Reemplazar un elemento concreto de la lista')
    print('7- Quitar un elemento')
    print('8- Ordenar la lista alfabeticamente')
    print('9- Vaciar la lista')

    print('*************************************************************')

    opcion = int(input("Ingrese una opción: "))

    print('*************************************************************')
    
    if opcion == 1:
        print(lista_marcas)
    elif opcion == 2:
        for marca in lista_marcas:
            print(marca)
    elif opcion == 3:
        print(f"El segundo elemento de la lista es: {lista_marcas[1]}")
    elif opcion == 4:
        lista_marcas.append('Toyota')
        print('Se agregó correctamente el elemento')
    elif opcion == 5:
        lista_marcas.insert(2, 'Subaru')
        print('Se agregó correctamente el elemento')
    elif opcion == 6:
        lista_marcas[3] = 'Susuki'
        print('Se reemplazó correctamente el elemento')
    elif opcion == 7:
        lista_marcas.pop(3)
        print('Se eliminó correctamente el elemento')
    elif opcion == 8:
        lista_marcas.sort()
        print('Se odenó correctamente la lista')
    elif opcion == 9:
        respuesta = int(input('¡ Está por vaciar la lista !, ¿Desea continuar? SI(1) NO(2): '))
        if respuesta == 1:
            lista_marcas.clear()
            print('Se vació correctamente la lista')
        elif respuesta == 2:
            print('No se vació la lista')
        else:
            print('¡La respuesta ingresada es incorrecta!')    
    else:
        print('¡La opción ingresada es incorrecta!')
