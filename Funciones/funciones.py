import math

# ===============================================
# ACTIVIDAD 1: Función simple sin parámetros
# ===============================================

def imprimir_hola_mundo():
    """Imprime el mensaje 'Hola Mundo!'."""
    print("Hola Mundo!")

# ===============================================
# ACTIVIDAD 2: Función con parámetro y retorno
# ===============================================

def saludar_usuario(nombre):
    """
    Recibe un nombre (str) y devuelve un saludo personalizado.
    Ejemplo: 'Hola Marcos!'.
    """
    return f"Hola {nombre}!"

# ===============================================
# ACTIVIDAD 3: Función con multiples parámetros
# ===============================================

def informacion_personal(nombre, apellido, edad, residencia):
    """
    Recibe datos personales e imprime una oración con la información.
    """
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# ===============================================
# ACTIVIDAD 4: Funciones para cálculos geométricos
# ===============================================

def calcular_area_circulo(radio):
    """
    Calcula y devuelve el área de un círculo (A = pi * r^2).
    """
    # Usamos math.pi para mayor precisión
    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    """
    Calcula y devuelve el perímetro de un círculo (P = 2 * pi * r).
    """
    perimetro = 2 * math.pi * radio
    return perimetro

# ===============================================
# ACTIVIDAD 5: Conversión de segundos a horas
# ===============================================

def segundos_a_horas(segundos):
    """
    Convierte una cantidad de segundos a su equivalente en horas (H = seg / 3600).
    """
    horas = segundos / 3600
    return horas

# ===============================================
# ACTIVIDAD 6: Tabla de multiplicar (con bucle)
# ===============================================

def tabla_multiplicar(numero):
    """
    Imprime la tabla de multiplicar de un número dado, del 1 al 10.
    """
    print(f"\n--- Tabla de Multiplicar del {numero} ---")
    # Usamos un bucle for para iterar del 1 al 10
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# ===============================================
# ACTIVIDAD 7: Operaciones básicas (devuelve tupla)
# ===============================================

def operaciones_basicas(a, b):
    """
    Recibe dos números y devuelve una tupla con los resultados de suma, 
    resta, multiplicación y división.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    # Manejar la división por cero de forma simple
    if b != 0:
        division = a / b
    else:
        division = "Indefinido (División por cero)"
        
    return (suma, resta, multiplicacion, division)

# ===============================================
# ACTIVIDAD 8: Cálculo del Índice de Masa Corporal (IMC)
# ===============================================

def calcular_imc(peso, altura):
    """
    Calcula y devuelve el IMC (peso / altura^2).
    """
    imc = peso / (altura ** 2)
    return imc

# ===============================================
# ACTIVIDAD 9: Conversión de Celsius a Fahrenheit
# ===============================================

def celsius_a_fahrenheit(celsius):
    """
    Convierte la temperatura de Celsius a Fahrenheit (F = (9/5)C + 32).
    """
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

# ===============================================
# ACTIVIDAD 10: Cálculo de Promedio
# ===============================================

def calcular_promedio(a, b, c):
    """
    Calcula y devuelve el promedio de tres números.
    """
    promedio = (a + b + c) / 3
    return promedio

# ===============================================
# PROGRAMA PRINCIPAL (Llamada a las funciones)
# ===============================================

def ejecutar_practico():
    print("\n" + "="*50)
    print("EJECUCIÓN DEL PRÁCTICO 2: FUNCIONES")
    print("="*50)

    # --- Llamada 1 ---
    print("\n--- 1. Hola Mundo ---")
    imprimir_hola_mundo() # Llamada a función sin parámetros

    # --- Llamada 2 ---
    print("\n--- 2. Saludo Personalizado ---")
    nombre_usuario = input("Ingrese su nombre: ").strip()
    saludo = saludar_usuario(nombre_usuario) # Llamada con parámetro
    print(saludo)

    # --- Llamada 3 ---
    print("\n--- 3. Información Personal ---")
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    edad_str = input("Edad: ").strip()
    residencia = input("Residencia: ").strip()
    # No convertimos edad a int porque solo se usa para imprimir
    informacion_personal(nombre, apellido, edad_str, residencia)

    # --- Llamada 4 ---
    print("\n--- 4. Área y Perímetro del Círculo ---")
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        area = calcular_area_circulo(radio)
        perimetro = calcular_perimetro_circulo(radio)
        
        print(f"El área del círculo es: {area:.2f}")
        print(f"El perímetro del círculo es: {perimetro:.2f}")
    except ValueError:
        print("ERROR: Ingrese un valor numérico para el radio.")

    # --- Llamada 5 ---
    print("\n--- 5. Segundos a Horas ---")
    try:
        segundos = int(input("Ingrese la cantidad de segundos: "))
        horas = segundos_a_horas(segundos)
        print(f"{segundos} segundos equivalen a {horas:.2f} horas.")
    except ValueError:
        print("ERROR: Ingrese un valor entero para los segundos.")
        
    # --- Llamada 6 ---
    print("\n--- 6. Tabla de Multiplicar ---")
    try:
        num_tabla = int(input("Ingrese un número para ver su tabla de multiplicar: "))
        tabla_multiplicar(num_tabla) # Llamada a función con bucle interno
    except ValueError:
        print("ERROR: Ingrese un valor entero.")

    # --- Llamada 7 ---
    print("\n--- 7. Operaciones Básicas ---")
    try:
        val1 = float(input("Ingrese el primer número (a): "))
        val2 = float(input("Ingrese el segundo número (b): "))
        
        # Recibe la tupla con los resultados
        suma, resta, mult, div = operaciones_basicas(val1, val2) 
        
        print(f"Suma (a + b): {suma}")
        print(f"Resta (a - b): {resta}")
        print(f"Multiplicación (a * b): {mult}")
        print(f"División (a / b): {div}")
    except ValueError:
        print("ERROR: Ingrese valores numéricos.")

    # --- Llamada 8 ---
    print("\n--- 8. Cálculo de IMC ---")
    try:
        peso = float(input("Ingrese su peso en kg: "))
        altura = float(input("Ingrese su altura en metros: "))
        imc = calcular_imc(peso, altura)
        print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")
    except ValueError:
        print("ERROR: Ingrese valores numéricos válidos.")

    # --- Llamada 9 ---
    print("\n--- 9. Celsius a Fahrenheit ---")
    try:
        celsius = float(input("Ingrese la temperatura en °C: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"{celsius:.2f}°C equivalen a {fahrenheit:.2f}°F.")
    except ValueError:
        print("ERROR: Ingrese un valor numérico para la temperatura.")

    # --- Llamada 10 ---
    print("\n--- 10. Cálculo de Promedio ---")
    try:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        n3 = float(input("Ingrese el tercer número: "))
        
        promedio = calcular_promedio(n1, n2, n3)
        print(f"El promedio de los tres números es: {promedio:.2f}")
    except ValueError:
        print("ERROR: Ingrese valores numéricos.")
        
    print("\n" + "="*50)
    print("FIN DEL PRÁCTICO")
    print("="*50)

# El punto de entrada para ejecutar todo el práctico
if __name__ == "__main__":
    ejecutar_practico()