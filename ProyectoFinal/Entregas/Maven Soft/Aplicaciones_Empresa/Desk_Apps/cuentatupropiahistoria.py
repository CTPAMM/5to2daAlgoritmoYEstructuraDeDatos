#problema:un usuario necesita crear un juego del tipo "cuenta tu propia historia"
#solucion:crear un algoritmo del juego
#algoritmo creo un programa de juego

while True:
    #paso 1: pedir el nombre del usuario
    nombre = input("ingrese su nombre")
    
    #paso 2: imprimir la bienvenida al usuario
    print(f"bienvenido/a {nombre}")
    
    #paso 3: iniciar el juego
    opcion = input("estas caminando por un bosque y entras a una cueva, seguis caminando y te crusas con dos caminos. que elegis? derecha o izquierda?")
    
    if opcion == "izquierda": 
        print("te crusaste a un oso y te mato. perdiste")
        break
    elif opcion == "derecha":
        opcion = input("seguis caminando y te cruazas con un puente viejo o trepar un muro para cruzar el rio. que opcion elegis? puente o muro?")
        if opcion == "puente":
            print("mientras ibas cruzando el puente, el puente se rompio y caiste al vacio. perdiste")
            break
        elif opcion == "muro":
             opcion = input("trepaste el muro y seguis caminando por la cueva, ves dos caminos, uno vez que te saca a fuera y el otro sigue por la cueva, que elegis, salir o seguir?")
             if opcion == "salir":
                 print("saliste de la cueva y seguisyte camiando por el bosque asta que llegaste a la cueva. ganaste!!!! gracias por jugar")
             elif opcion == "seguir":
                 print("seguiste y te moriste porque caiste en un pozo. perdiste")
                 break
