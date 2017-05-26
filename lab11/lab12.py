class Node:
    def __init__(self, content):
        self.next = None
        self.content = content

    def __str__(self):
        return "<>"

if __name__ == "__main__":
    n = Node("Apple")
    print(n)