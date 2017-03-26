def mi_funcion(arg1, arg2):
    return arg1 + arg2

def mi_suma_grande(arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5

mi_suma_grande(13, 45, 66, 3, 4)

def suma_simplificada(arg_list):
    return sum(arg_list)

suma_simplificada([13, 45, 66, 3, 4])

# pero necesita una lista :(

def que_son_args(*args):
    print(args)

que_son_args(12, 35, 64, 'hello')

def suma_simplificada(*args):
    return sum(args)  #args es una tupla de elementos pasados

suma_simplificada(13, 45, 66, 3, 4)

###

# Tambien como tupla de argumentos podemos pasar kwargs

def que_son_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

que_son_kwargs(name='Jose', location='UK')
que_son_kwargs(12, 35, 66, name='Jose', location='UK')

# args are a tuple
# kwargs is a dictionary
# This will come in handy!
