#with negative
def problem9(numlist):
    opt = list(numlist)
    for i in range(1, len(numlist)):
        if i == 1:
            opt[i] = max(opt[i-1], opt[i])
        else:
            opt[i] = max(opt[i], opt[i] + opt[i-2], opt[i-1])
    return opt[len(numlist)-1]

# non-negative
def max_sum(arr):
    prevOne, prevTwo, res = 0,0,0
    for i in range(len(arr)):
        if i == 0:
            res = arr[0]
        elif i == 1:
            res = max(arr[0], arr[1])
        else:
            res = max(prevOne, arr[i] + prevTwo)
        prevTwo = prevOne
        prevOne = res
    return res

print(problem9([2, 4, 6, 2, 5]))
print(problem9([5, 1, 1, 5]))
print(problem9([-1,-1,-1,-1,-1,5,-1,-1,-1]))

print(max_sum([2, 4, 6, 2, 5]))
print(max_sum([5, 1, 1, 5]))
print(max_sum([-1,-1,-1,-1,-1,5,-1,-1,-1]))

