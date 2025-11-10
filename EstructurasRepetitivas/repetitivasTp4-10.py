# EJERCICIO 10: Invertir el orden de los dígitos
print("\n--- EJERCICIO 10: Invertir Dígitos ---")

try:
    numero_original = int(input("Ingrese un número entero para invertir: "))
except ValueError:
    print("Error: Ingrese un número entero válido.")
else:
    numero = abs(numero_original) # Trabajar con el valor absoluto
    numero_invertido = 0
    
    # Usamos la lógica de división y módulo
    while numero > 0:
        # 1. Obtener el último dígito (usando el módulo 10)
        digito = numero % 10
        
        # 2. Agregar el dígito al número invertido (multiplicando por 10 y sumando)
        numero_invertido = (numero_invertido * 10) + digito
        
        # 3. Eliminar el último dígito del número original (división entera)
        numero = numero // 10
        
    # Restaurar el signo original si el número era negativo
    if numero_original < 0:
        numero_invertido = -numero_invertido
        
    print(f"El número invertido es: {numero_invertido}")