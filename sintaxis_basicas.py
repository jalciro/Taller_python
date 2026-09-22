# MOSTRAR EL CONTENIDO DE UNA VARIABLE

# Una variable permite almacenar un dato para utilizarlo
# posteriormente dentro del programa.

nombre = "Javier" # Variable de tipo string (cadena de texto)
documento = 71691299 # Variable de tipo int (número entero)
direccion = "Calle 38F N° 28-26 Medellin" # Variable de tipo string (cadena de texto)
tiene_deudas = True # Variable de tipo bool (booleano)

# MOSTRAR EL CONTENIDO DE UNA VARIABLE
print(nombre)

# CONCATENACIÓN USANDO +
print("concatenación usando +")
print("=" * 30)

# El operador + permite unir textos.
# Cuando usamos +, todos los elementos deben ser strings.

# documento es un entero (int), por lo que esta línea
# produciría un error:

# Para solucionarlo, podemos convertir el número a texto
# utilizando str().
print("Mi nombre es: " + nombre)

# CONCATENACIÓN USANDO ,
print("\nCONCATENACIÓN USANDO ,")
print("=" * 30)

# Al utilizar comas, Python permite mostrar diferentes
# tipos de datos sin necesidad de convertirlos a string.
print("Mi nombre es:", nombre, "y mi documento es:", documento)

# CONCATENACIÓN USANDO F-STRINGS
print("\nCONCATENACIÓN USANDO F-STRINGS")
print("=" * 30)

# Las f-strings permiten insertar variables directamente
# dentro de un texto.

# Se coloca la letra f antes de las comillas y las variables
# se escriben entre llaves { }.
print(f"Mi nombre es: {nombre} y mi documento es: {documento}")

# F-STRINGS CON VARIAS VARIABLES
print("\nMOSTRAR VARIAS VARIABLES CON F-STRINGS")
print("=" * 30)

# Las f-strings también permiten crear textos
# de varias líneas utilizando triple comilla.
print(f"""
Nombre:         {nombre}
Documento:      {documento}
Dirección:      {direccion}
¿Tiene deudas?: {tiene_deudas}
""")

# F-STRINGS CON COMILLAS SIMPLES
# También podemos utilizar tres comillas simples (''')
# para crear textos de varias líneas.
print("=" * 30)

print(f"""
Nombre:         {nombre}
Documento:      {documento}
Dirección:      {direccion}
¿Tiene deudas?: {tiene_deudas}
""")

# SALTO DE LÍNEA EN PYTHON

# \n representa un salto de línea.
# Salto de línea al inicio del texto
print(f"\n Hola, {nombre}!")

# Salto de línea al final del texto
print(f"Bienvenida {nombre} a Python.\n")

# ============================================================
# OPERADORES ARITMÉTICOS EN PYTHON
# ============================================================
numero1 = 10
numero2 = 3

suma           = numero1 + numero2   # 13
resta          = numero1 - numero2   # 7
multiplicacion = numero1 * numero2   # 30
division       = numero1 / numero2   # 3.333...
division_entera= numero1 // numero2  # 3
residuo        = numero1 % numero2   # 1
potencia       = numero1 ** numero2  # 1000

print(f"""
Resultado de Operaciones Aritméticas:
suma:            {numero1} +  {numero2} = {suma}
resta:           {numero1} -  {numero2} = {resta}
multiplicacion:  {numero1} *  {numero2} = {multiplicacion}
division:        {numero1} /  {numero2} = {division:.4f}
division_entera: {numero1} // {numero2} = {division_entera}
residuo:         {numero1} %  {numero2} = {residuo}
potencia:        {numero1} ** {numero2} = {potencia}
""")