#PROBLEMA: Un usuario necesita calcular la suma y resta de 2 numero.
#SOLUCION: Crear un algoritmo que solucione su problema.
#PROGRAMA: La solucion va a ser un programa para calcular la suma y la resta de 2 numeros.
while True:
    
  #PASO 1: pedir al usuario que ingrese los numeros a operar.

  numero1 = int(input("introduzca el primer numero"))
  numero2 = int(input("introduzca el segundo numero"))

  # PASO 2: Preguntar al usuario que operacion quiere realizr (menu) .

  print("1_suma")
  print("2_resta")

  #PASO 3: Pedir al usuario que ingrese una opcion.

  opcion = input("ingrese una opcion = ")

  # PASO 4: Realizar la operacion que selecciono el usuario.

  if opcion ==1:
     resultado = numero1 + numero2
  else:
     resultado = numero1 - numero2
    
  # PASO 5: Mostrar el resultado de la operacion al usuario.

  print(f"El resultado es: {resultado}")

