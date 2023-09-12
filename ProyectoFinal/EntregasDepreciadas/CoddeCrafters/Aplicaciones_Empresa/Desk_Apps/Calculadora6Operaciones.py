# Calculadora para realizar operaciones matematicas (6)

print("********************************************")
print("bienvenido a la calculadora de 6 operaciones")
print("********************************************")

print("********************************************")
print("1- SUMA")
print("1- RESTA")
print("1- MULTIPLICACION")
print("1- DIVISION")
print("5- POTENCIACION")
print("6- RADIACION")
print("********************************************")

opcion = int(input("ingrese una opcion de operacion: 2"))

# Comienza la logica del programa.

print("************Inicia la aplicacion***********")

numero1 = input("ingrese el primer numero: ")
numero2 = input("ingrese el segundo numero: ")

if opcion == 1:
    suma = numero1 + numero2
    print(f"el resultado de sumar {numero1} y {numero2} es: ")
elif opcion == 2:
    resta = numero1 - numero2
    print(f"el resultado de restar {numero1} y {numero2} es: {resta}")
    