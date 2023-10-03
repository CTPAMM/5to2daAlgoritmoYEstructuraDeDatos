# PROBLEMA: Un usuario necesita crear un juego del tipo "cuenta tu propia historia"
#SOLUCIÓN: Crear un ALGORITMO del juego 
#ALGORITMO: Creo un programa del juego

while True:
    #PASO 1: Pedir el nombre del usuario
    nombre = input("ingrese su nombre:")

    #PASO 2: Imprimir la bienvenida al usuario.
    print(f"bienvenido{nombre}")

    # PASO 3: Iniciar el juego 
    resultado = input("Estas en el bosque perdido y hay dos caminos, puedes ir a la derecha/izquierda ")

    if resultado == "izquierda":
        print("te cruzas con un oso y te ataca hasta el punto de morir") 
        break
    elif resultado =="derecha":
        resultado = input("te encontras con un prado hermoso y una cueva oscura para seguir el camino  volver/seguir")
        if resultado == "volver":
            print("perdiste porque un oso andaba cerca y te ataca")
            break
        elif resultado == "seguir":
            input(f" lograste llegar al pueblo con tu familia felicidades")