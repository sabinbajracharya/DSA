# 236. Lowest Common Ancestor of a Binary Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Medium

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Trees.traversal import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def traverse(root):
            if not root:
                return None

            if root.val == p.val or root.val == q.val:
                return root

            node_A = traverse(root.left)
            node_B = traverse(root.right)

            if node_A and node_B:
                return root
            else:
                return node_A or node_B


        return traverse(root)

            # if not root:
            #     return None, False

            # if root.val == p.val or root.val == q.val:
            #     return root, False

            # node_A, is_done = traverse(root.left)
            # if is_done:
            #     return node_A, True

            # node_B, is_done = traverse(root.right)
            # if is_done:
            #     return node_B, True

            # if node_A and node_B:
            #     return root, True

            # return node_A or node_B, False
        # return traverse(root)[0]


