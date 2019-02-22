def weaveLists(l1, l2, prefix):
    if len(l1) == 0:
        return prefix.copy().extend(l2)
    if len(2) == 0:
        return prefix.copy().extend(l1)
    result = []

    newl1 = l1.copy()
    popped = newl1.pop(0)
    newPref1 = prefix.copy().add(popped)
    result.extend(weaveLists(newl1, l2, newPref1))


    newl2 = l2.copy()
    popped = newl2.pop(0)
    newPref2 = prefix.copy().add(popped)
    result.extend(weaveLists(l1, newl2, newPref2))

    return result


def weaveLists(l1, l2, prefix):
    if len(l1) == 0 or len(l2) == 0:
        return prefix.copy().extend(l2).extend(l1)
    result = []

    popped = l1.copy().pop(0)
    newPref1 = prefix.copy().add(popped)
    result.extend(weaveLists(l1, l2, prefix))

    popped = l2.copy().pop(0)
    newPref2 = prefix.copy().add(popped)
    result.extend(weaveLists(l1, l2, prefix))

    return result


