#PROBLEMA: Un usuario necesita crear un juego del tipo "cuenta tu propia historia"
#SOLUCION: crear un algoritmo del juego.
#ALGORITMO: creo un programa del juego 
while True:
    #PASO 1: Pedir el nombre del usuario
    nombre = input("ingrese su nombre")
    
    #PASO 2: imprimir la bienvenida al usuario.
    print(f"bienvenido {nombre}")
    
    #PASO 3: iniciar el juego
    resultado =input("sos messi por patear el primer penal de la tanta de penales de la final del mundo,te preparas para patear,donde pateas izquierda o derecha?")
    
    if resultado == "derecha":
        resultado= input("lloris adivino el penal y lo atajo. perdiste")
        break
    elif resultado == "izquierda":
        resultado= input("lloris se tira a la dereha y metes el gol")  
        
        resultado = input("sos el dibu martinez esta a punto de patear el jugador frances cual lado eliges tirarte. derecha o izquierda")
    if resultado == "derecha":
        print("Te tiraste a la derecha y francia metio el gol te deprimes y pierdes la final del mundo")
        break
    elif resultado=="izquierda":
             input(f"te tiraste a la izquierda y atajas subiendo el animo de todo el equipo.SOMOS TODOS MONTIEL")
