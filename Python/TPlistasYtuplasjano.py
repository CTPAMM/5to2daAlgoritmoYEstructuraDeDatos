#--------------------------------
# titulo: tp de listas y tuplas
# Estudiantes: Su nombre
# Curso: 5° 2°
#--------------------------------

#Declaro una lista de 7 elementos
lista_jugadores = ['messi', 'neymar','cristiano ronaldo', 'roberto carlos', 'foden', 'salah', 'veratti']

print('**********Menu***********')
print('1- imprimir la lista')
print('2- agregar un elemento')
print('3- ordenar la lista alfabeticamente ')
print('4- quitar un elemento')
print('*************************************')

opcion = int(input("ingrese una opcion: "))

if opcion==1:
    print(lista_jugadores)
elif opcion==2:
    lista_jugadores.append(0)
elif opcion==3:
    lista_jugadores.sort()
elif opcion==4:
    lista_jugadores.pop(4)
else:
    print("ingrese nuevamente una opcion")