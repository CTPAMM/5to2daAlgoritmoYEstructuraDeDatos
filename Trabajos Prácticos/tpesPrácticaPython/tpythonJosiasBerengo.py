print ("tp evaluativo de python: josias berengo")
print ("1- ¿que es python?")
print ("2- ¿ que se puede programar en python?")
print ("3-imprimir un calculo matematico en python")

print ("desarollo del cuetionario:")
print ("1:python es un programa de pagina web")
print ("2: se pueden pragramar paginas web")
print ("3: desarollo el calculo")

# defino la funcion sumar 
def sumar (a, b):
    resultado = a + b 
    return resultado 

    # implemento la funcion
número1 = int(input ("ingrese el primer número:"))
número2 = int(input ("ingrese el segundo número:"))

    print (f"la suma de ambos números es {sumar(número1, número2)}")