# dp[i][j] = max(dp[i-1][j] , dp[i][j-prices[i]] + 1)
import math

def budgetShopping(n, bundleQuantities, bundleCosts):
    cq = sorted(zip(bundleCosts, bundleQuantities))
    quantities = [q for c, q in cq]
    costs = [c for c, q in cq]
    dp = []
    for i in range(n+1):
        dp.append([0]*(len(quantities)+1))
    for i in range(1, n+1):
        for j in range(1, len(quantities)+1):
            dp[i][j] = max(dp[i % costs[j-1]][j-1] + math.floor(i/costs[j-1])*quantities[j-1], dp[i][j-1])
    return dp[n][len(quantities)]


print(budgetShopping(10, [3, 6, 6, 10], [2, 2, 2, 10]))
print(budgetShopping(50, [20, 19], [24, 20]))