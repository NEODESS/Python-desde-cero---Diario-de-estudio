# Tema: Subcadenas y slicing
# Fecha: 2025-06-09
# Qué se practica: Uso de slicing para extraer partes de cadenas.
# Qué aprendiste: Aprendí a extraer subcadenas usando índices con slicing.


# subcadenas en python

mensaje = 'Hola Mundo'

print(mensaje)

# para generar subcadena hola -> cadena[indice_inicio:indicie_final + 1]
subcadena_hola = mensaje[0:4]
print(subcadena_hola)

# ejercicio, sacar la subcadena mundo de la variable mensaje

subcadena_mundo = mensaje[5:9 + 1]
print(subcadena_mundo)

subcadena_mundo = mensaje[5:10]
print(subcadena_mundo)
