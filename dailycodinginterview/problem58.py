def findIndex(num_list, target):
    lo = 0
    hi = len(num_list)-1
    while lo < hi:
        mid = int((lo + hi)/2)
        if num_list[mid] == target:
            return mid
        if (mid > 0 and num_list[mid-1] > num_list[mid]) or (mid < len(num_list)-1 and num_list[mid+1] < num_list[mid]):
            if target >= num_list[lo]:
                hi = mid-1
            elif target <= num_list[hi]:
                lo = mid+1
        elif num_list[mid] > target:
            hi = mid-1
        else:
            lo = mid+1
    return None

print(findIndex([13, 18, 25, 2, 8, 10], 8))

