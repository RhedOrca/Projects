s1 = "asdfffed"
s2 = "zxcvvvkf"

if (len(s1) != len(s2)):
    print ("Instant fail, ya doofus.")


def lexiconer(string):
    outlist = []
    uniques = []
    for char in string:
        if char in uniques:
            outlist.append(uniques.index(char))
        else:
            uniques.append(char)
            outlist.append(uniques.index(char))
    return outlist

print(str(lexiconer(s1)))

print(str(lexiconer(s2)))

if lexiconer(s1) == lexiconer(s2):
    print("There is a one-to-one lexicon.")
else:
    print ("No one-to-one exists.")