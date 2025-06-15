# Metodos de Cadenas en Python

# Metodos de la Clase cadena

mensaje = 'Hola Mundo'
print(f'Cadena origina: {mensaje}')

# Convertir a Mayusculas

mensaje_mayusculas = mensaje.upper()
print(f'Cadena en mayusculas: {mensaje_mayusculas}')

# Convertir a Minusculas

print(f'Cadena en minusculas: {mensaje.lower()}')  # en este caso se puede
# agregar el metodo directamente en la variable dentro de f-string

cadena = ' Juan Perez '
print(f'Cadenas con espacios: {cadena}')
print(f'Cadenas sin espacios: {cadena.strip()}')  # Elimina espacios en blanco al inicio y al final
