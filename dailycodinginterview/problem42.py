def subsetSum(numlist, target, templist, curIndex):
    if sum(templist) == target:
        return templist
    for i in range(curIndex, len(numlist)):
        templist.append(numlist[i])
        if sum(templist) <= target:
            resultlist = subsetSum(numlist, target, templist, i+1)
            if sum(resultlist) == target:
                return resultlist
        templist.pop()
    return templist

print(subsetSum([12, 1, 61, 5, 9, 2], 24, [], 0))
print(subsetSum([3, 34, 4, 12, 5, 2], 9, [], 0))