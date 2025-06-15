# Sistema de Generador ID Unico

from random import randint

# presentación

print('*** Sistema de Generación ID Único ***')

# Solicitud de valores
nombre = input('¿Cual es tu Nombre?: ')
apellido = input('¿Cual es tu Apellido?: ')
fecha_nacimiento = input('¿Cual es tu Año de Nacimiento (YYYY)?: ')

# Extracción de indices
letras_nombre = nombre[0:2]
letras_apellido = apellido[0:2]
numero_fecha = fecha_nacimiento[2:3 + 1]

# Generar un valor de 4  dígitos aleatorios
aleatorio = randint(0, 9999)

# Convertir en a mayusculas y concatenar
id_unico = f'{letras_nombre}{letras_apellido}{numero_fecha}{aleatorio}'  # cuando llamamos a la variable aleatorio
# se convierte de un int a un str por llamarlo con interpolacion
id_mayusculas = id_unico.upper()

print(f''' \nHola {nombre}, Habitante de Ciudad Gotica!
    Tu nuevo numero de identificación (ID) Generado por el sistema es:
    {id_mayusculas}
    Felicidades!''')
