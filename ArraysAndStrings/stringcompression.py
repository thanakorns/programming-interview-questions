def stringcompression(input):
    compressedStr = []
    sameCharacterCount = 0
    for i in range(len(input)-1):
        sameCharacterCount += 1
        if input[i] != input[i+1]:
            compressedStr.append(input[i])
            compressedStr.append(str(sameCharacterCount))
            sameCharacterCount = 0
    sameCharacterCount += 1
    compressedStr.append(input[len(input)-1])
    compressedStr.append(str(sameCharacterCount))
    newString = ''.join(compressedStr)
    print(newString)
    return newString if len(newString) < len(input) else input


print(stringcompression("aabcccccaaa"))


