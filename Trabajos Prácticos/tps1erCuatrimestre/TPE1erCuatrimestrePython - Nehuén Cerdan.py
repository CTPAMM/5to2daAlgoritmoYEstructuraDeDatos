# -------------------------------------------------------------------------------
# Fecha: 28-06-23
# Curso: 5° 2°
# Estudiante: Nehuén Cerdan 
# Título: Trabajo Práctico Evaluativo del 1er Cuatrimestre
#--------------------------------------------------------------------------------
'''
1) Escribe un programa muestre por pantalla “Hello World”.
'''
print(" Hello World ")

'''
2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.
'''
numero1 = 3
numero2 = 5

resultado = numero1 + numero2 

print(f"La suma {numero1} + {numero2} + es: {resultado}")

'''
3) Escribe un programa que pida el primer nombre, segundo nombre y apellido y escriba un texto que diga “Hola nombre completo”
'''

primerNombre = input("Introduzca el primer nombre: ")
segundoNombre = input("Introduzca el segundo nombre")
apellido = input("Introuzca el apellido")

print(f"Hola {primerNombre} + {segundoNombre} + {apellido}")

'''
4) Escribe un programa que pida un número, pida otro número y escriba el resultado de multiplicar estos dos números.
'''
numero1 = int(input("Introduzca el primer numero: "))
numero2 = int(input("Introduzca el segundo numero: "))
'''
5) Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.
'''
numero1 = int(input("Introduzca el primer numero: "))
numero2 = int(input("Introduzca el segundo numero: "))

if numero1 > numero2:
    print(f"El numero mayor a entre {numero1} y {numero2} es: {numero1}")
    print(f"El numero menor a engtre {numero1} y {numero2} es: {numero1}")

'''
6) Escribe un programa que pida un número y diga si es divisible por 2
'''

numero1 = int(input("Introduzca el primer numero: "))

if numero1%2 == 0:
    print(f"El numero {numero1} es divisible por 2")
else:
    print(f"El numero {numero1} no es divisible por 2")

'''
7) Escribe un programa que pida un número y nos diga si es divisible por 2 y 3 
(sólo hay que comprobar si lo es por uno de los cuatro)
'''
numero1 = int(input("Introduzca el primer numero: "))

if numero1%2 == 0 and numero1%3 == 0:
    print(f"El numero {numero1} es divisible por 2 y 3")
else:
    print(f"El numero {numero1} no es divisible por 2 y 3")
'''
8) Pide una nota (número). Muestra la calificación según la nota:
 0-3: Muy deficiente
 3-5: Insuficiente
 5-6: Suficiente
 6-7: Bien
 7-9: Notable
 9-10: Sobresaliente
'''

nota = int(input("introduzca la nota: "))

if nota > 0 and nota<= 3:
    print(f"Muy deficiente")
elif nota > 3 and nota <= 5
    print("Insuficiente")
elif nota > 5 and nota <= 6
    print("Suficiente") 
elif nota > 6 and <= 7
    print("Bien")
elif nota > 7 and <= 9
    print("Notable")
elif nota > 9 and <= 10
    print("Sobresaliente") 

'''
9) Crea una lista llamada "lista_numeros" y almacena los siguientes valores integer:
10,45,356,50,10,15,46,67,45,10,28,43,10,65,10,33
'''
lista_numero = [10,45,356,50,10,15,46,67,45,10,28,43,10,65,10,33]
'''
   a) Imprime el valor menor y mayor.
   b) Imprime la lista ordenada de menor a mayor
   c) Imprime el largo de la lista
   d) Imprime cuantas veces se repite el número 10

a) Imprime el valor menor y mayor
'''

print(lista_numero)

'''
b) Imprime la lista ordenada de menor a mayor
'''
lista_numero.sort()

print(lista_numero)
'''
c) imprime  el largo de la lista
'''
print(len(lista_numero))
'''
d) imprime cuantas veces se repite el numero 10
'''
prin(lista_numero.count(10))
'''
10) Crea una lista llamada "lista_colores" y almacena los siguientes valores string:
rojo, azul, verde, amarillo
'''
lista_colores = ["rojo", "azul", "verde", "amarillo"]

'''
    a) Imprime la lista modificada luego de añadir los colores en el código en este orden:
        gris - Antes de "rojo".
        rosa - En último lugar.
        naranja - Entre "azul" y "verde".
'''
lista_colores.insert(0, "gris")
lista_colores.append("rosa")
lista_coloresinsert(3, "naranja")

print(lista_colores)
'''