# 1)
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

# 2) 
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3)
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4)
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5)
contrasena = input("Ingrese una contraseña (8 a 14 caracteres): ")

if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6)
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se ajusta exactamente a los criterios de sesgo")

# 7) 
texto = input("Ingrese una frase o palabra: ")

if texto[-1].lower() in "aeiou":
    texto += "!"
print(texto)

# 8)
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 para mayúsculas, 2 para minúsculas, 3 para primera letra mayúscula: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")

# 9)
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

# 10)
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

# Normalizamos la fecha como tupla (mes, dia)
fecha = (mes, dia)

# Definimos rangos de fechas
invierno_norte = [ (12,21), (3,20) ]
primavera_norte = [ (3,21), (6,20) ]
verano_norte    = [ (6,21), (9,20) ]
otonio_norte    = [ (9,21), (12,20) ]

def esta_en_rango(fecha, inicio, fin):
    """Devuelve True si una fecha (mes,dia) está entre inicio y fin (inclusive)."""
    if inicio[0] < fin[0] or (inicio[0] == fin[0] and inicio[1] <= fin[1]):
        # Rango dentro del mismo año
        return inicio <= fecha <= fin
    else:
        # Rango cruza fin de año (ej: 21 dic - 20 mar)
        return fecha >= inicio or fecha <= fin

if esta_en_rango(fecha, (12,21), (3,20)):
    estacion_norte = "Invierno"
    estacion_sur   = "Verano"
elif esta_en_rango(fecha, (3,21), (6,20)):
    estacion_norte = "Primavera"
    estacion_sur   = "Otoño"
elif esta_en_rango(fecha, (6,21), (9,20)):
    estacion_norte = "Verano"
    estacion_sur   = "Invierno"
else:  # 21 sep - 20 dic
    estacion_norte = "Otoño"
    estacion_sur   = "Primavera"

if hemisferio == "N":
    print(f"En el hemisferio norte estás en {estacion_norte}.")
elif hemisferio == "S":
    print(f"En el hemisferio sur estás en {estacion_sur}.")
else:
    print("Hemisferio inválido. Ingrese 'N' o 'S'.")
