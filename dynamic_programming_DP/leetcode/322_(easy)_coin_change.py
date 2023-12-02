# 322. Coin Change

# Companies
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0


# This solution starts with the coin and then keeps on adding number until its equal to the amount or greater
class Solution1:
  def coinChange(self, coins, amount) -> int:
    if amount == 0:
      return 0

    cache = {}
    def flip(num):
      if num in cache:
        return cache[num]

      if (num == amount):
        return 0
      elif (num > amount):
        return float('inf')

      min_coins = float('inf')
      for coin in coins:
        min_coins = min(min_coins, 1 + flip(num + coin))

      cache[num] = min_coins
      return min_coins

    total = float('inf')
    for coin in coins:
      total = min(total, 1 + flip(coin))
    return -1 if total == float('inf') else total


# This solution starts from the amount and starts subtracting until its zero or negative
class Solution2:
  def coinChange(self, coins, amount) -> int:
    # Memoization dictionary to store already computed results
    memo = {}

    def helper(amount):
      # If the amount is zero, no coins are needed
      if amount == 0:
        return 0

      # If the amount is negative, it is not possible to make change
      if amount < 0:
        return float('inf')

      # If the result for the current amount is already computed, return it
      if amount in memo:
        return memo[amount]

      # Try all possible coin denominations and choose the minimum
      min_coins = float('inf')
      for coin in coins:
        min_coins = min(min_coins, 1 + helper(amount - coin))

      # Memoize the result and return it
      memo[amount] = min_coins
      return min_coins

    # Call the helper function with the given amount
    result = helper(amount)

    # If the result is still infinity, it means it's not possible to make change
    return -1 if result == float('inf') else result