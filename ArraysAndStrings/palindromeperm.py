def isPermutationOfPalidrome(str):
    str = str.lower().replace(" ", "")
    print(str)
    table = dict.fromkeys(str, 0)
    print(table)
    oddCount = 0
    for c in str:
        table[c] += 1
        if table[c] % 2 == 1:
            oddCount += 1
        else:
            oddCount -= 1
    return oddCount <= 1


def isPermutationOfPalindrome2(str):
    str = str.lower().replace(" ", "")
    checker = 0
    for c in str:
        checker ^= (1 << ord(c))
    return (checker & (checker - 1)) == 0





print(isPermutationOfPalindrome2("Tact Coa"))