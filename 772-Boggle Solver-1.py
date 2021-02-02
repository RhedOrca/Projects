from random import randint
alphabet = "abcdefghijklmnopqrstuvwxyz"

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

def randletter():
    x = alphabet[randint(0, 25)]
    return x


def gridbuilder():
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

def adjacentList(coord):
    y = coord[0]
    x = coord[1]
    up = 0
    down = 0
    left = 0
    right = 0
    if x != 0:
        up = grid[x-1][y]
    if x != 3:
        down = grid[x+1][y]
    if y != 0:
        left = grid[x][y-1]
    if y != 3:
        right = grid[x][y+1]
    output = [up, down, left, right]

    return output

def checker(candidate):
    for word in dictionary:
        if candidate in word:
            return True
    return False

def boggleSolver(currString, coord):
    if currString in dictionary:
        attempts.append(currString)
        return
    x = coord[1]
    y = coord[0]
    candidates = []
    adjacents = adjacentList(coord)
    if [y, x-1] in usedCoords:
        adjacents[0] = 0
    if [y, x+1] in usedCoords:
        adjacents[1] = 0
    if [y-1, x] in usedCoords:
        adjacents[2] = 0
    if [y+1, x-1] in usedCoords:
        adjacents [3] = 0
    for adjacent in adjacents:
        if adjacent == 0:
            continue
        else:
            candidates.append(currString + adjacent)
    for candidate in candidates:
        if checker(candidate):
            boggleSolver(candidate, coord)
        else:
            currString = ''
            break
    return



usedCoords = []
for x in range(0, 4):
    for y in range(0, 4):
        usedCoords = []
        boggleSolver(grid[y][x], [x, y])

solutions = []
for attempt in attempts:
    if attempt != None:
        solutions.append(attempt)

if solutions:
    input("\nSolutions found:\n" + str(solutions))
else:
    input("No solutions found.")