# 494. Target Sum
# Medium

# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.


# Example 1:
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3

# Example 2:
# Input: nums = [1], target = 1
# Output: 1

from ast import List

class Solution:
  def findTargetSumWays(self, nums: List[int], target: int) -> int:
    memo = {}
    def findTarget(sub_nums, num):
      arr_len = len(sub_nums)
      if (num, arr_len) in memo:
        return memo[(num, arr_len)]

      if arr_len == 0:
        return 1 if num == target else 0

      for item in sub_nums:
        res = findTarget(sub_nums[1::], num + item) + findTarget(sub_nums[1::], num - item)
        memo[(num, arr_len)] = res
        return res

    return findTarget(nums, 0)