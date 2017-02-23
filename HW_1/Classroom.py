class Classroom(object):
    def __init__(self, number, capacity, stuff):
        self.number = number
        self.capacity = capacity
        self.stuff = stuff

    def is_larger(self, classroom):
        if self.stuff > classroom.stuff:
            return True
        else:
            return False

    def equipment_differences(self, classroom):
        return list(set(self.stuff) - set(classroom.stuff))

    def __str__(self):
        stuff = ''
        for item in self.stuff:
            stuff += item + ', '
        stuff = stuff[:-2]

        return 'Classroom {0} has a capacity of {1} persons and has the' \
               'following equipment: {2}.'.format(self.number, self.capacity,
                                                  stuff)

    def __repr__(self):
        return "Classroom('{0}', {1}, {2})".format(self.number,
                                                   self.capacity,
                                                   self.stuff)
