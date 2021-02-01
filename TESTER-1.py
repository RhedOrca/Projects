from random import randint
xList = []
yList = []
print("How many questions?")
attempts = int(input())
for i in range(attempts):
    xList.append(randint(1, 15))
    yList.append(randint(1, 15))

correct = 0
for i in range(len(xList)):
    operator = randint(1, 3)
    if operator == 1:
        print(str(xList[i]) + " + " + str(yList[i]) + " = ?")
        answer = int(input())
        if answer == xList[i] + yList[i]:
            correct += 1
    elif operator == 2:
        print(str(xList[i]) + " - " + str(yList[i]) + " = ?")
        answer = int(input())
        if answer == xList[i] - yList[i]:
            correct += 1
    else:
        print(str(xList[i]) + " * " + str(yList[i]) + " = ?")
        answer = int(input())
        if answer == xList[i] * yList[i]:
            correct += 1
print("You scored " + str(correct) + "/" + str(attempts) + ". " + str(correct/attempts*100) + "%.")
