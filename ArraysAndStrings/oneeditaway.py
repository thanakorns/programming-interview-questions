def oneeditaway(str1, str2):
    if len(str1) == len(str2):
        return checkReplacement(str1, str2)
    elif len(str1) + 1 == len(str2):
        return checkInsert(str1, str2)
    elif len(str2) + 1 == len(str1):
        return checkInsert(str2, str1)
    else:
        return False

def checkReplacement(str1, str2):
    diffCount = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diffCount += 1
            if diffCount > 1:
                return False
    return True

def checkInsert(str1, str2):
    index1 = 0
    index2 = 0
    while((index1 < len(str1)) and (index2 < len(str2))):
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


print(oneeditaway("pale", "ple"))
print(oneeditaway("pale", "pales"))
print(oneeditaway("pale", "bale"))
print(oneeditaway("pale", "bae"))

