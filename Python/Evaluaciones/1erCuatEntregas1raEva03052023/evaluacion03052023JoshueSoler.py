# evaluacion del 03-05-2023
# joshue soler
#5° 2°

# 1° programa
# imprima en pantalla un menu de 4 opciones a eleccion.

print("********menu********")
print("1-pc gamer")
print("2-play 5")
print("3-juegos ilimitados")
print("4-xbox one")
print("*********************")

#2° programa
#ingrese por teclado 2 numeros e imprima en pantalla el resultado de su multiplicacion.

numero1 = int(input("introduzca el valor del primer numero"))
numero2 = int(input("introduzca el valor del segundo numero"))
 
print("la multiplicacion de los numeros es ")

print(numero1*numero2)

#3° programa 
#crear una lista con 4 elementos e imprimirla en pantalla 

lista_zapatillas = ("asics","puma" ,"munich","mizuno",)

print(lista_zapatillas)

for zapatilla in lista_zapatillas:

       print(zapatilla)


# 4° programa
# crear una calculadora de perimetro del rectangulo

base = int(input("introduzca el valor de la base:"))
altura = int(input("introduzca el valor de la altura:"))

#realiza el calculo
respuesta = (base *2) + (altura *2)

#imprime la respuesta 
print("el perimetro del rectangulo es :")
print (respuesta)