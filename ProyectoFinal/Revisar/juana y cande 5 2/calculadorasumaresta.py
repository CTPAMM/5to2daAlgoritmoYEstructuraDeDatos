#POBLEMA:un usario necesita calcular la SUMA y la RESTA de 2 numeros.
#SOLUCION:crear un algoritmo qie solucione su problema.
#PROGRAMA:la solucion va a ser un programa para calcular la suma y la resta de 2 numeros.

while True:
#PASO 1: pedir al usuario que ingrese los numeros a operar.

 numero1=int(input("introduzca el primer numero:"))
 numero2=int(input("introduzca el segundo numero"))

#PASO 2:preguntar al usuario que operacion quiere realizar(menu).

print("si desea restar ingrese 1")
print("si desea sumar ingrese 2")

#PASO 3: pedir al usuario que ingrese una opcion.

opcion= int(input("ingrese una opcion"))
            

 
#PASO 4: realizar la operacion que selecciono el usuario.

if opcion==1:
    resultado=numero1+numero2
else:
      resultado=numero1-numero2
      
#PASO 5: mostrar el resultado de la operacion al usuario

print (f"la suma entre{numero1} y{numero2}es:{resultado}")       