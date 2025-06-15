# 🧪 Quiz Día 6
# 🧠 Tema: Constantes, Cadenas, Caracteres Especiales, Formateo y Repaso General
#  📅 Fecha: 2025-06-14
# Qué se practica: Constantes, inmutabilidad, caracteres especiales, concatenación, f-strings, format(), slicing y reglas de variables

# --- EJERCICIO 1 ---
# Declara una constante llamada PI con valor 3.14159, según las convenciones de Python.
PI = 3.14159

# --- EJERCICIO 2 ---
# Explica con código por qué no se puede modificar directamente una cadena en Python.
cadena = "HolaMundo"
# cadena[0] = 'h'  # Esto daría error: TypeError: 'str' object does not support item assignment
# Las cadenas son inmutables; para "cambiar" una, se debe crear una nueva:
cadena = "holamundo"

# --- EJERCICIO 3 ---
# Declara una cadena con un mensaje que contenga: salto de línea, tabulación y comillas dobles.
mensaje = "\tHola \"mundo\"\nNuevo día"

# --- EJERCICIO 4 ---
# Une tres cadenas distintas con el método `.join()` y muestra el resultado. Usa guiones como separador.
a = "Hola"
b = "mundo"
c = "disciplinado"
parrafo = "-".join([a, b, c])
print(parrafo)

# --- EJERCICIO 5 ---
# Usa `f-string` para imprimir: "Mi nombre es Daniel y tengo 28 años."
nombre = 'Daniel'
edad = 28
print(f'Mi nombre es {nombre} y tengo {edad} años.')

# --- EJERCICIO 6 ---
# Usa el método `.format()` para construir la misma frase: "Mi nombre es Daniel y tengo 28 años."
print("Mi nombre es {} y tengo {} años.".format(nombre, edad))

# --- EJERCICIO 7 ---
# Extrae la palabra "disciplinado" de la cadena usando slicing: "Soy un aprendiz disciplinado"
frase = 'Soy un aprendiz disciplinado'
palabra = frase[16:29]

# --- EJERCICIO 8 ---
# ¿Cuál de las siguientes variables es válida según las reglas de nombramiento en Python?
# a) 1variable ❌
# b) mi-variable ❌
# c) _variable ✅
# d) clase ✅ (aunque no se recomienda porque es palabra reservada)
respuesta = "c y d"

# --- EJERCICIO 9 ---
# ¿Cuál es la diferencia entre usar el operador `+` para concatenar y el método `.join()`?
# '+' concatena strings directamente. `.join()` es más eficiente con múltiples cadenas (como listas) y más limpio en bucles.

# --- EJERCICIO 10 ---
# Explica con tus palabras qué es una constante y cómo se representa en Python.
# Una constante en Python es una variable que por convención no debe modificarse, y se escribe en MAYÚSCULAS.
# Ejemplo: MAX_TAMANO = 100
