def next_index(i, n):
    return 2*i if i < n/2 else 2*i - n + 1

def swap(i, nextIndex, nums):
    temp = nums[nextIndex]
    nums[nextIndex] = nums[i]
    nums[i] = temp


def inplace_swap(nums):
    visited = set()
    for i in range(len(nums)):
        nextIndex = next_index(i, len(nums))
        if nextIndex not in visited:
            while nextIndex != i:
                visited.add(nextIndex)
                swap(i, nextIndex)
                nextIndex = next_index(nextIndex, len(nums))
    return nums


