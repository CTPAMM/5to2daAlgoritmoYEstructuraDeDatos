#Calculadora par realizar operaciones matematicas(6)

print("**********************************************")
print("Bienvenido a la calculadora de 6 operaciones")
print("**********************************************")

print("******** MENÚ DE OPERACIONES **********")
print("1- SUMAR")
print("1- RESTA")
print("1- MULTIPLICACIÓN")
print("1- DIVISIÓN")
print("5- POTENCIACIÓN")
print("6- RADICACIÓN")
print("**************************************")

opcion= int(input("Ingrese una opción de operacion:"))

# Comienza la lógica del programa.
numero1=input("Ingrese el primer número. ")
numero2=input("Ingrese el segundo número:")


if opcion == 1:
    suma =  numero1 + numero2
    print(f"El resultado de sumar {numero1} y {numero2} es:{suma} ")
elif opcion == 2:
    resta=  numero1 + numero2
    print(f"El resultado de sumar {numero1} y {numero2} es:{resta} ")