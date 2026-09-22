#ciclos for = Repite por cantidad de veces
"""
Repetir cantidad de veces
for i in range (5):
    print(f"{i}. Hola mundo ")
"""
# Configurar posicion inicial
"""
for i in range (1,5):
    print(f"{i}. Hola mundo ")
"""
"""
# Configurar posicion inicial
for i in range (2,12,2):
    print(f"{i}. Hola mundo ")
"""

    # Configurar posicion inicial, final y el incremento
"""
for i in range (0,101,5):
    print(f"{i}. Hola mundo ")
"""

#Adivinar el numero secreto 1

numero_secreto = 5
intentos = 3

for i in range (intentos): #Ciclo para que se escriba varias veces el numero
    numero = int(input("Adivina el numero secreto (1-10): "))
    
    if numero == numero_secreto :
        print("🎉 Felicidades Adivinaste. 🎉")
        break
    else:
        intentos_restantes = intentos - (i + 1)
        print(f"❌ Te quedan {intentos_restantes} Intentos")

#Adivinar el numero secreto 2
import random

numero_secreto = random.randint(1,10)
intentos = 3

for i in range (intentos): #Ciclo para que se escriba varias veces el numero
    numero = int(input("Adivina el numero secreto (1-10): "))
    
    if numero == numero_secreto :
        print("🎉 Felicidades Adivinaste. 🎉")
        break
    else:
        intentos_restantes = intentos - (i + 1)
        print(f"❌ Te quedan {intentos_restantes} Intentos")
        
#Verificar si no le quedan intentos y mostrar el numero
    if intentos_restantes == 0:
        print(f"😢 ¡Se te acabaron los intentos! El número secreto era {numero_secreto}.")

# Ejercicio 1: Mostrar la tabla de multiplicar de un número
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

for i in range(1, 11):          # recorre los valores del 1 al 10
    print(f"{numero} x {i} = {numero * i}")

# Ejercicio 2: Sumar los primeros n números naturales
n = int(input("Ingrese un número entero positivo: "))

suma = 0
for i in range(1, n + 1):
    suma = suma + i

print(f"La suma de los primeros {n} números naturales es: {suma}")

# Ejercicio 3: Contar cuántos números pares hay entre 1 y n
n = int(input("Ingrese un número entero positivo: "))

contador = 0
numero   = 1
while numero <= n:
    if numero % 2 == 0:
        contador = contador + 1
    numero = numero + 1

print(f"Hay {contador} números pares entre 1 y {n}")

# Ejercicio 4: Solicitar una contraseña hasta que sea correcta
clave_correcta  = "python2026"
clave_ingresada = input("Ingrese la contraseña: ")

while clave_ingresada != clave_correcta:
    print("Contraseña incorrecta, intente de nuevo")
    clave_ingresada = input("Ingrese la contraseña: ")

print("Contraseña correcta, acceso concedido")

# Ejercicio 5: Calcular el factorial de un número
n = int(input("Ingrese un número entero no negativo: "))

factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i

print(f"El factorial de {n} es: {factorial}")

