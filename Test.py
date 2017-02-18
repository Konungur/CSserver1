import time
import sys


def greetings():
    """
    this func will greet you :)
    """
    time.time()  # starting timer
    print('Enter your name: ')  # asking for player1 name
    player1 = str(input())
    print('And now you: ')
    player2 = str(input())  # asking for player2 name
    time.sleep(1)  # setting pause on 1 sec
    print('Greetings, mate`s!')
    time.sleep(2)  # setting pause on 2 sec
    time.time()
    return 'Prepare to battle...' + player1 + " and " + player2
print(greetings())


def game_field():  # create a 10x10 board
    game_main_field = []
    second_player_field = []
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for x in range(len(letters)):
        game_main_field.append([])
        second_player_field.append([])
        for y in range(1, 11):
            game_main_field[x].append(str(letters[x]) + str(y))
            second_player_field[x].append(str(letters[x]) + str(y))
    set_fleet(game_main_field, second_player_field)  # call function to choose ships


def set_fleet(game_main_field, second_player_field):
    ships = {'Battleship': 4, 'Cruiser': 3, 'Submarine': 1, 'Destroyer': 2}  # size of each ship
    player_one_fleet = [['Battleship', 1], ['Cruiser', 2], ['Submarine', 4],
                        ['Destroyer', 3]]  # number of ships to place
    player_two_fleet = [['Battleship', 1], ['Cruiser', 2], ['Submarine', 4], ['Destroyer', 3]]
    for ship1 in player_one_fleet:  # place ships
        item = 0
        while ship1[1] > 0:  # check there's ships available
            item += 1
            type_of = ship1[0]
            ship_size = ships[ship1[0]]
            position = input("Player 1, enter coordinates of {0}: ".format(ship1[0]))  # choose position (i.e, A1)
            check = set_ship(game_main_field, ship_size, position, type_of)
            if check is True:
                ship1[1] -= 1
            else:
                print("Can't place ship here.")
    for ship2 in player_two_fleet:  # place ships
        item = 0
        while ship2[1] > 0:  # check there's ships available
            item += 1
            type_of = ship2[0]
            ship_size = ships[ship2[0]]
            position = input("Player 2, enter coordinates of {0}: ".format(ship2[0]))  # choose position (i.e, A1)
            check = set_ship(second_player_field, ship_size, position, type_of)
            if check is True:
                ship2[1] -= 1
            else:
                print("Can't place ship here.")
    play_game(game_main_field, second_player_field)


def check_set_space(game_main_field, ship_size, col, row, direction):  # check that ship can be placed
    check_ships = ["Battleship", "Cruiser", "Submarine", "Destroyer"]
    if direction == 'up':
        if row - int(ship_size) >= 0:  # check ship within boundaries
            for i in range(0, ship_size):
                if game_main_field[int(row - i)][int(col) - 1] not in check_ships:  # check for collision
                    pass
                else:
                    return False
            return True
        else:
            return False
    elif direction == 'down':
        space = row + int(ship_size)
        if space <= 11:  # check ship within boundaries
            for i in range(0, ship_size):
                rawr = game_main_field[int(row + i)][int(col) - 1]
                if rawr not in check_ships:  # check for collision
                    pass
                else:
                    return False
            return True
        else:
            return False
    elif direction == 'right':
        if col + int(ship_size) <= 11:  # check ship within boundaries
            for i in range(0, ship_size):
                if game_main_field[int(row)][int(col) + i - 1] not in check_ships:  # check for collision
                    pass
                else:
                    return False
            return True
        else:
            return False
    elif direction == 'left':
        if col - int(ship_size) >= 0:  # check ship within boundaries
            for i in range(0, ship_size + 1):
                if game_main_field[int(row)][int(col - 1) - i] not in check_ships:  # check for collision
                    pass
                else:
                    return False
            return True
        else:
            return False


def set_ship(game_main_field, ship_size, position, ship_type):
    row = position[0]
    row = ord(row) - 65
    if len(position) > 2:
        col = (position[1] + position[2])
    else:
        col = position[1]
    row = int(row)
    col = int(col)

    orientation = int(input("Place ship: \n"
                            "1. Vertically \n"
                            "2. Horizontally"))  # horizontal or vertical
    if orientation == 1:
        direction = int(input("Choose direction: \n"
                              "1. Up \n"
                              "2. Down"))  # up or down
        if direction == 1:
            result = check_set_space(game_main_field, ship_size, col, row, 'up')
            if result is True:
                for i in range(0, ship_size):
                    game_main_field[int(row - i)][int(col) - 1] = str(ship_type)

            print(game_main_field)
        else:
            result = check_set_space(game_main_field, ship_size, col, row, 'down')
            if result is True:
                for i in range(0, ship_size):
                    game_main_field[int(row + i)][int(col) - 1] = str(ship_type)

            print(game_main_field)
    else:
        direction = int(input("Choose direction: \n"
                              "1. Right\n"
                              "2. Left"))
        if direction == 1:
            result = check_set_space(game_main_field, ship_size, col, row, 'right')
            if result is True:
                for i in range(0, ship_size):
                    game_main_field[int(row)][int(col) + i - 1] = str(ship_type)
            print(game_main_field)
        else:
            result = check_set_space(game_main_field, ship_size, col, row, 'left')
            if result is True:
                for i in range(0, ship_size):
                    game_main_field[int(row)][int(col) - i - 1] = str(ship_type)
            print(game_main_field)
    return result


def play_game(game_main_field, second_player_field):
    print("Player 1 starts.")
    player_one_move = True
    player_two_move = False
    check_ships = ["Battleship", "Cruiser", "Submarine", "Destroyer"]
    victory = False
    while True:
        if player_one_move:
            while not victory:
                pos = input("Player 1, enter target: ")
                row = pos[0]
                row = ord(row) - 65
                if len(pos) > 2:
                    col = (pos[1] + pos[2])
                else:
                    col = pos[1]
                row = int(row)
                col = int(col) - 1
                target = second_player_field[row][col]
                ship_damage = target
                target = str(ship_damage)
                if target in check_ships:
                    print("Hit")
                else:
                    print("Miss")
                second_player_field[row][col] = "X"
                destroyed = True
                for y in second_player_field:
                    if destroyed:
                        for x in y:
                            if x == ship_damage:
                                destroyed = False
                                break
                    else:
                        break
                if destroyed:
                    if target in check_ships:
                        print("{0} DESTROYED.".format(target))
                victory = True
                for y in second_player_field:
                    if victory:
                        for j in y:
                            if j not in check_ships:
                                victory = True
                            else:
                                victory = False
                                break
                if victory:
                    print("PLAYER 1 WINS")
                    exit_game = str(input())
                    print("Wanna leave game? Y/N ", exit_game)
                    if exit_game == "Y":
                        sys.exit()
                    elif exit_game == "N":
                        print("Thanks for playing, enjoy your day ^^")
                player_one_move = False
                player_two_move = True
                break
        elif player_two_move:
            while not victory:
                pos = input("Player 2, enter target: ")
                row = pos[0]
                row = ord(row) - 65
                if len(pos) > 2:
                    col = (pos[1] + pos[2])
                else:
                    col = pos[1]
                row = int(row)
                col = int(col) - 1
                target = game_main_field[row][col]
                ship_damage = target
                target = str(ship_damage)
                if target in check_ships:
                    print("Hit")
                else:
                    print("Miss")
                game_main_field[row][col] = "X"
                destroyed = True
                for y in game_main_field:
                    if destroyed:
                        for x in y:
                            if x == ship_damage:
                                destroyed = False
                                break
                    else:
                        break
                if destroyed:
                    if target in check_ships:
                        print("{0} DESTROYED.".format(target))
                victory = True
                for y in game_main_field:
                    if victory:
                        for j in y:
                            if j not in check_ships:
                                victory = True
                            else:
                                victory = False
                                break
                if victory:
                    print("PLAYER 2 WINS")
                    exit_game = str(input())
                    print("Wanna leave game? Y/N ", exit_game)
                    if exit_game == "Y":
                        sys.exit()
                    elif exit_game == "N":
                        print("Thanks for playing, enjoy your day ^^")
                player_one_move = True
                player_two_move = False
                break
game_field()
