print("TP Evaluativo de Phyton")
print("1-¿que es phyton?")
print("2-¿que se puede programar con phyton")
print("3-Imprimir un calculo matematico")

print("desarrolo del cuestionario:")
print("1:Python es un lenguaje de programación ampliamente utilizado en las aplicaciones web, el desarrollo de software, la ciencia de datos y el machine learning  ")
print("2: Desarrollo de aplicaciones web con frameworks como Django o Flask , Automatización de tareas y procesamiento de datos. Machine learning y deep learning con librerías como TensorFlow y PyTorch. desarrollo de jegos con librerías como Pygame  ")
print("3: desarrollo el calculo  ")


#defino el calculo 
def sumar(a,b):
    resultado = a + b 
    return resultado 

#implemento la funcion
numero1 = int(input("Ingrese el primer numero:"))
numero2 = int(input("ingrese el segundo numero:"))

print(f"la suma de ambos numeros es {sumar(numero1,numero2)}")
