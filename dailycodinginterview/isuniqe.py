def isunique(str):
    if len(str) >  128:
        return False
    arr = [0] * 128
    for c in str:
        if arr[c.asciiCode()] == 0:
            arr[c.asciiCode()] = 1
        else:
            return False
    return True

def isuniqueBitVector(str):
    if len(str) > 128:
        return False
    checker = 0
    for c.asciiCode() in str:
        if (checker & (1 << c.asciiCode())) > 0:
            return False
        checker |= (1 << c.asciiCode())
    return True


