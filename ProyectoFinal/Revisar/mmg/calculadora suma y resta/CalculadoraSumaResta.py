#PROBLEM:Un usuario necesita calcular la SUMA y la RESTA de 2 números.
#SOLUCION:Crear un algoritmo que solucione su problema.
#PROGRAMA:La solución va a ser un programa para calcular la suma y la resta de 2 números

#PASO 1:Pedir al usuario que ingresenlos números a operar.

numero1 =int(input("ingresá el primer numero: "))
numero2 =int(input("ingresá el segundo numero: "))

print(f"el número 1 es : {numero1} y el numero 2 es: {numero2}")
#PASO 2: Mostrar menú de operacion.

opción = input("¿que operación quiere realizar (suma/resta)?")

#PASO 3: Pedir al usuario que ingrese ua operación

if opción == "suma":
    resultado = numero1 + numero2
else:
    resultado = numero1 + numero2


#PASO 4: Realizar la operación que seeccionó el usuario.

print(f"El resultado de la {opcion} entre el {numero1} y el {numero2} es: {resultado}")


#PASO 5: