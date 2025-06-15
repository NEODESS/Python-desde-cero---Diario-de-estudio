# Constantes en python
# Por lo generarl no existe un tipoespecifico para definir una  constante en python
# de manera específica, se le concidera una convención


# Si seguimos la siguiente convención de declarar el nombre de una variable en mayusculas
# y con ella indicamos que el valor de esta variable No debe modificarse una vez inicializada,
# le otorgamos el caracter de una constante
# NOMBRE_CONSTANTE = valor
# PI = 3.14159
# Ejemplo
print('*** Constante en python ***')

NOMBRE_BD = 'clientes_db'

print('Nombre de la base de datos:', NOMBRE_BD)
# Aunque Python no lo prohibe, no se debe modificar el valor de una constante
# (es decir, una variable declarada totalmente en mayuscula siguiendo
# las buenas prácticas y la convención de la que hablabamos)

# Tambien existen constantes que ya vienen incorporadas en el lenguaje python,
# aunque en este caso no está en mayuscula
# Ejemplo
print('Valord de math.pi:', math.pi)
# este tipo de constantes se definio que se usara en minusculas ya que estan incorporadas en el lenguaje 
# ya que suele usarse en formulas aritmeticas bastante complejas
