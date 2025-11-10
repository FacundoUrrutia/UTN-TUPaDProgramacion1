# EJERCICIO 6: Pares de 0 a 100 (decreciente)
print("\n--- EJERCICIO 6: Números Pares Decrecientes ---")

# range(99, -1, -2) genera números desde 99 (el par más alto es 98)
# Ajustamos para empezar en el par más alto (100) y terminar en 0, con paso -2
# Si 100 es par, el primer par menor es 100.
# Si el inicio es 100, el fin debe ser -1 para incluir el 0 (ya que range excluye el fin)
for numero in range(100, -1, -2):
    print(numero)