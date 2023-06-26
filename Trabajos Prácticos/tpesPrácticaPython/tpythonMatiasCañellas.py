print("TP Evaluativo de Python: Matias Cañellas")
print("1- ¿Qué es Python")
print("2- ¿Qué se puede programar con Python?")
print("3- Imprimir un cálculo matemático en python")

print("Desarrollo del cuestionario")
print("1: Python es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.")
print("2: se utiliza para desarrollar aplicaciones de todo tipo, ejemplos: Instagram, Netflix, Spotify, Panda3D, entre otros.")
print("3: desarrolo el calculo")

# defino la función sumar
def sumar(a, b):
    resultado = a + b
    return resultado

# Implemento la función
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

print(f"La suma de ambos números es{sumar(numero1, numero2)}")