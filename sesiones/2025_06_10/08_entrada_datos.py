# Entrada de Datos por consola: input()

numero = 10  # la definición en la variable, aquí se le conoce como valor en codigo duro
# ya que este valor lo proporcionamos nosotros y no el usuario

# mensaje = input('Proporciona un mensaje: ')
# print(f'El mensaje recibido es: {mensaje} ')

numero1 = input('Cual es tu primer número: ')
# print(numero1)
numero2 = input('Cual es tu segundo número: ')
# print(numero2)

# resultado_suma = numero1 + numero2
# print(f'Resultado de la suma: {resultado_suma}')  # aqui no se realiza la suma
# ya que lo que sucede es una concatenacion de los valores proporcionados

# Usaremos la funcion int() -> Convierte una cadena a un tipo de entero
# podriamos hacerlo de las siguientes 2 formas

# numero1 = int(input('Cual es tu primer número: ')) -> aqui se le agrega int y se envuelve toda la definicion
# para hacer la convercion
# print(numero1)
# numero2 = int(input('Cual es tu segundo número: '))
# print(numero2)
# o tambien podriamos hacer la convercion cuando vayamos a hacer la operacion,
# agregamos int para que en ves de concatenar, realice la suma

resultado_suma = int(numero1) + int(numero2)
print(f'Resultado de la suma: {resultado_suma}')
