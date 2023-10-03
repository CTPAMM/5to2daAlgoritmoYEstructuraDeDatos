#PROBLEMA: Un usuario necesita crear un juego del tipo "Cuenta" tu propia historia"
#SOLUCION: Crear un ALGORITMO del juego. 
#ALGORITMO: Creo un del juego

while True:
    # PASO 1: Pedir el nombre del usuario
   nombre = input("ingrese su nombre de usuario")
   
   # PASO 2: Imprimir la bienvenida al usuario.
   print(f"bienvenido {nombre}")
   
   # PASO 3: Iniciar el juego
   resultado = input("estas caminando por un bosque, puedes ir a la izquierda o a la derecha. ¿que camino elijes? (izquierda/derecha)")
   
   if resultado == "izquierda":
       print("Te cruzas con una manada de lobos. Perdiste")
       break
   elif resultado == "derecha": 
       resultado = input("Seguis caminando y te das cuenta que te quedas sin comida. ¿Seguis o volves? (seguir/volver)")
       if resultado == "volver":
           print("Perdiste porque habia comida cerca")
           break
       elif resultado == "seguir":
           print("ganaste porque encontraste un auto")
           break
       