# EJERCICIO 9: Media de N números
print("\n--- EJERCICIO 9: Calculadora de Media ---")

CANTIDAD_A_PROCESAR_MEDIA = 100 # Cambiar este valor para la prueba (ej. 5)
print(f"Se solicitarán {CANTIDAD_A_PROCESAR_MEDIA} números enteros para calcular la media.")

suma_total_media = 0
contador_valido = 0 # Contar solo las entradas que son números

i = 1
while i <= CANTIDAD_A_PROCESAR_MEDIA:
    try:
        numero = int(input(f"Ingrese el número {i}: "))
        suma_total_media += numero
        contador_valido += 1
        i += 1 # Avanzamos el bucle
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

if contador_valido > 0:
    media = suma_total_media / contador_valido
    print(f"\nLa media (promedio) de los {contador_valido} números ingresados es: {media:.2f}")
else:
    print("No se ingresaron números válidos para calcular la media.")