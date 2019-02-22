def stringRotate(rotatedString, targetString):
    if len(rotatedString) != len(targetString):
        return False
    newString = rotatedString + rotatedString
    targetIndex = 0
    for c in newString:
        if c == targetString[targetIndex]:
            targetIndex += 1
            if targetIndex == len(targetString):
                return True
        else:
            targetIndex = 0
    return False


print(stringRotate("erbottlewat", "waterbottle"))

