# Formateo de cadena


# El formateo es una  tecnica que nos permite incluir textos, variables, expresiones
# e incluso dar ciertos formatos a nuestras cadenas

# -F string (Python 3,6+):  es  la mas recomendada por ser las mas sencilla, rapida y legible
# Ejemplo
# resultado = f'Hola {variable}'  # se le da valor a una variable comenzando con la letra f seguido de comillas,
# se le incluye el texto o str que se quiere mostras y dentro de llaves ({})
# se ingresa la variable, asi podemos crear cadenas de forma dinamica

# - Metodo format -> es muy versatil y poderoso,, permite construirr cadenas muy complejas
# se utiliza desde la version 2.7 de python
# resultado = 'hola {}'.format(variable) por ser mas complejo que los demas, se recomienda usa f-string

nombre = 'Juan'
edad = 30

# f-string
mensaje = f'Hola, me llamo {nombre} y tengo {edad} años.'
print(mensaje)

# Metodo format
mensaje = 'Hola, me llamo {} y tengo {} años.'.format(nombre, edad)
print(mensaje)
