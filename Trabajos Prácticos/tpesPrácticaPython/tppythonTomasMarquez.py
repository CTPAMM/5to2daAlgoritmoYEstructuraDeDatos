print("tp evaluativo de python")
print("1- ¿que es python?")
print("2- ¿que se puede programar con python?")
print("3- imprimir un calculo matematico en python")

print("desarrollo del cuestionario")
print("1: es un lenguaje de programacion amplio que se usa en aplicaciones web, desarrllo de software, etc")
print("2: se puede programar aplicaciones web")
print("3: desarrollo del calculo: ")

#defino una funcion sumar
def sumar(a, b):
    resultado= a+b
    return resultado 

#implemento la funcion
numero1 = int(input("ingrese el primer numero"))
numero2 = int(input("ingres el segundo numero"))



print(f"la suma de ambos numeros es {sumar (numero1, numero2)}")
