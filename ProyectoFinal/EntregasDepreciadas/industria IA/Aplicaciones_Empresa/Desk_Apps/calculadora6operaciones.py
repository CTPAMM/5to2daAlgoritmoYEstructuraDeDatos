#calculadora para realizar operaciones matemáticas (6)

print("***********************************************")
print("bienvenido a la calculadora de 6 operaciones")
print("************************************************")

print("*************** menu de operaciones**************")
print("1- sumar")
print("2- restar")
print("3- multiplicar")
print("4- dividir")
print("5- potenciacion")
print("6- radicacion")
print("**************************************************")

opcion = int(input("ingrese una opcion de operacion"))

# comienza la lógica del programa 

print("*****************inicia aplicacion******************")

número1 = input("ingrese el primer número")
número2 = input("ingrese el segundo número")
if opcion == 1:
    suma = número1 + número2
    print(f"El resultado de sumar {número1} y {número2} es: {suma} ")
elif opcion == 2:
    resta = número1 - número2
    print("El resultado de resta {número1} y {número2} es {resta}")
    