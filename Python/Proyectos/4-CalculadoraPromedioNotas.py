#*******************************************************************************
# Fecha:
# 
# Estudiante:
# 
# Curso:
# 
# Trabajo Práctico: Calculadora de Promedio de Notas
# 
# Objetivo: Crear un programa que calcule el promedio de notas de un estudiante.
# 
# Instrucciones:
#   Listar la cantidad de asignaturas o materias.
#   Usando un bucle, solicitar al usuario que ingrese la nota de cada asignatura.
#   Calcular el promedio de las notas ingresadas.
#   Mostrar en pantalla el promedio calculado con un mensaje informativo.
#*******************************************************************************

   
# Listar materias
lista_materias = ['Matemáticas', 'Lengua', 'Física', 'Química']

cantidad_asignaturas = len(lista_materias)

# Inicializar una variable para almacenar la suma de notas
suma_notas = 0

# Bucle para ingresar las notas de cada asignatura
for materia in lista_materias:
    nota = float(input(f"Ingrese la nota de la asignatura {materia}: "))
    suma_notas += nota

# Calcular el promedio
promedio = suma_notas / cantidad_asignaturas

# Mostrar el promedio
print(f"El promedio de notas las materias {lista_materias} es: {promedio}")
