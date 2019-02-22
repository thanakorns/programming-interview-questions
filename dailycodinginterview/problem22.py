def wordBreak(s, wordDict):
    opt = [None] * (len(s)+1)
    opt[0] = []
    for i in range(1, len(s)+1):
        for j in range(0, i):
            if opt[j] != None and s[j:i] in wordDict:
                opt[i] = list(opt[j])
                opt[i].append(s[j:i])
                break
    return opt[len(s)]

print(wordBreak("leetcode", ["leet", "code"]))
