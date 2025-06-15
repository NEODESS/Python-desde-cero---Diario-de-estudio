# 🧪 Quiz Día 5 — Operadores de asignación y aritméticos
# 📅 Fecha: 2025-06-13
# 🧠 Tema: =, +=, -=, *=, /=, //=, %=, **=

# Ejercicio 1:
a = 10
b = 3
a += b  # a = 10 + 3
print(a)  # ✅ Resultado: 13

# Ejercicio 2:
a = 10
a *= b  # a = 10 * 3
print(a)  # ✅ Resultado: 30

# Ejercicio 3:
a %= b  # a = 30 % 3
print(a)  # ✅ Resultado: 0

# Ejercicio 4:
a = 4
b = 2
a **= b  # a = 4 ** 2
print(a)  # ✅ Resultado: 16

# Ejercicio 5:
x = 10
x /= 3  # x = 10 / 3
print(x, type(x))  # ✅ Resultado: ~3.333... <class 'float'>

# Ejercicio 6 (Bonus sobre slicing):
frase = "programar es un arte"
print(frase[-4:])  # ✅ Resultado: arte

# Ejercicio 7 (Bonus sobre interpolación):
nombre = "María"
apellido = "Gómez"
usuario = f"{nombre}.{apellido}@gotham.com".lower()
print(usuario)  # ✅ Resultado: maria.gómez@gotham.com
