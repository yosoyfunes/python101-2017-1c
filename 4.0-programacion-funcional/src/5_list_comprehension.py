lista_a_5 = [0, 1, 2, 3, 4]
otra_lista_a_5 = [x for x in range(5)]

copia_lista_a_5 = lista_a_5[:]

for my_number in range(10):
    print(my_number)

#############################

print([my_number for my_number in range(10)])

print([my_number * 2 for my_number in range(10)])

print([n for n in range(10) if n % 2 == 0])

names_list = ["John", "Rolf", "Anne"]
lowercase_names = [name.lower() for name in names_list]
print(lowercase_names)


tupla_a_5 = (x for x in range(5)) ###Generador a 5
print(tupla_a_5)

set_a_5 = {x for x in range(5)}
print(set_a_5)

primes_set = {x for x in range(2, 101) if all(x%y for y in range(2, min(x, 11)))}
print(primes_set)

lista_tupla = [(x,y) for x in range(len(names_list)) for y in names_list]
print(lista_tupla)

dict_values = {x:y for x,y in lista_tupla}

print(dict_values)
