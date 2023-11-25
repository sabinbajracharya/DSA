# 104. Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Easy

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
from Trees.traversal import TreeNode

class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:

    def traverse(root, current_depth, max_depth):
      if not root:
        return max(max_depth, current_depth)

      current_depth += 1

      max_depth = traverse(root.left, current_depth, max_depth)
      max_depth = traverse(root.right, current_depth, max_depth)
      return max_depth

    return traverse(root, 0, 0)