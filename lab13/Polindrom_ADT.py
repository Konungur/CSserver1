def palindrome_list():
    with open("words.txt", "r") as f:
        data = f.readlines()
    for line in data:
        words = line.split()
        words =