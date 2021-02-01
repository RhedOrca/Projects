from random import randint

input = []
inputCap = randint(3, 10)
for i in range(0, inputCap):
    input.append(randint(-10, 10))
print(str(input))
#the above generates the list for testing


if len(input) < 3:
    exit("There aren't even three integers, you muffin.")

output = 0

negIn = []
posIn = []

for num in input:
    if num < 0:
        negIn.append(num)
    else:
        posIn.append(num)
    negIn.sort()
    posIn.sort()
    posIn.reverse()

print("Negatives are " + str(negIn))
print("Positives are " + str(posIn))
potentials = []

if len(posIn) > 2:
    potentials.append(posIn[0] * posIn[1] * posIn[2]) #allpos
if len(negIn) > 2:
    potentials.append(negIn[len(negIn)-1] * negIn[len(negIn)-2] * negIn[len(negIn)-3]) #allneg
if len(negIn) > 1 and len(posIn) > 0:
    potentials.append(negIn[0] * negIn[1] * posIn[0]) #negsplit
if len(negIn) > 0 and len(posIn) > 1:
    potentials.append(posIn[len(posIn)-1] * posIn[len(posIn)-2] * negIn[len(negIn)-1]) #possplit


output = max(potentials)
print(str(potentials))
print(str(output) + " is the largest multiple.")