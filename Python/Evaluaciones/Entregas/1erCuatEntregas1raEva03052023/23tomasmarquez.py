# Evaluacion del 03/05/2023
# Tomas Marquez 
# 5°2°

# 1° Programa
#imprima en pantalla un menu de 4 opciones a eleccion

print("autos")
print("1- supra mk4")
print("2- gtr r35")
print("3- toyota supra")
print("4- gold trend")

# 2° programa
# ingrese por programa 2 numeros e imprima por pantalla el resultado de su multiplicacion

numero1 = int(input("introduzca un numero: "))
numero2 = int(input("introduzca otro numero: "))

print("la multiplicacion de los numeros es: ")
print(numero1 * numero2)

# 3° programa
#Crear una lista con 4 elementos e imprimir en pantalla
juegos = ["roblox", "call of duty", "project zombie", "clash royale"]# esto es una lista
print ("-- listado de juegos fav---")
print ("resultado del bucle clash royale")
for juegos in juegos: 
    if juegos == "clash royale":
        continue
    print (f"-color {juegos}.")

# 4° programq
#Crear una calculadora de perimetro del ractangulo

#declaracion y definicion de variables 

altura = int(input("introduzca el valor del altura: "))
base = int(input("introduzca el valor del base: "))

respuesta = (altura * 2) + (base * 2)

print("el perimetro del rectangulo es: ")
print(respuesta)