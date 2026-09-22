# Crear lista vacia
"""
lista_nombres = []

while True:
    variable_nombre = input("Ingrese un nombre: ")
    if variable_nombre != 'salir':
        lista_nombres.append(variable_nombre)

    if variable_nombre == "salir":
        print("Nombres guardados: ") 
        print(lista_nombres)
        break
"""
#Crear nombre
"""
nombre = input ("Ingrese su nombre: ")
print(f"Nombre en Mayusculas {nombre.upper()}")
print(f"Nombre en Minusculas {nombre.lower()}")  

if nombre.lower() == "javier":
    print("Hola Javier")
else:
    print("Tu no eres Javier")
"""

#Lista mascotas

lista_perros = []
lista_gatos = []

while True:
    try:
        pregunta = int(input("""
        Seleccionar Opcion:
        1: Registrar perro
        2: Registar gato
        3: Mostrar listado de perros
        4: Mostrar listado de gatos
        5: Salir    
        """))

        # Valida qué opción escogió el usuario
        if pregunta == 1:
            perro = input("Cual es el nombre del perro: ")
            lista_perros.append(perro)
        elif pregunta == 2:
            gato = input("Cual es el nombre del gato: ")
            lista_gatos.append(gato)
        elif pregunta == 3:
            print("Listado perros: ")
            print(lista_perros)
        elif pregunta == 4:
            print("Listado gatos: ") 
            print(lista_gatos)
        elif pregunta == 5:
            print("Saliendo del sistema")
            break
        else:      
            print("Opcion Invalida")

    except ValueError:
        print("Ingrese un numero valido")
   


