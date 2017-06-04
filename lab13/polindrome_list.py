from arraystack import ArrayStack
from abstractcollection import AbstractCollection

class PolindromeChecker(ArrayStack):
    def __init__(self, fiel):
        self.fiel = fiel

    def reader(self):
        """
        This method reads words from vocab, and returns a list of these words
        """
        lstfiel = open(self.fiel, 'r')
        lst = []
        for i in lstfiel.readlines():
            i = i.lower()
            lst.append(i)
        return lst

    def finding(self):
        """
        This method finds all polindromes in curent vocab, and return list of polindromes
        """
        s = ArrayStack()
        polindrom = False
        list_polindrom = []

        def polindrom_checker(str):
            firstpart, secondpart = str[:len(str)//2], str[len(str)//2:]
            for i in firstpart:
                s.add(i)
            for i in secondpart:
                if s.pop() != i:
                    polindrom = False
                    s.clear()
                    break
                else:
                    polindrom = True
            if polindrom == True:
                return firstpart + secondpart

        for i in [i[:-1] for i in self.reader()]:
            if len(i) % 2 == 0:
                if polindrom_checker(i) != None:
                    list_polindrom.append(polindrom_checker(i))
            else:
                first, second = i[:len(i)//2], i[len(i)//2:]
                first = first + second[0]
                i = first + second
                polindrom_checker(i)
                if polindrom_checker(i) != None:
                    first, second = polindrom_checker(i)[:len(polindrom_checker(i))//2], polindrom_checker(i)[len(polindrom_checker(i))//2:]
                    first = first[:-1]
                    word = first + second
                    list_polindrom.append(word)

        return list_polindrom

    def writing(self):
        """
        This method writes all polindromes into fiel.txt
        """
        with open('palindrome_en.txt', 'w') as f:
            for i in self.finding():
                f.write(i + '\n')

p = PolindromeChecker('words.txt')
print(p.finding())

