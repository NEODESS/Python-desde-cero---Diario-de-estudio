# 📘 Quiz Día 3 — Variables, cadenas, slicing, input, proyecto de email
# 📅 Fecha: 2025-06-11
# 🧠 Qué se evalúa: variables, cadenas, slicing, input(), concatenación, casing

# --- EJERCICIO 1 ---
# Declara tu nombre y edad, y muestra:
# "Hola, mi nombre es Daniel y tengo 28 años."
nombre = "Daniel"
edad = 28
print(f"Hola, mi nombre es {nombre} y tengo {edad} años")  # ✅ Correcto

# --- EJERCICIO 2 ---
# Corrige variables inválidas:
# 1nombre = "Daniel"
# Solución:
nombre1 = "Daniel"  # ✅ Válido

# --- EJERCICIO 3 ---
# Extraer "aprendiz" de la frase:
frase = "Soy un aprendiz disciplinado"
sub = frase[7:15]
print(sub)  # ✅ Imprime "aprendiz"

# --- EJERCICIO 4 ---
# Cambiar "programar es mágico" por "programar es poderoso"
frase2 = "programar es mágico"
nueva = frase2[:13] + "poderoso"
print(nueva)  # ✅ "programar es poderoso"

# --- EJERCICIO 5 ---
# Generar email estilo Ciudad Gótica (desde la rutina vista en clase)
print("*** Bienvenido al sistema de generación de emails de Ciudad Gótica ***")
nombre = "Bruce"
apellido = "Wayne"
correo = "@ciudadgotica.com"
username = f"{nombre}.{apellido}{correo}".lower()
print(f'''
Tu nuevo email generado por el sistema es:
    [{username}]
    *** Felicidades ***
''')  # ✅ Código completo con concatenación, casing e interpolación
