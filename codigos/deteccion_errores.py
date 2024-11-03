import random

# Función para calcular el bit de paridad (paridad par)
def calcular_paridad(bits):
    # La paridad es 1 si hay un número impar de bits en 1, de lo contrario es 0
    return sum(bits) % 2

# Función para crear un mensaje con paridad
def crear_mensaje_con_paridad(mensaje):
    # Calculamos el bit de paridad para el mensaje
    paridad = calcular_paridad(mensaje)
    # Agregamos el bit de paridad al final del mensaje
    mensaje_con_paridad = mensaje + [paridad]
    return mensaje_con_paridad

# Función para verificar si el mensaje recibido tiene errores
def verificar_mensaje(mensaje_con_paridad):
    # Separar el mensaje de datos del bit de paridad
    datos, paridad = mensaje_con_paridad[:-1], mensaje_con_paridad[-1]
    # Calcular la paridad de los datos
    paridad_calculada = calcular_paridad(datos)
    # Comparar la paridad calculada con la paridad recibida
    return paridad_calculada == paridad

# Función para simular un error aleatorio en el mensaje
def introducir_error(mensaje):
    # Elegimos una posición aleatoria en el mensaje
    posicion = random.randint(0, len(mensaje) - 1)
    # Cambiamos el bit en esa posición
    mensaje[posicion] = 1 - mensaje[posicion]  # 0 -> 1 o 1 -> 0
    return mensaje

# Mensaje original (en binario)
mensaje_original = [1, 0, 1, 1, 0]  # Ejemplo de datos binarios

# Crear mensaje con paridad
mensaje_con_paridad = crear_mensaje_con_paridad(mensaje_original)
print("Mensaje original con paridad:", mensaje_con_paridad)

# Simulamos la recepción del mensaje sin errores
print("Verificación sin errores:", verificar_mensaje(mensaje_con_paridad))

# Simulamos la transmisión con un error introducido
mensaje_con_error = introducir_error(mensaje_con_paridad[:])  # Copia para no modificar el original
print("Mensaje con error:", mensaje_con_error)
print("Verificación con error:", verificar_mensaje(mensaje_con_error))

