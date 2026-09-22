#Repaso clase pasada.
"""
var_nombre = input("Por favor ingrese su nombre: ")
var_edad = int(input(f"{var_nombre}) Por favor ingrese su edad: ")) #Solicitar edad.

#Condicion Validar si edad >= 18.
if var_edad >=18:
    print(f"{var_nombre} Usted es mayor de edad. ")
else: 
    print(f"{var_nombre} Usted en menor de edad. ") 
"""

# Ejercicio 1: Determinar si un número es positivo, negativo o cero. float = numero decimal
"""
numero = float(input("Ingrese un número: "))

if numero > 0:
    print(f"{numero} es positivo")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print("El número es cero")
    """

# Ejercicio 2: Verificar si una persona es mayor de edad
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# Ejercicio 3: Determinar si un número es par o impar
"""
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:      # si el residuo es 0 → es par
    print(f"El {numero} es par")
else:
    print(f"El {numero} es impar")
    """

# Ejercicio 4: Clasificar una nota académica
"""
nota = float(input("Ingrese la nota obtenida (0.0 a 5.0): "))

if nota > 5:
    print("Nota invalida")

elif nota >= 4.5:
    print("Desempeño superior")
elif nota >= 3.5:
    print("Desempeño alto")
elif nota >= 3.0:
    print("Desempeño básico")
elif nota < 0:
    print("Nota invalida")
else:
    print("Desempeño bajo")
"""

# Ejercicio 5: Determinar el mayor de tres números
"""
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3

print(f"El mayor de los tres números es: {mayor}")
"""

#Taller 2

# Ejercicio 1. Elaborar un algoritmo que solicite el nombre y edad de una persona y determine si es mayor o menor de edad.
"""
var_nombre = input("Por favor ingrese su nombre: ")
var_edad = int(input(" Por favor ingrese su edad: "))

#validar si la edad es negativo:

if var_edad <0:
    print(f"Error: La edad {var_edad} es invalida. ")

#Validar si la edad es menor a 18 y calcular cuantos años faltan

elif var_edad < 18:
    print(f" Te faltan: {18 - var_edad} años. ")
    
else: 
    print(f"Tu nombre es: {var_nombre} y Tu edad es: {var_edad}")
"""

# Ejercicio 2.
nombre =   input("Ingrese el nombre del estudiante: ")
nota= input("ingrese la nota: ")

nota= float (input("Ingrese la nota obtenida (0.0 a 5.0): "))

if nota<0 or nota >5.0:
   print("Nota invalida")

elif nota >= 4.5<= 5.0:
   print("excelente - Aprobado")

elif nota>= 3.5 >= 4.4: 
   print("Bueno - Aprobado")

elif nota >= 3.0 >= 3.4: 
   print("Aceptable - Aprobado")
   
else:
   print("Insuficiente - Reprobado")

print(f"su nombre {nombre} y su nota es {nota} :  ")

# Ejercicio 3. Elaborar un algoritmo que solicite nombre de un cliente y el valor total de una compra, y calcule el descuento segun el valor.
var_nombre = input("Por favor ingrese su nombre: ")
var_compra = float(input("El valor total de la compra: "))

if var_compra < 100000: 
    print("Sin descuento")
elif var_compra > 100000 and var_compra < 299999:
    print(f"Total descuento 10% {var_compra * 0.1}")
elif var_compra > 300000 and var_compra < 499999:
    print(f"Total descuento 15% {var_compra * 0.15}")
elif var_compra >= 500000:
    print(f"Total descuento 20%b {var_compra * 0.2}")

# Ejercicio 4. 
nombre_ciudad = input("Ingrese nombre de la ciudad: ")
Temperatura = float(input("La temperatura en grados celsius (10° a 32°:)"))

if Temperatura >= 32:
    print("Muy caliente")
elif Temperatura >= 26:
    print("Caliente")
elif Temperatura >= 18:
    print("Templado")
elif Temperatura >= 10:
    print("Fria")
elif Temperatura <= 10:
    print("Muy fria")

if Temperatura <18:
    print(f"Temperatura baja: llevar abrigo")

# Ejercicio 5: Empleado y salario
var_nombre = input("Ingrese nombre del empleado: ")
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
valor_hora = float(input("Ingrese el valor por hora: "))

salario = valor_hora * horas_trabajadas
var_seguridad = salario * 0.08 


if horas_trabajadas < 0 or valor_hora < 0:
    print("Error: Las horas trabajadas y el valor por hora deben ser números positivos.")

elif horas_trabajadas <= 160:

    salario_neto = salario - var_seguridad
    print(f""" === RESUMEN DE PAGO SALARIO ===
    -Salario: {salario} 
    -Seguridad social {var_seguridad} 
    -Salario neto es: {salario_neto}
    """)

elif horas_trabajadas > 160:

    horas_extras = horas_trabajadas - 160
    valor_horas_extras= (horas_extras* valor_hora )* 1.25
    salario_neto = (valor_hora * horas_trabajadas) + valor_horas_extras - var_seguridad

    print (f""" == RESUMEN DE PAGO SALARIO ==
    -Horas extras {horas_extras} Valor Horas Extras {valor_horas_extras}
    -Salario basico: {salario}
    -seguridad social {var_seguridad} 
    -salario total {salario_neto} 

""")