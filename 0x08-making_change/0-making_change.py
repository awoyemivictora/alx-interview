#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Create a dp array where dp[i] will be the minimum number of coins needed to make i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0 # No coins are needed to make 0


    # Iterate through each coin
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    
    # If dp[total] is still infinity, return -1, meaning it's not possible to form the total
    return dp[total] if dp[total] != float('inf') else -1

print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))