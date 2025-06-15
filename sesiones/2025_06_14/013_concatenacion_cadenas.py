# Concatenación de cadenas

# Es una operacion que permite convinar 2 o mas cadenas para formar una nueva
# En python existen varias Formas

# -Uso de operador  + : es el mas directo para concatenar
# Ejemplo: Concatenacion = 'Hola' + 'Mundo' Si los valores don cadenas hace la concatenacion

# -Uso de join: La fusion join nos permite unir tantas cadenas como necesitemos,
# solo debemos pasar cada cadena a concatenar separadas por una coma y entre parentesis
"".join(["cadena1", "cadena2", "cadena3"])  # a este metodo join le pasamos como parametro una lista
# -Lista -> es un conjunto de datos separados por coma (,)
# Ejemplo
cadena1 = 'Hola'
cadena2 = 'Mundo'
concatenacion = cadena1 + ' ' + cadena2
print(concatenacion)

# Usando el metodo join
concatenacion = ''.join([cadena1, ' ', cadena2])
print(concatenacion)
