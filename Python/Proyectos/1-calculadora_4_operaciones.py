# -------------------------------------------------------------
# Fecha: 10-05-23
# Estudiante: Su Nombre Completo
# Título: Calculadora de 4 operaciones V2 (aplicando funciones)
#--------------------------------------------------------------

# Función para sumar dos números

def sumar(a, b):
    return a+b

def restar(a, b):
    return a-b

def multiplicar(a, b):
    return a*b

def dividir(a, b):
    return a/b

print("Ingrese dos números: ")

num1= float(input("Introduzca el primer número: "))
num2= float(input("Introduzca el segundo número: "))

print("¿Qué operación desea realizar?")
print("1- Sumar")
print("2- Restar")
print("3- MUltiplicar")
print("4- Dividir")

operacion = input("Introduzca una opción: ")

if operación == "1":
    resultado= sumar(num1, num2)
    print(f"La suma es igual a: {resultado}")


    

    
    



