# 1)
mensaje = "Hola Mundo!"
print(mensaje)

# 2) 
nombre = input("Por favor, ingresa tu nombre: ")
print(f"Hola {nombre}!")

#3)
nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Ahora, ingresa tu apellido: ")
edad = input("¿Cuál es tu edad?: ")
residencia = input("¿Dónde resides?: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4)
import math

radio = float(input("Por favor, ingresa el radio del círculo: "))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

# 5)
segundos = int(input("Ingresa una cantidad de segundos: "))
horas = segundos / 3600

print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# 6)
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# 7)
num1_str = input("Ingresa el primer número (distinto de 0): ")
num2_str = input("Ingresa el segundo número (distinto de 0): ")

num1 = float(num1_str)
num2 = float(num2_str)

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"La suma de los números es: {suma}")
print(f"La resta de los números es: {resta}")
print(f"La multiplicación de los números es: {multiplicacion}")
print(f"La división de los números es: {division}")

# 8)
peso = float(input("Por favor, ingresa tu peso en kilos: "))
altura = float(input("Ahora, ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

print(f"Tu índice de masa corporal es: {imc:.2f}")

# 9)
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32

print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}°F")

# 10)

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

suma = numero1 + numero2 + numero3

promedio = suma / 3

print(f"El promedio de los tres números es: {promedio:.2f}")