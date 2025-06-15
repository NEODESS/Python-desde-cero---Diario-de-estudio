# 📅 Fecha: 2025-06-10
# 🧠 Tema: Métodos de cadenas, formato de texto, entrada de datos, proyecto generador de ID


# ─────────────────────────────────────────────────────────────────────────────
# 1. Convertir texto a minúsculas
texto_1 = "CIUDAD GÓTICA"
texto_minuscula = texto_1.lower()
print(texto_minuscula)  # ciudad gótica

# ─────────────────────────────────────────────────────────────────────────────
# 2. Interpolación para mensaje de bienvenida
nombre = "Bruce"
apellido = "Wayne"
ciudad = "Ciudad Gótica"
mensaje = f'Hola, {nombre} {apellido}. Bienvenido a {ciudad}.'
print(mensaje)  # Hola, Bruce Wayne. Bienvenido a Ciudad Gótica.

# ─────────────────────────────────────────────────────────────────────────────
# 3. Solicitar números y sumarlos correctamente
numero_1 = int(input('Proporciona el primer número: '))
numero_2 = int(input('Proporciona el segundo número: '))
resultado = numero_1 + numero_2
print(f'El resultado de la suma es: {resultado}')

# ─────────────────────────────────────────────────────────────────────────────
# 4. Extraer las tres primeras letras del nombre ingresado
nombre = input('¿Cuál es tu nombre?: ')
letras_3 = nombre[0:3]
print(f'Las 3 primeras letras de tu nombre son: {letras_3}')

# ─────────────────────────────────────────────────────────────────────────────
# 5. Generador de ID único con entradas del usuario
from random import randint

nombre = input('¿Cuál es tu nombre?: ')
apellido = input('¿Cuál es tu apellido?: ')
anio = input('¿Cuál es tu año de nacimiento?: ')

# Generar número aleatorio de 4 cifras siempre con ceros a la izquierda si es necesario
aleatorio = randint(0, 9999)
aleatorio_formateado = f'{aleatorio:04}'

# Tomar los dos primeros caracteres del nombre y del apellido
letras_id = nombre[0:2]
letras_id2 = apellido[0:2]

# Formar el ID único con interpolación y convertir a mayúsculas
formato_id = f'{letras_id}{letras_id2}{anio}-{aleatorio_formateado}'
id_entregado = formato_id.upper()

print(f'Su ID único es: {id_entregado}')
