# PROBLEMA: Un usuario necesita calcular la MULTIPLICACIÓN y la DIVISIÓN
# SOLUCIÓN: Crear un algoritmo que solucione su problema
# PROGRAMA: La solución va a ser un programa para calcular


#PASO 1: Pedir al usuario que ingrese los numeros a operar

numero1 = input("ingrese el primer numero")
numero2 = input("ingrese el segundo numero ")
print(f"el numero 1 es: {numero1} y el número 2 es: {numero2}")


#PASO 2: Mostrar menu de operacion.

print("seleccione 1 para dividir")
print("seleccione 2 para multiplicar")

#PASO 3: Pedir al usuario ingrese una opción

opcion = input("¿que operacion desea realizar (división/multiplicación)")


#PASO 4: Realizar la operación que selecciono el usuario.

if opcion ==1:
    resultado = numero1/ numero2
else:
    resultado = numero1*numero2
    
#PASO 5: imprimir el resultado

print(f"el resultado de la {opcion} entre el {numero1} y el {numero2} es: {resultado}")