import random
cycle = 0
maxProfit = 1000
while maxProfit > 200:
    stockPrices = []
    while len(stockPrices) < 10:
        stockPrices.append(random.randint(1, 1000))
    print(stockPrices)
    maxProfit = 0
    maxProfitProof = ""
    i = 0
    while i < len(stockPrices)-1:
        j = i + 1
        while j < len(stockPrices):
            potentialProfit = stockPrices[j]-stockPrices[i]
            if potentialProfit > maxProfit:
                maxProfit = potentialProfit
                print("New potential max profit: " + str(maxProfit))
                maxProfitProof = str(potentialProfit)+" found at " + str(stockPrices[i]) + " to " + str(stockPrices[j])
            j = j+1
        i=i+1
    print(maxProfitProof)
    cycle += 1
print("Sub-200 profit found after " + str(cycle) + " cycles.")

