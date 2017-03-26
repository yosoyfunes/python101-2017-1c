

print(string_variable)
print(my_variable)

# Print es una funcion que imprime la variable que recibe por parametro (cuando veamos objetos veremos en que se basa este comportamiento)

def my_print_method(my_parameter):
    print(my_parameter)

my_print_method(string_variable)



def my_multiplication_method(number_one, number_two, tree):
    tree("")
    return number_one * number_two

my_multiplication_method(1,3, my_print_method)


print(my_multiplication_method(56, 75))

my_print_method(my_multiplication_method('b', 5))  # Que debería hacer esto?
