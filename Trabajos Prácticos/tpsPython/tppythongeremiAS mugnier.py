print("TP Evaluativo de Python")
print("1- ¿Que es Python?")
print("2- ¿Que se puede programar con Python?")
print("3- Imprimir Un calculo matemático en Python ")

print("Desarrollo de cuestionario")
print("1- Python es un lenguaje de programación ampliamente utilizado en las aplicaciones web, el desarrollo de software, la ciencia de datos y el machine learning (ML)")
print("2- Desarrollo de aplicaciones web,Automatización de tareas y procesamiento de datos, Machine learning y deep learning con librerías,Desarrollo de juegos con librerías.")
print("3- Desarrollo el calculo")

# defino la función sumar
def sumar(a, b):
    resultado = a + b
    return resultado

# implemento la función
numero1 = int(input("Ingrese el primer número:"))
numero2 = int(input("Ingrese el segundo número:"))
 


print(f"La suma de ambos números es: {sumar(numero1, numero2)}")
