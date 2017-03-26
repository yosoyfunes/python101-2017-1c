personas_que_conozco = ["John", "Rolf", "Anne"]
user_name = input("ingresa tu nombre: ")
if user_name in personas_que_conozco:
    print("hola, te conozco!")


if user_name in personas_que_conozco:
    print("hola {}, te conozo!".format(user_name))


if user_name in personas_que_conozco:
    print("hola {name}, te conozco!".format(name=user_name))

"Hola {name}, Te conozco {}!".format("bien", name=user_name)
"hola {}, te conozco {}!".format("John", "bien")


def a_quien_conozco():
    names = input("Ingrese los nombres de las personas, separado por coma: ")
    names_list = names.split(",")
    return names_list

def preguntar_usuario():
    # pregunta al usuario por su nombre
    # verifica que el usuario este en la lista
    # si esta, imprime algo

    user_name = input("Ingresa tu nombre: ")
    if user_name in a_quien_conozco():
        print("Hola {}, Te conozco!!".format(user_name))
