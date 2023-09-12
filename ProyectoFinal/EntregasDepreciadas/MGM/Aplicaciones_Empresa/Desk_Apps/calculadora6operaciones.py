#clacluladora para realizar operaciones matematicas (6)

print("*******************************")
print("bienvenido a la calculadora de 6 operaciones")
print("*******************************")

print("********** MENU DE OPERACIONES ***************")
print("1- SUMAR")
print("2- RESTA")
print("3- MULTIPLICACIÓN")
print("4- DIVISIÓN")
print("5- POTENCIACIÓN")
print("6- RADICACIÓN")
print("*******************************")

opción = int(input("ingrese una opción de operación"))

# comienza la lógica del programa.

numero1 = input("ingrese el primer número: ")
numero2 = input("ingrese el segundo número: ")

if opción == 1:
    suma = numero1 + numero2
    print(f"el resultado de sumar {numero1} y {numero2} es: {suma}")
elif opción == 2:
    resta= numero1 - numero2
    print(f"el resultado de restar {numero1} y {numero2} es: {resta}")