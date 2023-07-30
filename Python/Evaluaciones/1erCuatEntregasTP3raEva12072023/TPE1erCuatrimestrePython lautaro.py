# -------------------------------------------------------------------------------
# Fecha: 28-06-23
# Curso: 5° 2°
# Estudiante: Geremias Uriel Mugnier
# Título: Trabajo Práctico Evaluativo del 1er Cuatrimestre
#--------------------------------------------------------------------------------
'''
1) Escribe un programa muestre por pantalla “Hello World”.
'''
print("Hello World") 
'''
2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5. 
'''
result=3+5
print(f"el resultado de 3+5 es:" ("result"))
'''
3) Escribe un programa que pida el primer nombre, segundo nombre y apellido y escriba un texto que diga “Hola nombre completo”
'''
nombre1=(input("Ingrese Su Nombre" ))
apellido1=(input("Ingrese su apellido") )
print(f"Hola {nombre1} {apellido1}")
'''
4) Escribe un programa que pida un número, pida otro número y escriba el resultado de multiplicar estos dos números.
'''
numero1=int(input("Ingrese Un Numero"))
numero2=int(input("Ingrese un Numero"))
print(numero1 * numero2)
'''
5) Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.
'''
numero1=int(input("introduzca el primer numero"))
numero2=int(input("introduzca el segundo numero"))
if numero1 > numero2
    print(f"el numero mayor entre {numero1} y {numero2} es: {numero2}")
else:
   print(f"el numero mayor entre {numero1} y {numero2} es: {numero2}")
'''
6) Escribe un programa que pida un número y diga si es divisible por 2
'''
numero1=int(input("ingrese un numero"))

if numero1%2==0:
     print(f"el numero {numero1} es divisible por 2")
else:
     print("el numero {numero1} no es divisble por 2")
'''
7) Escribe un programa que pida un número y nos diga si es divisible por 2 y 3 
(sólo hay que comprobar si lo es por uno de los cuatro)
'''
numero1 = int(input("introduzca el primer numero: "))

if numero1%2 == 0:
   print(f"el numero {numero1} es divisible por 2")
else:
    print(f"el numero {numero1} es divisible por 3")
'''
8) Pide una nota (número). Muestra la calificación según la nota:
 0-3: Muy deficiente
 3-5: Insuficiente
 5-6: Suficiente
 6-7: Bien
 7-9: Notable
 9-10: Sobresaliente
'''
numero1=int(input("Ingrese Su numero de calificacion"))

if numero1 > 0 or numero1 <=3 :
    print("Muy Deficiente")

elif numero1 >3 or numero1 <=5 :
    print("Insuficiente")

elif numero1 >5 or numero1<=6 :
    print ("Suficiente")

elif numero1 >6 or numero1 <=7 :
  print("Bien")

elif numero1 >7 or numero1<=9 :
 print("Notable")

elif numero1 <9 or numero1<=10 :
 print("Sobresaliente")
'''
9) Crea una lista llamada "lista_numeros" y almacena los siguientes valores integer:
10,45,356,50,10,15,46,67,45,10,28,43,10,65,10,33
'''
lista_numeros = {10,45,356,50,10,15,46,67,45,10,28,43,5,65,10,33}

'''
   a) Imprime el valor menor y mayor.
  '''
print(f"el mayor numero es {lista_numeros[2]} y el menor numer {lista_numeros[2]}")

'''
   b) Imprime la lista ordenada de menor a mayor
   '''
lista_numeros.sort()

print(lista_numeros)

   '''
   c) Imprime el largo de la lista
   '''

print(len(lista_numeros))

'''
   d) Imprime cuantas veces se repite el número 10
   '''
print(lista_numeros.count(10))

'''

10) Crea una lista llamada "lista_colores" y almacena los siguientes valores string:
rojo, azul, verde, amarillo

    a) Imprime la lista modificada luego de añadir los colores en el código en este orden:
        gris - Antes de "rojo".
        rosa - En último lugar.
        naranja - Entre "azul" y "verde".
'''

lista_colores = ["rojo", azul, verde, amarillo]
        
lista_colores.insert(0, "gris")
lista_colores.append("rosa")
lista_colores.insert(3, "naranja")

print(lista_colores)
