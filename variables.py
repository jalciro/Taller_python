# Taller 1 Ejercicios a resolver

# 1. Solicitar el largo y el ancho de un terreno rectangular y calcular su perímetro.

print("Ejercicio 2: Área de un rectángulo")
base   = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

area = base * altura

print(f"El área del rectángulo es: {area}")

# 2. S


print("Ejercicio 1: Sumados numeros")
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print(f"Resultado: {numero1 + numero2}")



#Ejercicio 3
print("Ejercicio 3: Conversión de minutos a horas y minutos")

horas   = minutos_totales // 60   # división entera → horas completas
minutos = minutos_totales % 60    # módulo → minutos restantes

print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos} minutos")

#Ejercicio 4
print("Ejercicio 4: Cálculo del precio con descuento")
precio    = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

valor_descuento = precio * (descuento / 100)   # valor que se descuenta
precio_final    = precio - valor_descuento      # precio con descuento

print(f"El precio final a pagar es: {precio_final}")

#Ejercicio 5
print("Ejercicio 5: Intercambio de valores entre dos variables")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

auxiliar = a   # guardar temporalmente el valor de a
a = b          # a toma el valor de b
b = auxiliar   # b toma el valor original de a

print(f"Después del intercambio: a = {a} , b = {b}")


#Taller 1
#Ejercicio 1
print("Ejercicio 1: Solicitar el largo y ancho de un terreno rectancular y cacular su perimetro")
largo = float(input("Ingrese el largo del terreno en metros: "))
ancho = float(input("Ingrese la ancho del terreno en metros: "))

Perimetro = largo * ancho

print(f"El perimetro del rectanculo es: {(largo*2  + ancho*2)}")


print("*"*80)

#Ejercicio 2
print("Ejercicio 2: Solicitar tres numeros y mostrar su promedio")
numero1=float(input("Ingrese el numero 1: "))
numero2=float(input("Ingrese el numero 2: "))
numero3=float(input("Ingrese el numero 3: "))

print(f"el promedio de los numeros es {(numero1 + numero2 + numero3)/3}")

#Ejercicio 4
print("Ejercicio 4: Solicitar un valor en pesos colombianos y mostar su equivalencia aproximado en dolares (tasa fija: 1 USD = 4000 COP)")
pesos = float(input("Ingresa la cantidad de numero a convertir a dolares "))
dolar = pesos/4000

print(f"Este es el valor en dolares" , dolar)

#Ejercicio 5
print("Ejercicio 5: Conversión de segundos a horas")
segundos_totales = float(input("ingrese los segundos "))
print(f"tiempo en minutos {segundos_totales /60}")
print(f"tiempo en horas {segundos_totales /3600}")

