#Calculadora para realizar operaciones matematicas (6)

print("**********************************************")
print("Bienvenido a la calculadora de 6 operaciones")
print("**********************************************")

print("************* MENU DE OPERACIONES ************")
print("1- SUMA")
print("2- RESTA")
print("3- MULTIPLICACION")
print("4- DIVISION")
print("5- POTENCIACION")
print("6- RADICACION")
print("**********************************************")

opcion = int(input("Ingrese una opcion de operacion: "))

# comienza la logica del programa.

print("*************Inicia la Aplicacion*************")

numero1 = input("Ingrese el primer numero:")
numero2 = input("Ingrese el segundo numero:")

if opcion == 1:
    SUMA = numero1 + numero2
    print(f"El resultado de SUMAR {numero1} y {numero2} es: ")
elif opcion == 2:
    resta = numero1 + numero2
    print(f"El resultado de restar {numero1} y {numero2} es: {resta}")
