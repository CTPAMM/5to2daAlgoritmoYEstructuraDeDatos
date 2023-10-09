# PROBLEMA: un usuario necesita crear un juego del tipo "cuenta tu propia historia"
# SOLUCION: crear uun ALGORITMO del juego.
# ALGORITMO: creo un programa del juego

while True:
    # PASO 1: pedir el nombre del usuario 
    nombre = input("ingrese su nombre: ")
    
    #PASO 2: imprimir la bienvenida al usuario.
    print(f"bienvenido {nombre:}")
    
    #PASO 3: iniciar el juego
    resultado = input("estas en un camino de piedras, a unos metros el camino se separa en dos, el camino de la izquierda y el camino de la derecha ¿cual eliges? (izquierda/derecha)")
    
    if resultado == "izquierda":
      resultado = input("te encontras con tu papá pero es un zombie y te mata. Perdiste")
      break
    elif resultado == "derecha":
        resultado = input("seguis caminando, pero te agarra mucha hambre, lo peor que a pocos metros se te acerca una manada de bufalos ¿que eliges?(volver/seguir)")
        if resultado == "volver":
            print("perdiste porque los bufalos no te iban a hacer daño, y a unos pasos mas había un local de comida rapida")
            break
        elif resultado == "seguir":
            input(f"decides seguir el camino esquivando a los bufalos, a los pocos pasos te econtras un local de comida rapida y disfrutas de la comida. ganaste")
    print("¡ Gracias por participas !")