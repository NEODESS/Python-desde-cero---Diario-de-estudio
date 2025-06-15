# Generador de email

# Mensaje de presentación
print('*** Bienvenido al sistema de generación de email de ciudad gotica ***')

# Entrada de datos

nombre = input('¿Cual es tu nombre?: ')
apellido = input('¿Cual es tu apellido?: ')

# Creación del correo
correo = '@ciudadgotica.com'
user_name = nombre + '.' + apellido + correo
email_terminado = user_name.lower()

# Mensaje de respuesta

print(f'''Tu nuevo email generado por el sistema es:
    {email_terminado}
    *** Felicidades ***''')
