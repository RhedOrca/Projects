class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

Node1 = Node(1)
N = 5
k = 2

currNode = Node1
for i in range(2, N+1):
    currNode.next = Node(i)
    currNode = currNode.next
currNode.next = Node1

#  Everything above here generates the circular list

currNode = Node1
counter = 1
while currNode.next != currNode:
    counter += 1
    if counter == k:
        print("Killing prisoner " + str(currNode.next.value))
        currNode.next = currNode.next.next
        counter = 1
    currNode = currNode.next
input("Congratulations, prisoner " + str(currNode.value) + ".")