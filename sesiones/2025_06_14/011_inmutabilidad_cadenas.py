# Inmutabilidad de una cadena
# Una vez que se crea una cadena, sus caracteres no pueden ser modificados
# Si se desea modificar, tenemos que crear una nueva cadena
cadena1 = 'Hola mundo'  # Aqui creamos el objeto str 'Hola mundo'
# cadena1[0] = 'h'
# print(cadena1) Al hacer esto nos saldra un error de tipo 'str' debido a que
# no se pueden modificar los caracteres de una variable ya que el valor asignado esta siendo
# guardado como objeto en la memoria ram (random acces memory) y este objeto es inmutable,
# no se puede modifica. Lo quue si podemos hacer es asignar una nueva cadena, Ejemplo
# cadena1 = ('Adios')  aqui lo que sucede es que al cambiar o asignarle un valor diferente,
# este se crea como objeto  en la memoria y la variable ya no apunta al valor anterior,
# es como si cambiaramos la direccion del valor que tiene la variable y al cambiarse la direccion  apuntar a otra
# los carteres anteriores se vuelven candidatos para ser eliminados de la memoria
# ya que no estan siendo "vistos" o  llamados y asi parece que el nuevo valor, toma el lugar del anterior

cadena2 = cadena1  # en este caso como estamos referenciando a la primera variable que se creo
# antes de darle un nuevo valor, hace que esta no sea elegible para ser borrada,
# debido a que tiene a un espectadoro su valor esta siendo solicitado
# Ejemplo
cadena1 = 'Adios'
print(cadena1)
print(cadena2)

# En resumen, mientas que aun existan VARIABLES, que referencien a los objetos,
# aun se podran seguir usando en nuetro programa, cuando yyya no se referencien
# estos pasaran a ser elegibles para ser borrados
