def problem2(numlist):
    productFromLeft = list(numlist)
    productFromRight = list(numlist)
    ans = [1] * len(numlist)
    last_index = len(numlist)-1
    for i in range(1, len(numlist)):
        productFromLeft[i] *= productFromLeft[i-1]
        productFromRight[last_index-i] *= productFromRight[last_index-i+1]
    for i in range(len(numlist)):
        if i - 1 >= 0:
            ans[i] *= productFromLeft[i-1]
        if i + 1 <= last_index:
            ans[i] *= productFromRight[i+1]
    return ans

ans = problem2([1, 2, 3, 4, 5])
print(ans)

