# 300. Longest Increasing Subsequence
# Medium

# Given an integer array nums, return the length of the longest strictly increasing
# subsequence.

# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def update(num_index, next_index):
          if next_index >= len(nums):
            return 0

          num = nums[num_index]
          if (num, num_index)  in memo:
            return memo[(num, num_index)]

          bigger = 0
          for index in range(next_index, len(nums)):
            item = nums[index]

            if (item > num):
              res = 1 + update(index, index + 1)
              bigger = max(bigger, res)
              # There can be multiple value for the same item
              # Add the value that is the maximum
              # 5->6->7->12 and 5->6->12 so 6 can have two different results but we care only of the maxium
              memo[(num, num_index)] = bigger
          return bigger


        bigger = 0
        for index, num in enumerate(nums):
          bigger = max(bigger, 1 + update(index, index + 1))
        return bigger