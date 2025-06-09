# Tema: Reglas de Variables
# Fecha: 2025-06-09
# Qué se practica: Nombramiento válido de variables y uso de convenciones como snake_case.
# Qué aprendiste: Aprendí las reglas de sintaxis para nombrar variables correctamente y las buenas prácticas.

# Reglas para definir el nombre de variables

# 1. Comenzar con letra o guion bajo (_)
_mi_variable = 30

# 2. Puede continuar con letras, numeros o guion bajos (_)
_mi_variable2 = 40

# 3mi_variable2 = 40 # esto arroja un error
_mi_variable234 = 40

# 3. Sensible a mayusculas y minusculas
mi_variable = 30
# print(Mi_variable) esto arroja un error porque devio empezar por
# minuscula si la variable esta definida a partir de una minuscula

print(mi_variable)

# No se pueden usar palabras reservadas (keyword
# class, if, for,
# class = 50 esto da error por que estas llamando una variable reservada por py
classs = 50
print(classs)

# Buenas practicas en Python
# Notacion snake case (notacion de serpiente) es parecido al serpenteo de una serpiente nnn_nnn_nnn_ 
nombre_usuario = 'Juan'
# notacion de camello o camel case, se inicia con minuscula y
# las siguientes palabras con mayuscula (no recomendable en python)
nombreUsuario = 'Carlos'
# Notacio Pascal (Primera letrra de cada palabra en mayuscula) no se recomienda en python
NombreUsuario = 'Karla'

print(nombre_usuario + ',', nombreUsuario + ',', NombreUsuario + '.')
