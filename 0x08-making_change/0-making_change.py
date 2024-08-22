def makeChange(coins, total):
    # If the total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # Initialize the dp array with a large value (inf)
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins are needed to make 0 total
    dp[0] = 0

    # Iterate over all amounts from 1 to total
    for i in range(1, total + 1):
        # Check each coin
        for coin in coins:
            if coin <= i:
                """Only consider coins that are less than or
                    equal to the current amount """
                dp[i] = min(dp[i], dp[i - coin] + 1)

    """ If dp[total] is still infinity, that means the total
        cannot be met with the given coins """
    return dp[total] if dp[total] != float('inf') else -1
