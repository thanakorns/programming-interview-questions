import random

def pickElementFromStream(stream):
    picked = None

    for i, element in enumerate(stream):
        if i == 0:
            picked = element
        #    prob of current element being chosen with i+1 elements processed so far of is 1/(i+1)
        elif random.randint(1, i+1) == 1:
            picked = element
    return picked

