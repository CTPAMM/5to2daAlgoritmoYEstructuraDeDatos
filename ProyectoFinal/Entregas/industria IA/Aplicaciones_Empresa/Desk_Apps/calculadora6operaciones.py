#calculadora para realizar operaciones matemáticas (6)

while True:
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
elif opcion == 3:
    multi´licación = número1 * número2
    print("El resultado de multiplicar {número1} y {número2} es {multiplicación}")
elif opcion == 4:
    división = número1 / número2
    print("El resultado de dividir {número1} y {número2} es {dividir}")
elif opcion == 5:
    potenciación = número1 ** número2
    print("El resultado de potenciación {número1} y {número2} es {potenciación}")
elif opcion == 6:
    radicación = número1 - número2
    print("El resultado de radicación {número1} y {número2} es {radicación}")
else:
    print("Ingresó una opcion incorrecta.Vuelva a intentarlo.")
    

