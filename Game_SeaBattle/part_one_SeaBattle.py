import random


def read_file():
    """
    (str)->(data)
    """
    with open('field.txt') as f:
        data = f.read().splitlines()
        return data


def has_ship(data, coordinates, field):
    """
    (data, tuple)->(bool)
    """
    cor = []
    for i in range(len(data)):
        for j in range(1, len(data[i]) + 1):
            cor.append((chr(65 + i), j, data[i][j - 1]))
    for i in field:
        if (i[0], i[1]) == coordinates:
            return i[2], cor
    if has_ship(data, coordinates, field) == "*":
        return True, cor
    else:
        return False, cor


def get_right(pos):
    col, row = pos
    index = col.index(col)
    if index == 9:
        return None
    else:
        return col[index + 1], row


def get_left(pos):
    col, row = pos
    index = col.index(col)
    if index == 0:
        return None
    else:
        return col[index - 1], row


def get_down(pos):
    col, row = pos
    index = row.index(row)
    if index == 9:
        return None
    else:
        return col, row[index + 1]


def get_up(pos):
    col, row = pos
    index = row.index(row)
    if index == 0:
        return None
    else:
        return col, row[index - 1]


def ship_size(data, pos):
    """
    (data, tuple) -> (tuple)
    """
    if has_ship(data, pos):
        size = 1
    else:
        return 0
    direction = 'N'
    if get_left(pos):
        if has_ship(data, get_left(pos)):
            direction = 'H'
    if get_right(pos):
        if has_ship(data, get_right(pos)):
            direction = 'H'
    if get_up(pos):
        if has_ship(data, get_up(pos)):
            direction = 'V'
    if get_down(pos):
        if has_ship(data, get_down(pos)):
            direction = 'V'
    if direction == 'N':
        return size
    col, row = pos
    if direction == 'H':
        while get_left((col, row)) and has_ship(data, get_left((col, row))):
            col, row = get_left((col, row))
        while get_right((col, row)) and has_ship(data, get_right((col, row))):
            col, row = get_right((col, row))
            size += 1
    else:
        while get_up((col, row)) and has_ship(data, get_up((col, row))):
            col, row = get_up((col, row))
        while get_down((col, row)) and has_ship(data, get_down((col, row))):
            col, row = get_down((col, row))
            size += 1
    return size


def is_valid(cor):
    """
    (data)->(bool)
    """
    if len(cor) < 99:
        return False
    elif cor.count("*") < 20:
        return False
    else:
        return True


def field_to_str(cor):
    """
    (data)->(str)
    """
    results_of_game = cor
    my_string = '_'.join(results_of_game)
    file = open('results_of_game.txt', 'w')
    for i in my_string:
        file.write(i + '\n')
    file.close()
    file_check = open('results_of_game.txt', 'r')
    l = [line.strip() for line in file_check]
    file_check.close()
    return l


def generate_field():
    """
    ()->(data)
    """
    field = []
    for x in range(10):
        field.append(["-"] * 10)
    for row in field:
        print(" ".join(row))
    random_row = random.randint(0, len(field) - 1)
    random_col = random.randint(0, len(field[0]) - 1)
    return [random_col, random_row]
