print("TP Evaluativo de Python: Nehuén Cerdan")
print("1- ¿Qué es Python?")
print("2- ¿Qué se puede programar con Python")
print("3- Imprimir un calculo matemático en Python")

print("Desarrollo del cuestionario:")
print("1: Python es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código, se utiliza para desarrollar aplicaciones de todo tipo, ejemplos: Instagram, Netflix, Spotify, Panda3D, entre otros.​")
print("2:Luego de la instalación, Python puede iniciarse a través del menú de Inicio. Como alternativa, también estará disponible desde cualquier símbolo del sistema o sesión de PowerShell al escribir python . Además, pip e IDLE pueden ser usados escribiendo pip o idle . IDLE también puede ser encontrado en el Inicio.")
print("3: Desarrollo el cálculo:")

# defino la función dunción
def sumar(a, b):
    resultado = a + b
    return resultado

# implemento la función
numero1 = int(input("Ingresar el primer número: "))
numero2 = int(input("Ingrese el sefundo número: "))

print(f"La suma de ambos número es: {sumar(numero1, numero2)}")
