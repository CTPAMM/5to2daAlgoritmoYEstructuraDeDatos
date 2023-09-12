# Calculadora para realizar operaciones matematicas (6)

while True:
    
    print("********************************************")
    print("bienvenido a la calculadora de 6 operaciones")
    print("********************************************")

    print("********************************************")
    print("1- SUMA")
    print("2- RESTA")
    print("3- MULTIPLICACION")
    print("4- DIVISION")
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
    print(f"el resultado de sumar {numero1} y {numero2} es: {suma} ")
elif opcion == 2:
    resta = numero1 - numero2
    print(f"el resultado de restar {numero1} y {numero2} es: {resta}")
elif opcion == 3:
    multiplicacion = numero1 * numero2
    print(f"el resultado de la multiplicacion {numero1} y {numero2} es: {multiplicacion} ")
elif opcion == 4:
    division = numero1 / numero2
    print(f"el resultado de la division {numero1} y {numero2} es: {division} ")
elif opcion == 5:
    potenciacion = numero1 ** numero2
    print(f"el resultado de potenciacion {numero1} y {numero2} es: {potenciacion}")
elif opcion == 5:
    radicacion = numero1 - numero2
    print(f"el resultado de la radicacion {numero1} y {numero2} es: {radicacion}")
else:
    print("ingreso una opcion incorrecta.vuelva a intentarlo.")