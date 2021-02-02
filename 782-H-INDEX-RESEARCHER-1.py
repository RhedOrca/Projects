from random import randint

papers = []
for i in range(0, randint(3, 20)):
    papers.append(randint(0, 20))
papers.sort()
papers.reverse()
print(str(papers))
#  Everything above generates the test citation list

for i in range(0, len(papers)):
    if papers[i] <= i:
        input("H-index is " + str(i))
        break


