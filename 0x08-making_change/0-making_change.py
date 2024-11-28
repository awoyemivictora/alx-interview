#!/usr/bin/python3

def makeChange(coins, total):
    # Edge case: if the total is 0 or negative, no coins are needed
    if total <= 0:
        return 0
    
    # Initialize the dp array where dp[i] represents the minimum number of coins needed to make i
    # We initialize it with a large number (float('inf')) indicating that the value is not yet achievable
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make 0

    # Iterate over all coins and update dp values for amounts from coin to total
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, return -1 as it's impossible to make that amount
    return dp[total] if dp[total] != float('inf') else -1

print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))
