'''
You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
'''
def minimum_step_to_destination(sequence):
    minimumStep = 0
    for i in range(len(sequence)-1):
        x, y = sequence[i]
        x1, y1 = sequence[i+1]
        minimumStep += max(abs(x-x1), abs(y-y1))
    return minimumStep

print(minimum_step_to_destination([(0, 0), (1, 1), (1, 2)]))
print(minimum_step_to_destination([(4, 6), (1, 2), (4, 5), (10, 12)]))
