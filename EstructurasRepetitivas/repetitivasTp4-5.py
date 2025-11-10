# EJERCICIO 5: Juego de adivinanza
print("\n--- EJERCICIO 5: Juego de Adivinanza ---")

# Importar la librería necesaria
import random

# Generar el número secreto entre 0 y 9
numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False

print("¡Adivina el número secreto (entre 0 y 9)!")

while not adivinado:
    intentos += 1
    
    try:
        suposicion = int(input(f"Intento #{intentos}: Ingresa tu suposición: "))
        
        if 0 <= suposicion <= 9:
            if suposicion == numero_secreto:
                adivinado = True
                print(f"🎉 ¡Felicidades! Adivinaste el número {numero_secreto}.")
                print(f"Te tomó {intentos} intentos.")
            elif suposicion < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            else:
                print("Demasiado alto. Intenta de nuevo.")
        else:
            print("Número fuera del rango (0-9).")
            
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")