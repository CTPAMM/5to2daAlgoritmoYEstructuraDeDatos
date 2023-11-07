import serial
from time import sleep

ArduinoSerial = serial.Serial('/dev/ttyACM0', 9600) #Inicializamos el puerto de serie a 9600 baudios
sleep(5)

while True:
   # PASO 1: Mostrar menú de opciones al usuario.

   print("************MENÚ DE OPCIONES******************")
   print("Mover el SERVO (ingrese un número entre 0-180): ")
   print("Salir del menú (ingrese '200'): ")
   print("**********************************************")
   
   # PASO 2: Pedir al usuario ingrese su opción.

   opcion = int(input("Ingrese su opción: "))
   
   # PASO 3: Decidir operación a realizar según la opción del usuario.

   if(opcion >= 0 and opcion <= 180):
      ArduinoSerial.write(str(opcion).encode()) #Enviamos el número por serial, codificado en Unicode.
   elif opcion == 200:
      print("¡Gracias por utilizar nuestro programa!")
      break
   else:
      print("¡Ingresó una opción incorrecta! Por favor vuelvalo a intentar.")
