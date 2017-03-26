#Ejemplo de funcion input

'''
input posee parametro opcional de mensaje, en este caso
el mensaje es "ingrese valor \n"
Aqui, \n significa new line. Osea un salto de linea o un enter en la terminal.
'''
value = input("ingrese valor\n")
'''
El programa para su ejecucion hasta no recibir datos de entrada.
El interprete queda loopeando dentro de la funcion input hasta obtener el valor deseado.
Luego de obtenerlo, 'value' posee el valor de entrada del usuario
'''
print(value)
print(type(value))
