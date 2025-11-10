# EJERCICIO 8: Clasificador de N números
print("\n--- EJERCICIO 8: Clasificador de N Números ---")

CANTIDAD_A_PROCESAR = 100  # Cambiar este valor para la prueba (ej. 10)
print(f"Se solicitarán {CANTIDAD_A_PROCESAR} números enteros.")

conteo_pares = 0
conteo_impares = 0
conteo_positivos = 0
conteo_negativos = 0

i = 1
while i <= CANTIDAD_A_PROCESAR:
    try:
        numero = int(input(f"Ingrese el número {i}: "))
    except ValueError:
        print("Entrada no válida. Reintente.")
        continue # Vuelve al inicio del bucle sin incrementar i
    
    # Clasificación Par/Impar (Módulo %)
    if numero % 2 == 0:
        conteo_pares += 1
    else:
        conteo_impares += 1
        
    # Clasificación Positivo/Negativo (Excluyendo el 0)
    if numero > 0:
        conteo_positivos += 1
    elif numero < 0:
        conteo_negativos += 1
    
    i += 1 # Solo avanzamos el contador si la entrada fue válida

print("\n--- RESULTADOS ---")
print(f"Total de números procesados: {CANTIDAD_A_PROCESAR}")
print(f"Números Pares: {conteo_pares}")
print(f"Números Impares: {conteo_impares}")
print(f"Números Positivos (sin contar 0): {conteo_positivos}")
print(f"Números Negativos: {conteo_negativos}")