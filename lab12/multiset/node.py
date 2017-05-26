# A class implementing a node.

class Node:

    def __init__(self, item, next = None):
        """
        Produces a newly constructed empty node.
        __init__: Any -> Node
        Fields: item stores any value
            next points to the next node in the list
        """
        self.item = item
        self.next = next

    def __str__(self):
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        print_def = str(self.item)
        print(print_def)
        return str(self.item)

