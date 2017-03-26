my_string = "hello"

for character in my_string:
    print(character)

for asdf in my_string:
    print(asdf)

my_list = [1, 2, 5, 3, 67]

for number in my_list:
    print(number)

for number in my_list:
    print(number ** 2)

debe_continuar = True
while debe_continuar:
    print("I'm continuing!")

    user_input = input("Debo continuar? (s/n)")
    if user_input == 'n':
        debe_continuar = False
