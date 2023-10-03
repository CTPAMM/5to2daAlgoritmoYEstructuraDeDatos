#PROBLEMA: Un usuario necesita crear un juego del tipo "cuenta tu propia historia"
#SOLUCION: Crear un algoritmo del juego.
#ALGORITMO: Creo un programa del juego.

while True:
    # PASO 1: Pedir el nombre del usuario
    nombre = input("ingrese su nombre")
    
    # PASO 2: imprimir la bienvenida al usuario.
    print(f"{nombre}")
    
    # PASO 3: iniciar el juego
    resultado = input("estas durmiendo y te despiertas, puedes (seguir durmiendo o levantarte)")
    
    if resultado == "seguir durmiendo":
        print("te pierdes todo el dia. perdiste")
        break
    elif resultado == "levantarte":
        resultado = input("te levantas y te das cuenta que tenes que ir al baño (baño/no baño)")
        if resultado == "baño":
            print("bien, vas a orinar y a lavarte los dientes")
        elif resultado == "no baño":
            input(f"te descompones y te llevan al hospital. perdiste")

print("¡ Gracias Por Participar !")       