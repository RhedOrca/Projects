import main

def finalRowFillCheck(root):
    testnode = root
    depth = 1
    while testnode.left:
        testnode = testnode.left
        depth += 1
    print("Depth is " + str(depth))
    unsolved = True
    newRoot = root
    depthRemaining = depth - 1
    numerator = 0
    denominator = 0
    while unsolved:
        if rightCheck(newRoot, depthRemaining):
            testRoot = testRoot.right
            numerator += 1
        else:
            testRoot = testRoot.left
        depthRemaining -= 1
        denominator += 1


def rightCheck(newRoot, depthRemaining):
    testRoot = newRoot.right
    while testRoot.left:
        testRoot = testRoot.left
        depthRemaining -= 1
    if depthRemaining == 0:
        return True
    else:
        return False