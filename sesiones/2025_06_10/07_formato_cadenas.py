# Formato de Cadenas en Python

var_hola = 'Hola'
var_mundo = 'Mundo'

# Imprimir los valores
print(var_hola, var_mundo)

# Concatenacion de cadenas (unir dos o mas cadenas)
var_hola_mundo = var_hola + var_mundo
print(var_hola_mundo)

# Ahora con espacio por que la anterior es "HolaMundo"
var_hola__mundo = var_hola + ' ' + var_mundo
print(var_hola__mundo)
# El mas (+) sirve tanto para operaciones aritmeticas como para concatenar cadenas (juntarlas)
# todo depende del tipo de dato con el que esté trabajando, si los tipos de datos son numero
# realiza una operación aritmetica

# Interpolación de cadenas, usando la letra f

var_hola__mundo = f'Mi cadena: {var_hola} {var_mundo}'  # imporntante colocar la letra f al inicio
# ya que sin la f es solo una cadena mas

print(var_hola__mundo)

# Interpolación con multilineas, f''' ''', o f""" """ (impresión de cadena multilinea)
print(f'''Mi cadena: 
    {var_hola}
        {var_mundo}''')
