# EJERCICIO 2: Cantidad de dígitos de un número
print("\n--- EJERCICIO 2: Cantidad de dígitos ---")

# Solicitar la entrada como string para manejar cualquier carácter
numero_str = input("Ingrese un número entero: ").strip()

# Eliminar el signo si existe para contar solo dígitos
if numero_str.startswith('-') or numero_str.startswith('+'):
    numero_str = numero_str[1:]

# Usar len() para obtener la cantidad de dígitos
cantidad_digitos = len(numero_str)

print(f"El número ingresado tiene {cantidad_digitos} dígitos.")