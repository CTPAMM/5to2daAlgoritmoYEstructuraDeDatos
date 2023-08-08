#-----------------------------------------
# Titulo: TP de las listas y tuplas
# Estudiante: joshue soler
# curso:5° 2°
#-----------------------------------------

#Declaro una lista de 7 elementos
Listas_equiposgrandes = ['Boca','inter de miami','argentina','barcelona','united','city','real madrid']

print('************* menu *******************')
print('1- imprimir la lista')
print('2- agregar un elemento')
print('3- ordenar la lista alfabeticamente')
print('4- quitar un elemento')
print('**************************************')

opcion = int(input("ingrese una opcion:"))

if opcion==1:
    print(Listas_equiposgrandes)
elif opcion==2:
    Listas_equiposgrandes.append('toyota')
elif opcion==3:
    Listas_equiposgrandes.sort()
elif opcion==4:
    Listas_equiposgrandes.pop(3)

else:
    print('ingrese nuevamente una opcion')
