from random import randint

histo = []
def genHistogram(histo):    #generates random histogram
    for i in range(0, 5):
        histo.append(randint(1,10))
    print(str(histo))
genHistogram(histo)
#everything above here generates the array I'm trying to solve

maxArea = 0

for num1 in histo: #starts primary cycle
    print("starting new cycle with " + str(num1))
    currMax = num1
    chain = 0
    maxChain = 1
    for num2 in histo: #starts secondary cycle
        if num2 >= num1:
            chain += 1
        else:
            maxChain = max(chain, maxChain)
            chain = 0

        maxChain = max(chain, maxChain)
        currMax = num1 * maxChain
        print("CurrMax = " + str(currMax))
        maxArea = max(currMax, maxArea)
        print("maxArea = " + str(maxArea))

print(maxArea)
