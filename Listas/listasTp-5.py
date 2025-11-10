# ===============================================
# PRÁCTICO 5: MANEJO DE LISTAS Y ESTRUCTURAS ANIDADAS
# ===============================================

import random

# ----------------------------------------------------
# 1) Notas de 10 estudiantes
# ----------------------------------------------------
def ejercicio_1():
    print("\n--- EJERCICIO 1: Análisis de Notas ---")
    
    # Crear una lista con las notas de 10 estudiantes (usamos números flotantes)
    notas = [7.5, 8.9, 6.0, 9.5, 7.8, 8.2, 5.5, 9.9, 7.1, 8.5]
    
    # Mostrar la lista completa.
    print("\nLista de notas:")
    i = 0
    while i < len(notas):
        print(f"Nota {i+1}: {notas[i]}")
        i += 1
    
    # Calcular y mostrar el promedio.
    suma_notas = 0
    i = 0
    while i < len(notas):
        suma_notas += notas[i]
        i += 1
    
    promedio = suma_notas / len(notas)
    print(f"\nPromedio de notas: {promedio:.2f}")
    
    # Indicar la nota más alta y la más baja (usando lógica simple sin funciones max/min)
    # Inicializamos con el primer elemento
    nota_maxima = notas[0]
    nota_minima = notas[0]
    
    i = 1
    while i < len(notas):
        if notas[i] > nota_maxima:
            nota_maxima = notas[i]
        if notas[i] < nota_minima:
            nota_minima = notas[i]
        i += 1
        
    print(f"Nota más alta: {nota_maxima}")
    print(f"Nota más baja: {nota_minima}")

# ----------------------------------------------------
# 2) Cargar 5 productos, ordenar y eliminar
# ----------------------------------------------------
def ejercicio_2():
    print("\n--- EJERCICIO 2: Gestión de Productos ---")
    
    productos = []
    
    # Pedir al usuario que cargue 5 productos en una lista.
    i = 0
    while i < 5:
        producto = input(f"Ingrese el nombre del producto #{i+1}: ").strip()
        if producto:
            productos.append(producto)
            i += 1
        else:
            print("El nombre no puede estar vacío.")

    # Mostrar la lista ordenada alfabéticamente (usando sorted())
    # sorted() devuelve una nueva lista ordenada, no modifica la original
    productos_ordenados = sorted(productos)
    print("\nLista de productos ordenada alfabéticamente:")
    i = 0
    while i < len(productos_ordenados):
        print(f"- {productos_ordenados[i]}")
        i += 1

    # Preguntar qué producto desea eliminar y actualizar la lista.
    producto_a_eliminar = input("\nIngrese el nombre del producto que desea eliminar: ").strip()
    
    try:
        # Se usa la lista original para la eliminación
        productos.remove(producto_a_eliminar)
        print(f"'{producto_a_eliminar}' ha sido eliminado.")
    except ValueError:
        print(f"ERROR: El producto '{producto_a_eliminar}' no se encontró en la lista.")
        
    print("\nLista final actualizada:")
    i = 0
    while i < len(productos):
        print(f"- {productos[i]}")
        i += 1

# ----------------------------------------------------
# 3) Pares e impares de 15 números al azar
# ----------------------------------------------------
def ejercicio_3():
    print("\n--- EJERCICIO 3: Clasificación de Pares e Impares ---")
    
    # Generar una lista con 15 números enteros al azar entre 1 y 100.
    numeros_originales = []
    i = 0
    while i < 15:
        numeros_originales.append(random.randint(1, 100))
        i += 1
        
    print("Lista original generada:")
    print(numeros_originales)
    
    pares = []
    impares = []
    
    # Crear una lista con los pares y otra con los impares.
    i = 0
    while i < len(numeros_originales):
        numero = numeros_originales[i]
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
        i += 1
        
    # Mostrar cuántos números tiene cada lista.
    print(f"\nNúmeros Pares ({len(pares)}):")
    i = 0
    while i < len(pares):
        print(pares[i], end=", " if i < len(pares) - 1 else "")
        i += 1
        
    print(f"\n\nNúmeros Impares ({len(impares)}):")
    i = 0
    while i < len(impares):
        print(impares[i], end=", " if i < len(impares) - 1 else "")
        i += 1
    print("\n")


# ----------------------------------------------------
# 4) Crear una nueva lista sin elementos repetidos
# ----------------------------------------------------
def ejercicio_4():
    print("\n--- EJERCICIO 4: Eliminar Duplicados ---")
    
    # Lista con valores repetidos
    lista_repetida = [10, "rojo", 5, "azul", 10, "rojo", 99, 5, "verde", 99]
    print(f"Lista original: {lista_repetida}")
    
    lista_sin_duplicados = []
    
    # Crear una nueva lista sin elementos repetidos.
    i = 0
    while i < len(lista_repetida):
        elemento = lista_repetida[i]
        
        # Verificar si el elemento ya está en la nueva lista
        j = 0
        ya_existe = False
        while j < len(lista_sin_duplicados):
            if lista_sin_duplicados[j] == elemento:
                ya_existe = True
                break
            j += 1
            
        if not ya_existe:
            lista_sin_duplicados.append(elemento)
            
        i += 1

    # Mostrar el resultado.
    print("\nLista sin elementos repetidos:")
    i = 0
    while i < len(lista_sin_duplicados):
        print(lista_sin_duplicados[i], end=", " if i < len(lista_sin_duplicados) - 1 else "")
        i += 1
    print("\n")
    
# ----------------------------------------------------
# 5) Gestión de lista de estudiantes (agregar/eliminar)
# ----------------------------------------------------
def ejercicio_5():
    print("\n--- EJERCICIO 5: Lista de Estudiantes ---")
    
    estudiantes = ["Ana", "Beto", "Carla", "David", "Erica", "Fran", "Gabi", "Hugo"]
    
    print("Lista inicial de estudiantes:")
    print(estudiantes)
    
    opcion = input("\n¿Quiere [A]gregar o [E]liminar un estudiante? (A/E): ").strip().lower()
    
    if opcion == 'a':
        nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ").strip()
        if nuevo_estudiante:
            estudiantes.append(nuevo_estudiante)
            print(f"'{nuevo_estudiante}' agregado.")
        else:
            print("Operación cancelada.")
            
    elif opcion == 'e':
        estudiante_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ").strip()
        try:
            estudiantes.remove(estudiante_a_eliminar)
            print(f"'{estudiante_a_eliminar}' ha sido eliminado.")
        except ValueError:
            print(f"ERROR: '{estudiante_a_eliminar}' no se encontró en la lista.")
            
    else:
        print("Opción no válida. No se realizaron cambios.")
        
    # Mostrar la lista final actualizada.
    print("\nLista final actualizada:")
    i = 0
    while i < len(estudiantes):
        print(f"- {estudiantes[i]}")
        i += 1

# ----------------------------------------------------
# 6) Rotar lista una posición a la derecha
# ----------------------------------------------------
def ejercicio_6():
    print("\n--- EJERCICIO 6: Rotación de Lista ---")
    
    numeros = [10, 20, 30, 40, 50, 60, 70]
    print(f"Lista original: {numeros}")
    
    # Rotar todos los elementos una posición hacia la derecha
    # 1. Usar slicing para obtener el último elemento
    ultimo_elemento = numeros[-1]
    
    # 2. Usar slicing para obtener todos los elementos excepto el último
    resto_lista = numeros[:-1]
    
    # 3. Concatenar: el último elemento + el resto de la lista
    numeros_rotados = [ultimo_elemento] + resto_lista
    
    print(f"Lista rotada a la derecha:")
    i = 0
    while i < len(numeros_rotados):
        print(numeros_rotados[i], end=", " if i < len(numeros_rotados) - 1 else "")
        i += 1
    print("\n")

# ----------------------------------------------------
# 7) Matriz 7x2: Temperaturas (Min/Max)
# ----------------------------------------------------
def ejercicio_7():
    print("\n--- EJERCICIO 7: Análisis de Temperaturas (Matriz 7x2) ---")
    
    # Matriz [ [Min, Max], [Min, Max], ... ] para 7 días
    temperaturas = [
        [15, 25],  # Lunes
        [17, 28],  # Martes
        [14, 26],  # Miércoles
        [16, 25],  # Jueves
        [18, 30],  # Viernes
        [19, 32],  # Sábado
        [17, 30]   # Domingo
    ]
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # Calcular el promedio de las mínimas y el de las máximas.
    suma_min = 0
    suma_max = 0
    i = 0
    while i < len(temperaturas):
        suma_min += temperaturas[i][0] # La mínima está en el índice 0
        suma_max += temperaturas[i][1] # La máxima está en el índice 1
        i += 1
        
    promedio_min = suma_min / len(temperaturas)
    promedio_max = suma_max / len(temperaturas)
    
    print(f"Promedio de Temperaturas Mínimas: {promedio_min:.2f}°C")
    print(f"Promedio de Temperaturas Máximas: {promedio_max:.2f}°C")
    
    # Mostrar en qué día se registró la mayor amplitud térmica.
    max_amplitud = -1 # Se inicializa con un valor imposiblemente bajo
    dia_mayor_amplitud = ""
    
    i = 0
    while i < len(temperaturas):
        minima = temperaturas[i][0]
        maxima = temperaturas[i][1]
        amplitud = maxima - minima
        
        if amplitud > max_amplitud:
            max_amplitud = amplitud
            dia_mayor_amplitud = dias[i]
        i += 1
        
    print(f"\nMayor amplitud térmica ({max_amplitud}°C) registrada el: {dia_mayor_amplitud}")

# ----------------------------------------------------
# 8) Matriz de Notas 5x3 (Estudiantes x Materias)
# ----------------------------------------------------
def ejercicio_8():
    print("\n--- EJERCICIO 8: Análisis de Notas por Estudiante y Materia ---")
    
    # Matriz [ [M1, M2, M3], [M1, M2, M3], ... ] para 5 estudiantes
    notas = [
        [8.0, 7.5, 9.0], # Estudiante 1
        [6.5, 8.0, 7.0], # Estudiante 2
        [9.0, 9.5, 8.5], # Estudiante 3
        [7.0, 6.5, 7.5], # Estudiante 4
        [5.0, 6.0, 5.5]  # Estudiante 5
    ]
    
    num_estudiantes = len(notas)
    num_materias = len(notas[0]) # Asumiendo que todas las filas tienen 3 columnas

    # 1. Mostrar el promedio de cada estudiante.
    print("\n--- PROMEDIO POR ESTUDIANTE ---")
    i = 0
    while i < num_estudiantes:
        suma_estudiante = 0
        j = 0
        # Sumar las 3 notas del estudiante 'i'
        while j < num_materias:
            suma_estudiante += notas[i][j]
            j += 1
        
        promedio_estudiante = suma_estudiante / num_materias
        print(f"Estudiante {i+1}: {promedio_estudiante:.2f}")
        i += 1

    # 2. Mostrar el promedio de cada materia.
    print("\n--- PROMEDIO POR MATERIA ---")
    j = 0
    while j < num_materias:
        suma_materia = 0
        i = 0
        # Sumar la nota de la materia 'j' para los 5 estudiantes
        while i < num_estudiantes:
            suma_materia += notas[i][j]
            i += 1
        
        promedio_materia = suma_materia / num_estudiantes
        print(f"Materia {j+1}: {promedio_materia:.2f}")
        j += 1

# ----------------------------------------------------
# 9) Tablero de Ta-Te-Ti (Tic-Tac-Toe)
# ----------------------------------------------------
def mostrar_tablero(tablero):
    print("\n--- TABLERO ---")
    i = 0
    while i < len(tablero):
        # Unir los elementos de la fila con un pipe "|"
        print(" | ".join(tablero[i]))
        # Imprimir separador entre filas
        if i < len(tablero) - 1:
            print("-" * 9) 
        i += 1
    print("---------------")

def ejercicio_9():
    print("\n--- EJERCICIO 9: Juego de Ta-Te-Ti ---")
    
    # Inicializar tablero 3x3 con guiones "-"
    tablero = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]
    
    jugador = "X"
    jugadas_restantes = 9
    
    mostrar_tablero(tablero)

    while jugadas_restantes > 0:
        print(f"Turno del jugador: {jugador}")
        
        try:
            fila = int(input("Ingrese Fila (0, 1, o 2): "))
            columna = int(input("Ingrese Columna (0, 1, o 2): "))
        except ValueError:
            print("ERROR: Ingrese solo números enteros para la fila y columna.")
            continue
            
        # Validaciones de rango
        if not (0 <= fila <= 2 and 0 <= columna <= 2):
            print("ERROR: Fila o columna fuera del rango (0-2).")
            continue
        
        # Validación de casilla vacía
        if tablero[fila][columna] == "-":
            tablero[fila][columna] = jugador
            jugadas_restantes -= 1
            mostrar_tablero(tablero)
            
            # Cambiar de jugador
            if jugador == "X":
                jugador = "O"
            else:
                jugador = "X"
        else:
            print("ERROR: Esa casilla ya está ocupada. Intente de nuevo.")

    if jugadas_restantes == 0:
        print("\nJuego terminado. ¡Es un empate!")

# ----------------------------------------------------
# 10) Matriz 4x7: Ventas por Producto y Día
# ----------------------------------------------------
def ejercicio_10():
    print("\n--- EJERCICIO 10: Análisis de Ventas (Matriz 4x7) ---")
    
    # Matriz [ Producto1...4 ] x [ Día1...7 ]
    # Filas (4): Productos | Columnas (7): Días
    ventas = [
        [10, 15, 8, 20, 12, 5, 18],  # Producto 1
        [22, 10, 15, 12, 18, 25, 10], # Producto 2
        [5, 8, 12, 10, 7, 6, 9],    # Producto 3
        [30, 25, 15, 20, 10, 12, 15] # Producto 4
    ]
    
    num_productos = len(ventas)
    num_dias = len(ventas[0])
    
    # 1. Mostrar el total vendido por cada producto.
    print("\n--- TOTAL VENDIDO POR PRODUCTO ---")
    totales_producto = []
    i = 0
    while i < num_productos:
        suma_producto = 0
        j = 0
        while j < num_dias:
            suma_producto += ventas[i][j]
            j += 1
        
        totales_producto.append(suma_producto)
        print(f"Producto {i+1}: {suma_producto}")
        i += 1

    # 2. Mostrar el día con mayores ventas totales.
    print("\n--- DÍA CON MAYORES VENTAS ---")
    totales_dia = []
    j = 0
    while j < num_dias:
        suma_dia = 0
        i = 0
        # Sumar las ventas de todos los productos en el día 'j'
        while i < num_productos:
            suma_dia += ventas[i][j]
            i += 1
        totales_dia.append(suma_dia)
        j += 1
        
    # Encontrar el día con mayor venta (similar a Ej. 7)
    max_venta_dia = totales_dia[0]
    dia_mayor_venta = 1
    j = 1
    while j < len(totales_dia):
        if totales_dia[j] > max_venta_dia:
            max_venta_dia = totales_dia[j]
            dia_mayor_venta = j + 1
        j += 1
        
    print(f"Día con mayores ventas totales: Día {dia_mayor_venta} ({max_venta_dia} unidades)")

    # 3. Indicar cuál fue el producto más vendido en la semana.
    print("\n--- PRODUCTO MÁS VENDIDO EN LA SEMANA ---")
    # Los totales_producto ya fueron calculados en el punto 1
    
    max_venta_producto = totales_producto[0]
    producto_mas_vendido = 1
    i = 1
    while i < len(totales_producto):
        if totales_producto[i] > max_venta_producto:
            max_venta_producto = totales_producto[i]
            producto_mas_vendido = i + 1
        i += 1
        
    print(f"El producto más vendido fue el Producto {producto_mas_vendido} ({max_venta_producto} unidades)")


# ----------------------------------------------------
# MENÚ DE EJECUCIÓN DEL PRÁCTICO
# ----------------------------------------------------
def menu_practico_5():
    while True:
        print("\n" + "="*50)
        print("          PRÁCTICO 5: MANEJO DE LISTAS")
        print("="*50)
        print("1. Análisis de Notas (10 estudiantes)")
        print("2. Gestión de Productos (Cargar, Ordenar, Eliminar)")
        print("3. Pares e Impares (15 números al azar)")
        print("4. Eliminar Duplicados")
        print("5. Gestión de Estudiantes (Agregar/Eliminar)")
        print("6. Rotación de Lista (Derecha)")
        print("7. Matriz de Temperaturas (Promedio y Amplitud)")
        print("8. Matriz de Notas (Promedio por Estudiante y Materia)")
        print("9. Juego de Ta-Te-Ti (Tablero 3x3)")
        print("10. Matriz de Ventas (Producto y Día)")
        print("11. Salir")
        print("-" * 50)
        
        opcion_str = input("Seleccione un ejercicio (1-11): ").strip()
        
        if not opcion_str.isdigit():
            print("ERROR: Ingrese un número válido.")
            continue
            
        opcion = int(opcion_str)

        if opcion == 1: ejercicio_1()
        elif opcion == 2: ejercicio_2()
        elif opcion == 3: ejercicio_3()
        elif opcion == 4: ejercicio_4()
        elif opcion == 5: ejercicio_5()
        elif opcion == 6: ejercicio_6()
        elif opcion == 7: ejercicio_7()
        elif opcion == 8: ejercicio_8()
        elif opcion == 9: ejercicio_9()
        elif opcion == 10: ejercicio_10()
        elif opcion == 11:
            print("\nFinalizando el Práctico 5. ¡Buen trabajo!")
            break
        else:
            print("Opción fuera de rango. Intente de nuevo.")

if __name__ == "__main__":
    menu_practico_5()