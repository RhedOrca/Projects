list1 = []
for num in range(1, 8):
    list1.append(num)

for i in range(1,8):
    outputlist = []
    for num in list1:
        outputlist.append(num * i)
    print (str(outputlist))