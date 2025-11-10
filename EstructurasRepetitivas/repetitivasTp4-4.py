# EJERCICIO 4: Sumador secuencial hasta ingresar 0
print("\n--- EJERCICIO 4: Sumador hasta 0 ---")

total_acumulado = 0
print("Ingrese números enteros para sumar (ingrese 0 para finalizar):")

while True:
    try:
        entrada_str = input("Número a sumar: ").strip()
        numero = int(entrada_str)
        
        if numero == 0:
            break  # Detiene el bucle al ingresar 0
            
        total_acumulado += numero
        
    except ValueError:
        # Manejo simple de entrada no numérica
        print("Entrada no válida. Por favor, ingrese un número entero.")
        
print(f"El total acumulado es: {total_acumulado}")