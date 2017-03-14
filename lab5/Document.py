class Document:
    def __init__(self):
        """setting var`a"""
        self.characters = []
        self.cursor = 0
        self.filename = ""

    def insert(self, character):
        """checking for cursor move"""
        self.characters.insert(self.cursor, character)
        self.cursor += 1

    def delete(self):
        del self.characters[self.cursor]

    def save(self):
        """saving readed information"""
        f = open(self.filename, "w")
        f.write(''.join(self.characters))
        f.close()

    def forward(self):
        """cursor move`s forward"""
        try:
            self.cursor += 1
        except EOFError:
            print("EndOfFileError")


    def back(self):
        """cursor move`s backward"""
        try:
            self.cursor -= 1
        except Exception:
            print("OutOfFile")



class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def home(self):
        while self.document.characters[
                    self.position - 1] != '\n':
            self.position -= 1
            if self.position == 0:  # Got to beginning of file before newline
                break

    def end(self):
        """checking for the end file"""
        while self.position < len(self.document.characters
                                  ) and self.document.characters[
            self.position] != '\n':
            self.position += 1


class Character:
    def __init__(self, character,
                 bold=False, italic=False, underline=False):
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        """returning characters"""
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character
