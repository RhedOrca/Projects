class Node:

    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

class Quack:
    dummyHeader = Node(0)

    def push(self, dummyHeader, data):
        node = Node(data)
        node.prev = dummyHeader
        node.next = dummyHeader.next
        dummyHeader.next = node



    def pop(self):


    def pull(self):




    def printTree(self):
        print(self.data)