def read_file():
    """
    (str)->(data)
    """
    with open('field.txt') as f:
        data=f.read().splitlines()
        return data

def has_ship(data, coordinates, field):
    """
    (data, tuple)->(bool)
    """
    print(data, coordinates, field)
    cor=[]
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

def ship_size():
    """
    (data, tuple)->(tuple)
    """

def is_valid(cor):
    """
    (data)->(bool)
    """
    if len(cor) < 99:
        return False
    elif cor.count("*")<20:
        return False
    else:
        return True

def field_to_str(cor):
    """
    (data)->(str)
    """
    results_of_game=cor
    my_string='_'.join(results_of_game)
    file = open('results_of_game.txt', 'w')
    for i in my_string:
        file.write(i + '\n')
    file.close()
    file_check=open('results_of_game.txt', 'r')
    l = [line.strip() for line in file_check]
    file_check.close()

def generate_field():
    """
    ()->(data)
    """
    field=[]
    for x in range(10):
        field.append(["-"] * 10)
    for row in field:
        print (" ".join(row))
    random_row=randint(0, len(field) - 1)
    random_col=randint(0, len(field[0]) - 1)
