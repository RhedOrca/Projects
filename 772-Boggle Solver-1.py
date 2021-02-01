from random import randint
alphabet = "abcdefghijklmnopqrstuvwxyz"
library = ["at", "by", "cat", "as", "ex", "but", "be", "no", "um", "is", "me", "si", "or", "im", "to", "go", "am", "ba", "be", "id", "if", "in", "is", "gi"]

def randletter():
    x = alphabet[randint(0, 25)]
    return x


def gridbuilder():
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    LoL = [l1, l2, l3, l4]

    for innerlist in LoL:
        for i in range(0, 4):
            innerlist.append(randletter())

    print(str(LoL))
    for innerlist in LoL:
        print(str(innerlist))

    navigablelist = []
    for innerlist in LoL:
        for item in innerlist:
            navigablelist.append(item)

    return navigablelist


def wordcheck(attempt, library, index, navigablelist, nogo):
    for word in library:
        if str(attempt) == word[:len(attempt)]:
            nogo.append(index)
            print("Comparing " + str(attempt) + " to " + str(word) + ".")
            if str(attempt) == word:
                print ("!!!Solution found: " + str(attempt) + "!!!")
                return True
            else:
                up = index - 4
                down = index + 4
                left = index - 1
                right = index + 1
                if up >= 0 and up < len(navigablelist) and wordcheck(attempt + navigablelist[up], library, up, navigablelist, nogo):
                    return True
                if down >= 0 and down < len(navigablelist) and wordcheck(attempt + navigablelist[down], library, down, navigablelist, nogo):
                    return True
                if left >= 0 and left < len(navigablelist) and wordcheck(attempt + navigablelist[left], library, left, navigablelist, nogo):
                    return True
                if right >= 0 and right < len(navigablelist) and wordcheck(attempt + navigablelist[right], library, right, navigablelist, nogo):
                    return True
    return False


def bogglesolver():
    navigablelist = gridbuilder()
    print (str(navigablelist))
    i = 0
    for letter in navigablelist:
        nogo = [i]
        i += 1
        if wordcheck(letter, library, 0, navigablelist, nogo):
            print("Solution found. Have a nice day.")


#def nextLetterCheck(nogo, attempt):
    #give list of non-viable moves, run wordcheck on each move, if successful call nextLetterCheck on that position


bogglesolver()