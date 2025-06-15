# Tema: Ejercicios integrados sobre variables, cadenas y slicing
# Fecha: 2025-06-09
# Qué se practica: Aplicación de conceptos básicos de Python: print, variables, cadenas, reglas de nombres y slicing.
# Qué aprendiste: Aprendí a declarar variables, a usar print con concatenación, a identificar errores de sintaxis, y a manipular cadenas con slicing.
# Qué te costó más: Diferenciar cuándo usar slicing y cómo concatenar correctamente con print.

# --- EJERCICIO 1 ---
# Enunciado:
# Declara una variable con tu nombre y otra con tu edad. Usa print para mostrar el mensaje:
# "Hola, mi nombre es Daniel y tengo 28 años."

# respuesta:
nombre = 'Daniel'
edad = 28
# print('Hola, mi nombre es' nombre ' y tengo' edad ' años.') por falta de concatenación ❌ Esto genera error.

# Corrección:
print('Hola, mi nombre es', nombre, 'y tengo', edad, 'años.')  # ✅ usando comas
# o
print(f'Hola, mi nombre es {nombre} y tengo {edad} años.')     # ✅ usando f-string


# --- EJERCICIO 2 ---
# Enunciado:
# Corrige los errores de nombramiento en las siguientes variables inválidas.

# observación:
# 1nombre = 'Daniel'  ❌ Error: no se puede iniciar con número.

# respuesta correcta:
nombre = 'Daniel'
# o
nombre1 = 'Daniel'
# o
nombre_1 = 'Daniel'


# --- EJERCICIO 3 ---
# Enunciado:
# Dada la cadena frase = "Soy un aprendiz disciplinado", extrae la palabra "aprendiz" usando slicing.

frase = "Soy un aprendiz disciplinado"

# respuesta:
subcadena_aprendiz = frase[7:15]
print(subcadena_aprendiz)  # ✅ Correcto

# Comentario:
# Recuerda que slicing va desde el índice de inicio hasta el índice final SIN incluirlo.


# --- EJERCICIO 4 ---
# Enunciado:
# Usa slicing y concatenación para transformar "programar es mágico" en "programar es poderoso"

frase = "programar es mágico"

# respuesta:
subcadena_programar = frase[0:13]
reemplazo = 'poderoso'
print(subcadena_programar, reemplazo)  # ✅ Lógica funcional

# respuesta más precisa:
nueva_frase = frase[:13] + 'poderoso'
print(nueva_frase)  # ✅ Resultado: programar es poderoso


# --- EJERCICIO 5 ---
# Enunciado:
# Explica en voz alta (como hiciste hoy) qué aprendiste en este estudio.

# Resumen textual (de lo que dijiste y escribiste):
"""
Hoy aprendí los conceptos base de Python: cómo imprimir mensajes, declarar variables, y trabajar con strings. 
También entendí la importancia de las reglas de nombramiento y practiqué cómo extraer subcadenas.
Me costó un poco entender la sintaxis de slicing y concatenar bien con print, pero lo fui corrigiendo con la práctica.
"""

