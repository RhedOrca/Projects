import random
counter = 0
bestofsetlist = []
while counter < 1000:
    rollset = []
    while len(rollset) < 4:
        rollset.append(random.randint(1, 100))
    bos = 100
    for roll in rollset:
        if roll < bos:
            bos = roll
    bestofsetlist.append(bos)
    print(rollset)
    counter += 1
print(bestofsetlist)
sum = 0
max = 0
for num in bestofsetlist:
    sum += num
    if num > max:
        max = num
avgroll = sum/len(bestofsetlist)
print("average roll is " + str(avgroll))
print("Highest Best of set roll was " + str(max))