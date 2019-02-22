#if two strings contain unique characters
def checkPerm(str1, str2):
    bitVector1 = 0
    bitVector2 = 0
    for c in str1:
        bitVector1 |= 1 << c.ascii()
    for c in str2:
        bitVector2 |= 1 << c.ascii()
    return (bitVector1 | bitVector2 ) == bitVector1

def checkPerm(str1, str2):
    if len(str1) != len(str2):
        return False
    characters = [0] * 128
    for c in str1:
        characters[c.ascii()] += 1
    for c in str2:
        characters[c.ascii()] -= 1
        if characters[c.ascii()] < 0:
            return False
    return True



