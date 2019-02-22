def findInvesions(numlist):
    numlist_tuple = (numlist, 0)
    return mergeSort(numlist_tuple)[1]


def mergeSort(numlist_tuple):
    if len(numlist_tuple[0]) <= 1:
        return numlist_tuple
    # print(numlist_tuple)
    numlist = numlist_tuple[0]
    mid = int(len(numlist)/2)
    l1 = numlist[:mid]
    l2 = numlist[mid:]
    l1_tuple = (l1, 0)
    l2_tuple = (l2, 0)
    sorted_l1_tuple = mergeSort(l1_tuple)
    sorted_l2_tuple = mergeSort(l2_tuple)
    result_tuple = merge(sorted_l1_tuple , sorted_l2_tuple)
    return result_tuple

def merge(l1_tuple, l2_tuple):
    l1 = l1_tuple[0]
    l2 = l2_tuple[0]
    inversionCount = l1_tuple[1] + l2_tuple[1]
    result_list = []
    while l1 or l2:
        if l1 and l2:
            if l2[0] < l1[0]:
                result_list.append(l2.pop(0))
                inversionCount += len(l1)
            else:
                result_list.append(l1.pop(0))
        elif l1:
            result_list.append(l1.pop(0))
        elif l2:
            result_list.append(l2.pop(0))
    print(result_list)
    return (result_list, inversionCount)

print(findInvesions([5, 4, 3, 2, 1]))