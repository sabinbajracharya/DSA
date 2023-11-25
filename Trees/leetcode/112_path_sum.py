# 112. Path Sum - https://leetcode.com/problems/path-sum/description/

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.
# Example 1:

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
from Trees.traversal import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(root, total):
            if root == None:
                return False

            total += root.val

            if root.left == None and root.right == None:
                return total == targetSum

            if traverse(root.left, total):
                return True

            if traverse(root.right, total):
                return True

            return False

        return traverse(root, 0)