import serial # use 'pip install pyserial' to install the lib

ArduinoSerial = serial.Serial('/dev/ttyACM0', 9600)


while True:
    # PASO 1: Mostrar menú de opciones al usuario.
    
    print("************MENÚ DE OPCIONES******************")
    print("Encender LED (ingrese 'encender')")
    print("Apagar LED (ingrese 'apagar')")    
    print("Salir del menú (ingrese 'salir')")
    print("**********************************************")
    
    # PASO 2: Pedir al usuario ingrese su opción.

    opcion = input("Ingrese su opción: ")
    
    # PASO 3: Decidir operación a realizar según la opción del usuario.

    if opcion == 'encender':
        ArduinoSerial.write(b'encender')
    elif opcion == 'apagar':
        ArduinoSerial.write(b'apagar')
    elif opcion == 'salir':
        print("¡Gracias por utilizar nuestro programa!")
        break
    else:
        print("¡Ingresó una opción incorrecta! Por favor vuelvalo a intentar.")
    