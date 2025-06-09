# Arquitectura del Proyecto 📁: `python_desde_0_diario_de_estudio`

Este repositorio tiene como objetivo documentar de forma clara, progresiva y ordenada el proceso de aprendizaje en Python desde cero, con prácticas diarias, ejercicios personalizados y recursos complementarios. A continuación, se detalla la estructura del proyecto:

---

## 🌲 Estructura general de carpetas y archivos

```plaintext


# 📁 python_desde_0_diario_de_estudio   # Carpeta raíz del repositorio. Contiene todo el proyecto de aprendizaje diario de Python.
    
├── README.md                           # Explica de forma general el propósito del proyecto, cómo navegarlo y cómo usarlo.
├── ARCHITECTURE.md                     # Documento que describe esta arquitectura y sus convenciones de organización.
├── sesiones/                           # Carpeta donde se almacenan las sesiones de estudio por fecha.
    
│   └── 2025_06_09/                     # Subcarpeta correspondiente a la sesión del día 09 de junio de 2025.
│       ├── 01_hola_mundo.py            # Primer script: imprime un mensaje en pantalla con print().
│       ├── 02_variables.py             # Define variables de distintos tipos (int, float, string).
│       ├── 03_reglas_de_variables.py   # Aplica reglas de nombramiento de variables en Python.
│       ├── 04_cadenas.py               # Muestra uso de cadenas, saltos de línea (\n), tabulaciones (\t).
│       └── 05_subcadenas.py            # Aplica slicing para extraer subcadenas desde strings.
    
├── ejercicios/                         # Carpeta para prácticas, retos, pruebas y autoevaluaciones adicionales.
│   └── ejercicios_2025_06_09/          # Subcarpeta con ejercicios correspondientes al día 09 de junio de 2025.
│       └── quiz_2025_06_09.py          # Archivo con preguntas-respuestas prácticas sobre lo aprendido ese día.
    
├── recursos/                           # Carpeta donde se pueden guardar referencias, apuntes, imágenes o links útiles.
│                                       # (Por ejemplo: enlaces a cursos, PDFs, capturas, documentos externos).
    
├── docs/                               # Carpeta para documentación adicional del proyecto (Markdown).
│   ├── buenas_practicas.md             # Documento con buenas prácticas de escritura y estilo en Python.
│   └── glosario.md                     # Diccionario de términos clave aprendidos (con definición y ejemplo corto).
    




📄 Descripción de cada elemento
README.md
Resumen general del propósito del repositorio. Explica qué se estudia, cómo está estructurado el aprendizaje y qué herramientas se utilizan. Este archivo debe ser lo primero que vea cualquier visitante.

ARCHITECTURE.md
Este mismo archivo. Aquí se documenta la arquitectura del repositorio: qué carpetas existen, qué contienen, cómo nombrar archivos y cómo expandir el proyecto de forma ordenada.

🗂️ Carpeta: sesiones/
Contiene subcarpetas por fecha (YYYY_MM_DD). Cada una almacena los archivos .py correspondientes a lo practicado ese día durante el estudio.

2025_06_09/
Primera sesión documentada. Contiene:

01_hola_mundo.py: primer script simple con print().

02_variables.py: declaración y uso básico de variables.

03_reglas_de_variables.py: reglas de nombres válidos y ejemplos inválidos.

04_cadenas.py: manejo de cadenas, saltos de línea, tabulaciones.

05_subcadenas.py: slicing y extracción de subcadenas.

📁 Carpeta: ejercicios/
Aquí se guardan los ejercicios o pruebas prácticas que no vienen directamente del curso (por ejemplo, quices o retos que te coloco yo o que inventas tú).

ejercicios_2025_06_09/
Carpeta que contiene los ejercicios del día 2025-06-09. Dentro:

quiz_2025_06_09.py: contiene una prueba de 5 preguntas basada en los temas estudiados ese día.

📚 Carpeta: recursos/
Espacio reservado para guardar archivos como PDFs, enlaces útiles, hojas de trucos, infografías, etc. También puedes crear subcarpetas dentro si llegas a tener recursos por tema (como “cadenas”, “listas”, “funciones”).

📘 Carpeta: docs/
Contiene documentación complementaria:

buenas_practicas.md: archivo con convenciones de código, nombres de variables, estilo, etc.

glosario.md: archivo tipo diccionario, donde vas agregando definiciones breves de términos que vayas aprendiendo.

🧠 Reglas de organización
Cada archivo .py debe tener un comentario inicial indicando:

Tema.

Fecha.

Qué se practica.

Qué aprendiste.

Los nombres de archivo siguen el formato:
NN_nombre_tema.py, donde NN es el orden del tema del día.

Las carpetas de fecha siguen el formato:
YYYY_MM_DD.

Todo debe estar en minúsculas y con guiones bajos, tanto carpetas como archivos.

✍️ Expansión futura
Puedes crear carpetas por semana si el volumen crece.

Puedes añadir carpeta proyectos/ para integrar mini-proyectos que combinen varios temas.

Puedes vincular con GitHub Pages usando la carpeta docs/ para una versión web navegable.