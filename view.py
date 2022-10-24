from tabulate import tabulate

# Визуализация программы
def hello_one():
    # Приветствуем игроков
    print('Приветствую вас в игре крестики нолики!')
    name_one_player = input("Введите ваше имя: ")
    print(f'Приветствую тебя, {name_one_player}!')
    return name_one_player


def hello_two():
    name_two_player = input("Введите имя второго игрока: ")
    print(f'Приветствую тебя, {name_two_player}!')
    print()
    return name_two_player


def playing_field():
    # Создание игрового поля
    matrix_game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    headers_table = ['GAME ', 'for ', 'YOU ']

    print(tabulate(matrix_game, headers=headers_table, tablefmt='fancy_grid'))

    return matrix_game


def winner(count, random_move, name_one_player, name_two_player):
    # Вывод победителя
    if count == True and random_move == 2:
        print(f'🔥🔥🔥 Победил игрок: {name_one_player} 🔥🔥🔥')
    elif count == True and random_move == 1:
        print(f'🔥🔥🔥 Победил игрок: {name_two_player} 🔥🔥🔥')
    elif count == None:
        print('НИЧЬЯ 😥:')
