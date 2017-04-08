
def sqr(x):
    return x ** 2

secuencia = (1,2,3)

funcion = sqr

resultado = map(funcion, secuencia)
print(resultado)
resultado2 = map(sqr, secuencia)
print(secuencia)
print(resultado2)

resultado3 = map(lambda x: x**2, secuencia)

print(resultado3)
print(resultado2 == resultado3)
print(resultado2 is resultado3)
print("abc" is "abc")
