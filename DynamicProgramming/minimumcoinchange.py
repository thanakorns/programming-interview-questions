def mc(amount, coinList):
    sol = [0] * (amount+1)
    for i in range(amount+1):
        sol[i] = i
        for coin in coinList:
            if coin <= i:
                tentativeSol = (sol[i - coin] + 1)
                if tentativeSol < sol[i]:
                    sol[i] = tentativeSol
    return sol[amount]

amnt = 63
clist = [1,5,10,21,25]

print(mc(amnt, clist))

