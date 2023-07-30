# Evaluación del 03/05/23
# Su nombre completo 
# 5° 2°

# 1° Programa
# Imprima en plantilla un menú de 4 opciones a elección

print(menú)
print("1- Carne")
print("2- Pollo")
print("3- Pescado")
print("4- Cordero")

# 2° Programa
# Ingrese por teclado 2 números e imprima por pantalla el resultado de su multiplicación

numero1=int(input("Introduzca el valor del primer número: "))
numero2=int(input("Introduzca el valor del segundo número: "))

print("La multiplicación de los número es: ")
print(numero1 * numero2)

# 3° Programa
# Crear una lista con 4 elementos e imprimirla en pantalla 

Lista_juegos = ["Cs", "Minecraft", "Fifa", "Cod"]

print(Lista_juegos)

for juego in Lista_juegos:
    print(juego)

# 4° Programa
# Crear una calculadora de perímetro del rectángulo

base = int(input("Introduzca el valor de la base: "))
altura = int(input("Introduzca el valor de la altura: "))

respuesta = (base * 2) + (altura * 2)

print("El perímetro del rectangulo es: ")
print(respuesta)