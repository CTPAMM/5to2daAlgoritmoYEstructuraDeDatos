# evaluación del 03-05-23
# rios giovanni gabriel
#5°2
# 1° programa 
# imprimir en pantalla un menu de 4 opciones a elección

print("*candidatos a balon de oro:")
print("1- benzema")
print("2-messi")
print("3-julian alvarez")
print("4-haaland")
print("5-mbappe")

# 2° programa
# ingrese por teclado 2 numeros e imprima por pantalla el resultado de su multiplicación
 
numero1 = int(input("introduzca el valor del primer numero: "))
numero2 = int(input("introduzca el valor del segundo numero: ")) 
print("la multiplicación de los numeros es: ")
print(numero1*numero2)


# 3° programa 
#crear una lista con 4 elementos e imprimirla en pantalla

lista_mejores_juegos = ("resident evil","the last of us","minecraft","clash royal")

print(lista_mejores_juegos)

for juegos in lista_mejores_juegos:
    print(juegos)
    
# 4° programa 
# crear una calculadora de perimetro del rectángulo

base = int(input("introduzca el valor de la base: "))
altura = int(input("introduzca el valor de la altura"))

# Realiza el calculo

respuesta = (base * 2) + (altura * 2)

print("el perimetro del rectangulo es : ")
print(respuesta)