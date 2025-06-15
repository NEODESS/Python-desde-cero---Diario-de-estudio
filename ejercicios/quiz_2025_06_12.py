# 📘 Quiz Día 4 — Nivel Intermedio
# 📅 Fecha: 2025-06-13
# 🧠 Qué se evalúa: operadores aritméticos, asignación compuesta, slicing, casing, input, interpolación, buenas prácticas.

# --- EJERCICIO 1 ---
# ¿Cuál es el valor final de A después de ejecutar este bloque de código?
a = 12
b = 4
a //= b  # División entera compuesta: a = a // b → 12 // 4 = 3
print(a)  # ✅ Resultado: 3

# --- EJERCICIO 2 ---
# ¿Qué imprime este código y por qué?
mensaje = "Python es divertido"
print(mensaje[3:10])  # ✅ Resultado: 'hon es ' (del índice 3 hasta el 9)

# --- EJERCICIO 3 ---
# ¿Cómo escribirías esta línea usando interpolación?
x = 12
y = 9
print(f'El resultado es {x * y}')  # ✅ Resultado: El resultado es 108

# --- EJERCICIO 4 ---
# ¿Qué resultado imprime este código si el usuario ingresa Pedro y Ramírez?
nombre = "Pedro"
apellido = "Ramírez"
usuario = f'{nombre}.{apellido}@gotham.com'.lower()
print(usuario)  # ✅ Resultado: pedro.ramírez@gotham.com

# --- EJERCICIO 5 ---
# ¿Cuál opción NO es una buena práctica para nombrar variables?
# ❌ PascalCase no es buena práctica en Python para variables:
VariableInvalida = 10  # 🚫

# --- EJERCICIO 6 ---
# ¿Qué resultado imprime esta línea?
frase = "programar es un arte"
print(frase[-4:])  # ✅ Resultado: arte

# --- EJERCICIO 7 ---
# Corrige este código para que funcione correctamente:
nombre = "Lucía"
nombre_mayus = nombre.upper()
print(f'Hola {nombre_mayus}, bienvenida')  # ✅ Resultado correcto
