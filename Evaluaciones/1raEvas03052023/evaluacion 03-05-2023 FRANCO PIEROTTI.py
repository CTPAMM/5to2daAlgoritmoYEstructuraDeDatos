# Evaluacion del 03-05-2023
# Franco Agustin Pierotti
# 5to 2da

# 1er Programa
# imprima en pantalla un menu de 4 opciones a eleccion.

print ("*******menu de electrodomesticos********")
print ("1- computadora")
print ("2- heladera")
print ("3- televisor")
print ("4-celular")
print ("**********")

# 2do programa
# imprimir por teclado 2 numeros e imprima por pantalla el resultado de su multiplicacion. 

numero1=int(input("introduzca el valor del primer numero: "))
numero2=int(input("introduzca el valor del segundo numero:"))

print("la multiplicacion de los numeros es: ")
print(numero1 * numero2)


# 3er Programa
# Crear una lista con 4 elementos e imprimiral en pantalla.

lista_marcas=("nike", "adidas", "puma", "kappa")

print(lista_marcas)
for marca in lista_marcas:
    print(marca)

# 4to Programa 
# crear una calculadora de perimetro del rectangulo.

base = int(input("introduzca el valor de la base: "))
altura =int(input("introduzca el valor de la altura"))
respuesta = (base*2) + (altura*2) 
print("el perimetro del rectangulo es: ")
print (respuesta)