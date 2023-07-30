# Evalución del 03/05/2023
# Nehuén Cerdan
# 5° 2°

# 1° Programa
# Imoprimima en panatalla un menú de opciones a elección.

print("***MENU DE MARCAS DE AUTOS JDM***")
print("1-Toyota")
print("2-Nissan")
print("3-Mazda")
print("4-Mitsubishi")
print("*****************************")

# 2° Programa
# Ingrese por teclado 2 números e imprima por pantalla el resultado de su multiplicación.

numero1=int(input(" Intruduzca el valor del primer número:"))
numero2=int(input(" Introduzca el valor del segundo número:"))

print("La suma de los números es:")
print(numero1 * numero2)

# 3° Programa
# Crear una lista con 4 elementos e imprimirla en panatalla.

lista_autos_jdm=["Nissan", "Mitsubishi", "Mazda", "Toyota"]

print(lista_autos_jdm)
for auto in lista_autos_jdm:
    print(auto)
    
# 4° Programa
# Crear una calculadora de perímetros del rectángulo,

Base = int (input("Introduzca el valor de la base: "))
altura = int(input(" Introduzca el valor de la altura: "))

respuesta = (base*2) * (altura*2)

print(" La superficies del rectangulo es: ")
print (respuesta)