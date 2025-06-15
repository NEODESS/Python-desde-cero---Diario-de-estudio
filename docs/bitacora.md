🗓️ Bitácora de estudio – Día 1
📅 Fecha: 2025-06-09
📁 Archivos trabajados:

01-hola-mundo.py

02-variables.py

03-reglas-variables.py

04-cadenas.py

05-subcadenas.py

📚 Temas abordados:

01 – Hola mundo:

Primera impresión de texto con print().

Fundamento del entorno de ejecución.

02 – Variables:

Declaración e impresión de variables.

Uso de print() con variables.

03 – Reglas de variables:

Identificadores válidos: sin espacios, sin comenzar con número, sin símbolos especiales.

Uso correcto de snake_case.

04 – Cadenas:

Definición de cadenas (str).

Uso de comillas simples, dobles y triples.

Cadenas multilínea.

05 – Subcadenas:

Acceso por índice: cadena[0]

Rangos: cadena[0:3]

Combinación con print() para mostrar porciones de texto.

🧠 Observaciones:
Día de fundamentos absolutos. Se establecieron las bases del lenguaje, diferenciando bien entre nombres válidos,
estructura textual, y manipulación básica de cadenas. Todo esto sirvió de antesala para los métodos y entradas del día
siguiente.

🗓️ Bitácora de estudio – Día 2
📅 Fecha: 2025-06-10
📁 Archivos trabajados:

06-metodos-cadenas.py

07-formatos-cadenas.py

08-entrada-datos.py

(Proyecto aplicado: proyecto-id.py)

📚 Temas abordados:

06 – Métodos de cadenas:

.upper() para mayúsculas

.lower() para minúsculas

07 – Formatos de cadenas:

Concatenación con +

Interpolación con f-strings

Interpolación multilínea (f"""...""")

08 – Entrada de datos:

Captura con input()

Conversión de tipos: int(), float()

Diferencia entre valores codificados y proporcionados por el usuario.

Proyecto – Generador de ID único:

Subcadenas ([0:2]) de nombre y apellido

Captura de año

Número aleatorio con randint(0, 9999)

Unión con interpolación y transformación a mayúsculas con .upper()

Presentación en una sola línea.

🧠 Observaciones:
Transición directa del texto estático al texto dinámico. Se habilitó la lógica de interacción con el usuario,
preparación de datos y presentación personalizada. El mini-proyecto consolidó los elementos vistos en un ejercicio
funcional.

## 📘 Bitácora de Estudio — Día 3

- **📅 Fecha:** 2025-06-11
- **⏰ Tiempo estimado:** 25 minutos (antes de entreno)
- **🎯 Objetivo:** Estudiar métodos de cadenas, entrada de datos, formato, e iniciar reto práctico de generación de
  email.
- **📍 Plataforma:** Udemy (Curso de Python - Módulo de Operadores Hipnóticos)

---

### 🔸 Actividades realizadas

1. **Estudio rápido (previo al entreno):**
    - Desarrollo de un **generador de email** solicitado como reto práctico en menos de 15 minutos.
    - **Descripción del ejercicio:**
        - Mensaje de bienvenida con formato especial.
        - Solicitud de nombre y apellido mediante `input()`.
        - Concatenación del nombre, un punto, el apellido y el dominio `"@ciudadgotica.com"` como string.
        - Uso de `.lower()` para convertir el email final a minúsculas.
        - Impresión del resultado con `print()` en formato interpolado, multi-línea, con saltos de línea y tabulación.

    - **Lógica del código implementado:**
      ```python
      # Generación de email
 
      # Mensaje de presentación
      print("*** Bienvenido al sistema de generación de emails de Ciudad Gótica ***")
 
      # Entrada de datos
      nombre = input("¿Cuál es tu nombre?: ")
      apellido = input("¿Cuál es tu apellido?: ")
 
      # Creación del correo
      correo = "@ciudadgotica.com"
      username = nombre + "." + apellido + correo
      email_terminado = username.lower()
 
      # Mensaje final
      print(f'''
      Tu nuevo email generado por el sistema es:
      \t[{email_terminado}]
      \t*** Felicidades ***
      ''')
      ```

2. **Cuestionario "Variables y cadenas en Python" (3 preguntas):**
    - **Pregunta 1:** ¿Cuál de los siguientes es un nombre de variable válido?
        - ✅ Correcta: `__var__` (uso de guiones bajos es válido)
    - **Pregunta 2:** ¿Cuál opción es una buena práctica para nombrar variables?
        - ✅ Correcta: `mi_var` (uso de notación *snake_case*)
    - **Pregunta 3:** ¿Cómo se puede declarar una cadena `"Hola Mundo"`?
        - ✅ Correcta: Usando comillas simples o dobles, pero con apertura y cierre iguales.

3. **Resumen del progreso en Udemy:**
    - El sistema marcó como **"Primer día del módulo completado"** (aunque lo estudié en 3 sesiones).
    - Ya se han cubierto 8 archivos (consecutivos del 01 al 08), numerados y organizados por tema:
        - Día 1 (5 archivos): `01_hola_mundo.py`, `02_variables.py`, `03_reglas_variables.py`, `04_cadenas.py`,
          `05_subcadenas.py`
        - Día 2 (3 archivos): `06_metodos_cadenas.py`, `07_formato_cadenas.py`, `08_entrada_datos.py`
    - Día 3 aún no tiene archivo numerado, pero corresponde a `09_generador_email.py` que será organizado luego.

---

### 🧠 Observaciones

- Se notó una mejora en la velocidad de razonamiento y estructura lógica al resolver el reto práctico.
- En esta ocasión no se recibió asistencia directa en la escritura del código: fue elaborado con total autonomía.
- Se buscó aplicar buenas prácticas (uso de `.lower()`, concatenación clara, print con formato), pero aún pueden
  optimizarse ciertos aspectos (uso de `f-strings` más eficientes o validaciones de entrada).

---

### ✅ Estado de los módulos

- Módulo de introducción: **Finalizado**
- Variables y cadenas: **Finalizado**
- Entrada de datos: **Finalizado**
- Módulo actual: **Operadores Hipnóticos**
    - Operadores aritméticos: empezado y probado con variables `a = 10`, `b = 5`.
    - Operaciones realizadas:
        - Suma, resta, multiplicación, división, módulo, exponenciación.
        - Sintaxis y resultado verificados.
    - Por avanzar: Operadores de asignación simple y compuesta.

---

### 🤔 Reflexión del día

> "En solo 25 minutos resolví un reto práctico, respondí un cuestionario completo y anoté avances con precisión. No se
> trata de la cantidad de tiempo, sino de cómo lo aprovecho. Al regresar del entrenamiento, puedo continuar con más
> claridad, sabiendo que esta base ya está firme."

📘 Bitácora de Estudio — Día 4
📅 Fecha: 2025-06-12

⏰ Tiempo estimado: 35 minutos (noche)

🎯 Objetivo: Profundizar en operadores de asignación compuesta, tipos de datos y formatos de salida.

📍 Plataforma: Udemy – Curso Python Total (módulo: Operadores Hipnóticos)

🔸 Actividades realizadas
Revisión de operadores de asignación compuesta:

Aplicación de:

python
Copiar
Editar
x = 10
x += 5 # x = 15
x -= 3 # x = 12
x *= 2 # x = 24
x /= 4 # x = 6.0
x //= 2 # x = 3.0
x %= 2 # x = 1.0
x **= 3 # x = 1.0
Se comprendió que el valor se actualiza en cada línea con el nuevo resultado.

Introducción práctica a input() y formateo con f-strings:

Se ensayó una interpolación de strings con variables numéricas:

python
Copiar
Editar
nombre = "Daniel"
edad = 28
print(f"{nombre} tiene {edad} años.")  # ✅ Correcto
Se observó que el uso de f"" convierte automáticamente los enteros a string en contexto de impresión.

Mini desafío nocturno: slicing y transformación de cadena:

Transformar "Estudiar es duro" en "Estudiar es poderoso" usando slicing:

python
Copiar
Editar
frase = "Estudiar es duro"
nueva = frase[:13] + "poderoso"
print(nueva)  # ✅ Estudiar es poderoso
Uso correcto del operador //:

Se entendió que // hace división entera (sin decimales).

También se vio que puede combinarse con asignación:

python
Copiar
Editar
a = 17
a //= 4 # Resultado: 4
🧠 Observaciones
Se integró por primera vez la práctica de entrada y salida de datos reales (input() y print()).

El operador // y **= todavía no resultan completamente automáticos, pero se usan con más naturalidad.

La interpolación con f-strings fue una mejora clara respecto al uso de comas o concatenación con +.

✅ Estado del módulo
Asignación compuesta: ✔️ Dominado en varios contextos.

Interpolación: ✔️ Aplicada y entendida.

Tipos numéricos: ✔️ Se comprendió cómo interactúan con print().

Slicing e impresión: ✔️ Aplicado con seguridad.

🤔 Reflexión del día
"Sentí que ya comienzo a hablar con el lenguaje. Me veo capaz de crear frases, imprimir resultados, y transformar
cadenas. Aún me confundo con algunas operaciones menos comunes, pero estoy viendo cómo se combinan. Me gusta resolver
cosas reales, incluso con poco tiempo."

# 📘 Bitácora de Estudio — Día 4

- **📅 Fecha:** 2025-06-12
- **⏰ Tiempo estimado:** 30 minutos (previo al descanso)
- **🎯 Objetivo:** Estudiar operadores de asignación compuesta y reforzar slicing, casing y formato interpolado.
- **📍 Plataforma:** Udemy y ejercicios integrados

---

### 🔸 Actividades realizadas

1. **Estudio de operadores de asignación compuesta (`+=`, `-=`, `*=`, `/=`, `//=`, `**=`):**
    - Se practicaron combinaciones con `a = 10`, `b = 5`.
    - Ejemplo de uso:
      ```python
      a = 12
      b = 4
      a //= b
      print(a)  # 3
      ```

2. **Reforzamiento de slicing en cadenas complejas:**
    - Se usó la cadena `"Python es divertido"` para extraer subcadenas específicas.
    - Se comprendió mejor el rango `[inicio:fin]` donde `fin` no se incluye.

3. **Practicar casing (uso de `.upper()`, `.lower()`, `.capitalize()`):**
    - Se revisaron usos correctos para transformar strings antes de mostrar en pantalla.
    - Se aplicó en ejercicios de generación de emails y mensajes personalizados.

4. **Uso de `input()` con formato interpolado (`f""`):**
    - Se implementó correctamente para recibir datos y mostrarlos formateados:
      ```python
      nombre = input("Nombre: ")
      apellido = input("Apellido: ")
      print(f"Hola {nombre.capitalize()} {apellido.capitalize()}, bienvenido.")
      ```

---

### 🧠 Observaciones

- Se comprendió la diferencia entre operadores simples y compuestos, así como su ventaja sintáctica.
- Se aplicaron correctamente los métodos `.lower()` y `.upper()` para asegurar estandarización en datos sensibles (como
  correos).
- Se ejecutaron los ejercicios sin errores de sintaxis ni de lógica.

---

### ✅ Estado del avance

- Operadores Aritméticos: ✔️
- Operadores de Asignación Simple: ✔️
- Operadores de Asignación Compuesta: ✔️
- Slicing: ✔️ (revisión y refuerzo)
- Métodos de casing: ✔️
- Interpolación y entrada de datos: ✔️

# 📘 Bitácora de Estudio — Día 5

- **📅 Fecha:** 2025-06-13
- **⏰ Tiempo total:** 50 minutos
- **🎯 Objetivo del día:** Reforzar comprensión de operadores aritméticos y operadores de asignación compuesta; repasar
  slicing, concatenación e interpolación.
- **📍 Actividad principal:** Responder quiz del Día 5 basado en lo estudiado y repasado.

---

### 🔸 Actividades realizadas

1. **Repaso rápido de teoría:**
    - Se estudió sintaxis de operadores: `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`.
    - Se revisó cómo cada operador modifica la variable original y cambia el tipo en algunos casos (ej.: de `int` a
      `float`).

2. **Realización del *Quiz Día 5* :**
    - Se respondieron todos los ejercicios correctamente, comprobando mentalmente y luego ejecutando para validar
      resultados y comprender el comportamiento.

---

### ✅ Avance logrado

- **Operadores aritméticos:** ✔️
- **Asignación compuesta:** ✔️
- **Slicing, concatenación e interpolación:** ✔️
- **Quiz:** Completado y validado.

---

### 🧠 Reflexión

> "Repasar operadores me permitió consolidar la lógica matemática en código. Ejecutar luego de responder mentalmente
> ayudó a detectar sutiles variaciones de tipo (como el paso a `float`) y a entender mejor cada operación."

# 🧠 Bitácora de Estudio — Día 6

📅 Fecha: 14 de junio de 2025  
🎯 Temas estudiados: Constantes en Python, Inmutabilidad de cadenas, Caracteres especiales, Concatenación y Formateo de
cadenas.  
⏱️ Tiempo aproximado: 1 hora 30 minutos  
📍 Modalidad: Estudio individual + autoevaluación

## Detalle del estudio

Hoy no realicé estudio con video o lectura guiada sino que **repasé activamente todos los temas vistos hasta ahora**
mediante una técnica de evaluación: resolver un quiz integrador de todos los temas anteriores y los nuevos, que incluyó:

- Convención para definir constantes en Python (uso de mayúsculas).
- Concepto de **inmutabilidad de cadenas** y cómo funciona la memoria en ese contexto.
- Caracteres especiales como `\n`, `\t`, comillas escapadas.
- Concatenación: uso de `+` y `.join()`.
- Formateo: `f-string` vs `.format()`.
- Repaso de slicing, convenciones de nombres de variables y uso correcto del operador `+`.

🧩 También observé cómo distintas formas de concatenar pueden influir en el contexto (listas vs strings simples).

## Reflexiones

💬 Este día fue muy revelador especialmente en lo relacionado con la inmutabilidad de las cadenas y cómo Python gestiona
internamente los objetos en memoria.  
El formateo con `f-string` me pareció más legible que `.format()` y entendí que las convenciones (como las constantes en
mayúscula) son más una responsabilidad del programador que del lenguaje.

## Dificultades

🔸 La inmutabilidad de las cadenas fue lo más desafiante al inicio por el concepto abstracto de "objeto en memoria" y la
forma como Python apunta a esa dirección.  
🔸 También me confundí momentáneamente con el uso correcto de `.join()` y su aplicación en listas.

---

📌 *Bitácora realizada posterior al estudio como parte del sistema de control diario.*
