def minimalTree(arr):
    low = 0
    high = len(arr)-1
    return minimalTreeHelper(arr, low, high)


def minimalTreeHelper(arr, low, high):
    if (low > high):
        return None
    mid = (low+high)/2
    currentNode = Node(arr[mid])
    currentNode.left = minimalTreeHelper(arr, low, mid-1)
    currentNode.right = minimalTreeHelper(arr, mid+1, high)
    return currentNode


