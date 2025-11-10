# EJERCICIO 7: Suma de 0 hasta N
print("\n--- EJERCICIO 7: Suma de 0 a N ---")

while True:
    try:
        limite = int(input("Ingrese un número entero positivo (N): "))
        if limite < 0:
            print("N debe ser un número positivo.")
            continue
        break
    except ValueError:
        print("Entrada no válida. Ingrese un número entero.")

suma_total = 0
# El bucle va desde 0 hasta el límite (el +1 en range lo incluye)
for numero in range(limite + 1):
    suma_total += numero
    
print(f"La suma de todos los números entre 0 y {limite} es: {suma_total}")