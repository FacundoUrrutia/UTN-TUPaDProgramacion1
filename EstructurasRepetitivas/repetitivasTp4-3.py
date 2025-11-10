# EJERCICIO 3: Suma de números entre dos valores
print("\n--- EJERCICIO 3: Suma entre dos valores ---")

try:
    valor1 = int(input("Ingrese el primer valor entero: "))
    valor2 = int(input("Ingrese el segundo valor entero: "))
except ValueError:
    print("Error: Ingrese solo números enteros.")
else:
    # Determinar el rango correcto, asegurando que el inicio sea menor que el final
    inicio = min(valor1, valor2)
    fin = max(valor1, valor2)
    
    suma = 0
    # La función range() excluye el límite superior, así que sumamos 1 al inicio
    # y no hacemos nada con el fin, ya que debe ser excluyente.
    for numero in range(inicio + 1, fin):
        suma += numero
        
    print(f"La suma de los números entre {inicio} y {fin} (excluidos) es: {suma}")