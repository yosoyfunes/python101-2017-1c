my_dict = {'name': 'Jose','location': 'UK'}

lottery_player = {
    'name': 'Rolf',
    'numbers': (13, 22, 3, 6, 9)
}

dict_in_dict = {
    'universities': [
        {
            'name': 'Oxford',
            'location': 'UK'
        },
        {
            'name': 'Harvard',
            'location': 'US'
        }
    ]
}

##

lottery_player = {
    'name': 'Rolf',
    'numbers': (13, 22, 3, 6, 9)
}

players = [
    {
        'name': 'Rolf',
        'numbers': (13, 22, 3, 6, 9)
    },
    {
        'name': 'John',
        'numbers': (22, 3, 5, 7, 9)
    }
]

# como se selecciona uno de los players

player = players[0]

#como sumar todos los numeros de un player determinado
sum(player['numbers'])

sum([1, 2, 3, 4, 5])

#?????

player.total()
