#----------------------------------------------------------
# Fecha: 31-07-23
# Estudiante: Su Nombre Completo
# Título: Listas y Tuplas.
#----------------------------------------------------------

#---------------------------------------------------------------------
#  LISTAS
#---------------------------------------------------------------------

# Declarar y definir las variables
lista_marcas = ['Fiat', 'Ford', 'Chevrolet', 'Mercedez Benz']
print(lista_marcas)

# Bucle FOR para recorrer los elementos de la lista
for marca in lista_marcas:
    print(marca)

# Imprimir un elemento concreto de la lista
print(f"El segundo elemento de la lista es: {lista_marcas[1]}")

# Reemplazar un elemento de la lista
lista_marcas[3] = 'Audi'
print(lista_marcas)

# Agregar un elemento en la lista en la última posición
lista_marcas.append('Toyota')
print(lista_marcas)

# Agregar un elemento en la lista en una posición concreta
lista_marcas.insert(2, 'Subaru')
print(lista_marcas)

# Eliminar un elemento concreto de la lista
lista_marcas.pop(2)
print(lista_marcas)

# Ordenar alfabeticamente la lista
lista_marcas.sort()
print(lista_marcas)


