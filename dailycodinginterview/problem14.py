import random

def estimatePi(interval):
    circlePoints = 0
    squarePoints = 0
    for i in range(interval*interval):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        d = x*x + y*y
        if d <= 1:
            circlePoints += 1
        squarePoints += 1
        pi = 4 * (circlePoints / squarePoints)
    return pi

print(round(estimatePi(100), 3))
