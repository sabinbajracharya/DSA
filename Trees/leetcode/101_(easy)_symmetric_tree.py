# 101. Symmetric Tree - https://leetcode.com/problems/symmetric-tree/description/
# Easy

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Trees.traversal import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftTree = root.left
        rightTree = root.right

        return self.isMirror(leftTree, rightTree)

    def isMirror(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None or left.val != right.val:
            return False

        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

