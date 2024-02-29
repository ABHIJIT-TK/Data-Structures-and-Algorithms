def coinChangeWays(coins, n, sum):
    dp = [0] * (sum + 1)
    dp[0] = 1
    
    for i in range(n):
        for j in range(coins[i], sum + 1):
            dp[j] += dp[j - coins[i]]
    
    return dp[sum]

# Example usage
coins = [1, 2, 3]
sum = 5
n = len(coins)
print("Number of ways to make sum:", coinChangeWays(coins, n, sum))
