# PROBLEMA: Un usuario necesita un menu de opciones para realizar las tareas 
# SOLUCION: Crear un algoritmo que permita seleccionar opciones al usuario
# PROGRAMA: crear un programa con python

while True:
    #Paso 1: Presentar el menu de opciones 
    print ("***********************MENU DE IDIOMAS*************************")
    print("1-Ingles")
    print("2-Español")
    print("-Aleman")
    print("***************************************************************")
    #Paso 2: pedir al usuario que ingrese su opcion
                        
    opcion = int(input("ingrese su opcion: "))
                    
    #Paso 3: Decidir sobre la opcion del usuario.
                    
    if opcion == 1:
            print("Welcome to visual studio code,is a standalone source code editor that runs on Windows, macOS, and Linux. The top choice for web and JavaScript developers, with extensions to support almost any programming language.")
    elif opcion == 2:
            print("bienvenido a visual studio code, es un editor de código fuente independiente que se ejecuta en Windows, macOS y Linux. La elección principal para desarrolladores web y JavaScript, con extensiones para admitir casi cualquier lenguaje de programación.")
    elif opcion == 3:
            print("Willkommen zu visual studio code,ist ein eigenständiger Quellcode-Editor, der unter Windows, macOS und Linux läuft. Die erste Wahl für Web- und JavaScript-Entwickler mit Erweiterungen zur Unterstützung nahezu jeder Programmiersprache")
    else:
            print("¡opcion incorrecta. Vuelva a intertarlo! ")
        
    
        
        