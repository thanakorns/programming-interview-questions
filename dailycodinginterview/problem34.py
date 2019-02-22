def makeShortestPalindrome(str):
    if not str:
        return 0
    dp = []
    for i in range(len(str)):
        dp.append([""] * len(str))

    for i in range(1, len(str)):
        for l, h in zip(range(len(str)-i), range(i, len(str))):
            dp[l][h] = str[l] + dp[l+1][h-2] + str[h] if str[l] == str[h] else (min(str[l]+dp[l+1][h]+str[l], str[h]+dp[l][h-1]+str[h]))

    return dp[0][len(str)-1]

print(makeShortestPalindrome("geeks"))