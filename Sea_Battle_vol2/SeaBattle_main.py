import time
import sys

from Test import set_fleet, play_game, game_field


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


class BattleShipGame:
    """main class of the game"""

    def __init__(self):
        pass

    def game_field(self):  # creating a game field 10 * 10
        game_main_field = []
        second_player_field = []
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        for x in range(len(letters)):
            game_main_field.append([])
            second_player_field.append([])
            for y in range(1, 11):
                game_main_field[x].append(str(letters[x]) + str(y))
                second_player_field[x].append(str(letters[x]) + str(y))
        set_fleet(game_main_field, second_player_field)  # calling to the method that will raise ship placement

    def set_fleet(self, game_main_field, second_player_field, set_ship):
        ships = {'Battleship': 4, 'Cruiser': 3, 'Submarine': 1, 'Destroyer': 2}  # size of ship`s
        player_one_fleet = [['Battleship', 1], ['Cruiser', 2], ['Submarine', 4],
                            ['Destroyer', 3]]  # number of ships, that will be deployed
        player_two_fleet = [['Battleship', 1], ['Cruiser', 2], ['Submarine', 4], ['Destroyer', 3]]  # same for second
        for ship1 in player_one_fleet:  # from this moment, loop will place ship
            item = 0
            while ship1[1] > 0:  # check if there is space for another ship
                item += 1
                type_of = ship1[0]
                ship_size = ships[ship1[0]]
                position = input("Player 1, enter coordinates of {0}: ".format(ship1[0]))  # at this moment player will
                # chose were ship will be deployed
                check = set_ship(game_main_field, ship_size, position, type_of)
                if check is True:
                    ship1[1] -= 1
                else:
                    print("Can't place ship here.")
        for ship2 in player_two_fleet:  # same for another player
            item = 0
            while ship2[1] > 0:
                item += 1
                type_of = ship2[0]
                ship_size = ships[ship2[0]]
                position = input("Player 2, enter coordinates of {0}: ".format(ship2[0]))  # player chose position
                # of deployment
                check = set_ship(second_player_field, ship_size, position, type_of)
                if check is True:
                    ship2[1] -= 1
                else:
                    print("Can't place ship here.")
        play_game(game_main_field, second_player_field)

    def check_set_space(self, game_main_field, ship_size, col, row, direction):  # check that ship can be placed
        check_ships = ["Battleship", "Cruiser", "Submarine", "Destroyer"]
        if direction == 'up':
            if row - int(ship_size) >= 0:
                for i in range(0, ship_size):  # check for collision
                    if game_main_field[int(row - i)][int(col) - 1] not in check_ships:
                        pass
                    else:
                        return False
                return True
            else:
                return False
        elif direction == 'down':
            space = row + int(ship_size)
            if space <= 11:
                for i in range(0, ship_size):
                    raw = game_main_field[int(row + i)][int(col) - 1]
                    if raw not in check_ships:
                        pass
                    else:
                        return False
                return True
            else:
                return False
        elif direction == 'right':
            if col + int(ship_size) <= 11:
                for i in range(0, ship_size):
                    if game_main_field[int(row)][int(col) + i - 1] not in check_ships:
                        pass
                    else:
                        return False
                return True
            else:
                return False
        elif direction == 'left':
            if col - int(ship_size) >= 0:
                for i in range(0, ship_size + 1):
                    if game_main_field[int(row)][int(col - 1) - i] not in check_ships:
                        pass
                    else:
                        return False
                return True
            else:
                return False

    def set_ship(self, game_main_field, ship_size, position, ship_type, check_set_space):
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
                                "2. Horizontally"))  # setting a ship
        if orientation == 1:
            direction = int(input("Choose direction: \n"
                                  "1. Up \n"
                                  "2. Down"))
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
            if direction == 1:  # checking for player`s choise
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

    def play_game(self, game_main_field, second_player_field):  # game between players starts
        print("Player 1 starts.")
        player_one_move = True
        player_two_move = False
        check_ships = ["Battleship", "Cruiser", "Submarine", "Destroyer"]
        victory = False
        while True:  # setting main loop for the game
            if player_one_move:
                while not victory:
                    pos = input("Player 1, enter target: ")  # giving player turn for target choise
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
                    if destroyed:  # checking if ship has been destroyed, if yes raising str with warning
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
                    if victory:  # checking for player`s victory
                        print("PLAYER 1 WINS")  # telling about victory and asking if game need to be closed
                        exit_game = str(input())
                        print("Wanna leave game? Y/N ", exit_game)
                        if exit_game == "Y":
                            sys.exit()
                        elif exit_game == "N":
                            print("Thanks for playing, enjoy your day ^^")
                        else:
                            break
                    player_one_move = False
                    player_two_move = True
                    break
            elif player_two_move:
                while not victory:
                    pos = input("Player 2, enter target: ")  # giving player turn for target choise
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
                    if destroyed:  # checking if ship has been destroyed, if yes raising str with warning
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
                    if victory:  # telling about player`s victory
                        print("PLAYER 2 WINS")  # telling about victory and asking if game need to be closed
                        print("Wanna leave game? Y/N ", str(input()))
                        if exit_game == "Y":
                            sys.exit()
                        elif exit_game == "N":
                            print("Thanks for playing, enjoy your day ^^")
                        else:
                            break
                    player_one_move = True
                    player_two_move = False
                    break
game_field()
