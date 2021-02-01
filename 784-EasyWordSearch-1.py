from random import randint

dictFile = open("dict.txt", "r")
dictFileContents = dictFile.read()
dictionary = []

word = ''
for letter in dictFileContents:  # Loads dictionary into program
    if letter != '\n':
        word += letter
    else:
        if len(word) < 2:  # omits single letter words. Where's the fun in that?
            word = ''
            continue
        dictionary.append(word)
        word = ''


alphabet = "abcdefghijklmnopqrstuvwxyz"
original = []
xRange = 20
yRange = 20

for x in range(0, xRange):  # generates a 5x5 game board
    row = []
    for y in range(0, yRange):
        randletter = alphabet[randint(0, 25)]
        row.append(randletter)
    original.append(row)

for row in original: # Displays game board.
    print(str(row))

rotatedBoard = []

for x in range(0, len(original)):  # Generates a rotated game board for cleaner logic
    newRow = []
    for y in range(0, len(original)):
        newRow.append(original[y][x])
    rotatedBoard.append(newRow)

boards = [original, rotatedBoard]

success = False
for board in boards:
    for row in board:
        letterString = ""
        for letter in row:
            letterString += str(letter)  # Creates a string from a row for comparison
        for word in dictionary:
            if word in letterString:
                print("!!!" + str(word) + " found in " + str(row) + "!!!")
                success = True

if success:
    close = input("\n\nCongratulations, your game board had a word. You contributed in no way to finding it, but there it is.\n\n\nWell done.")
else:
    close = input("Tough luck mate. No words in the top 1000 today.")