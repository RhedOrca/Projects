from random import randint

dictFile = open("dict.txt", "r")
dictFileContents = dictFile.read()
dictionary = []
attempts = []
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
def randletter():
    x = alphabet[randint(0, 25)]
    return x


def gridbuilder():  # builds a random game board
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    grid = [l1, l2, l3, l4]

    for row in grid:
        for i in range(0, 4):
            row.append(randletter())

    return grid


grid = gridbuilder()

for row in grid:
    print(str(row))

def adjacentList(coord):  # produces a list of adjacent letters. Fills invalid spaces with '0'.
    y = coord[0]
    x = coord[1]
    up = 0
    down = 0
    left = 0
    right = 0
    if y != 0:
        up = grid[y-1][x]
    if y != 3:
        down = grid[y+1][x]
    if x != 0:
        left = grid[y][x-1]
    if x != 3:
        right = grid[y][x+1]
    output = [up, down, left, right]
    return output

def checker(candidate):  # Checks if a given move will produce a part/whole of a word from the dictionary.
    for word in dictionary:
        if word.startswith(candidate):
            print(str(word).swapcase() + " contains " + str(candidate).swapcase())
            return True
    return False

def boggleSolver(currString, coord):
    print("Testing with (" + currString + ") at " + str(coord))
    usedCoords.append(coord)
    if currString in dictionary:
        attempts.append(currString)
    x = coord[1]
    y = coord[0]
    adjacents = adjacentList(coord)
    if [y-1, x] in usedCoords:
        print("[" + str(y-1) + "," + str(x) + "] should be in " + str(usedCoords))
        adjacents[0] = 0
    if [y+1, x] in usedCoords:
        print("[" + str(y+1) + "," + str(x) + "] should be in " + str(usedCoords))
        adjacents[1] = 0
    if [y, x-1] in usedCoords:
        print("[" + str(y) + "," + str(x-1) + "] should be in " + str(usedCoords))
        adjacents[2] = 0
    if [y, x+1] in usedCoords:
        print("[" + str(y-1) + "," + str(x+1) + "] should be in " + str(usedCoords))
        adjacents[3] = 0
    for i in range(0, 4):
        if adjacents[i] != 0:
            newCoords = []
            if i == 0:
                newCoords.append(y - 1)
                newCoords.append(x)
                print("checking up @ " + str(newCoords))
            if i == 1:
                newCoords.append(y + 1)
                newCoords.append(x)
                print("checking down @ " + str(newCoords))
            if i == 2:
                newCoords.append(y)
                newCoords.append(x - 1)
                print("checking left @ " + str(newCoords))
            if i == 3:
                newCoords.append(y)
                newCoords.append(x + 1)
                print("checking right @ " + str(newCoords))
            newString = currString + adjacents[i]
            if checker(newString):
                boggleSolver(newString, newCoords)  # If checker, generate new coords to give bogglesolver.
    return


for y in range(0, 4):
    for x in range(0, 4):
        usedCoords = []
        print("\n\nNEW START POINT = [" + str(y) + ", " + str(x) + "]:" + str(grid[y][x]))
        boggleSolver(grid[y][x], [y, x])

solutions = []
for attempt in attempts:
    if attempt != None:
        solutions.append(attempt)

if solutions:
    input("\nSolutions found:\n" + str(solutions))
else:
    input("\n\nNo solutions found.")