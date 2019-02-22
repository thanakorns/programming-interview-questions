# def URLify(str, length):
#     firstIndex = 0
#     for c in str:
#         if c != " ":
#             break
#         firstIndex += 1
#     str = str[firstIndex: firstIndex+length]
#     str = str.replace(" ", "%20")
#     return str

def URLify(str, truelength):
    spaceCount = 0
    for i in range(truelength):
        if str[i] == ' ':
            spaceCount += 1
    index = truelength - spaceCount + (spaceCount * 3)
    for i in range(truelength-1, -1, -1):
        if str[i] == " ":
            str[index-1] = '0'
            str[index-2] = '2'
            str[index-3] = '%'
            index -= 3
        else:
            str[index-1] = str[i]
            print(str[i])
            index -= 1

    return str[index:truelength - spaceCount + (spaceCount * 3)]

listString = list("Mr John Smith                                         ")
# print(listString)
print(URLify(listString, 13))
