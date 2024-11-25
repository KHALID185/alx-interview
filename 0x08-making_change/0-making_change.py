#!/usr/bin/python3
"""
Coin Change Algorithm: Minimum Coins Needed
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins to meet a total amount.

    Args:
        coins (list): Available coin denominations
        total (int): Target total amount

    Returns:
        int: Fewest number of coins needed, or -1 if impossible
    """
    # Handle base cases
    if total <= 0:
        return 0

    # Initialize dynamic programming table
    # dp[i] stores minimum coins needed for amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Compute minimum coins for each amount
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return result, -1 if impossible to make total
    return dp[total] if dp[total] != float('inf') else -1
