from collections import deque

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def in_order_traversal(root):
  result = []

  def traverse(node):
    if node == None:
      return

    traverse(node.left)
    result.append(node.value)
    traverse(node.right)

  traverse(root)
  return result

def pre_order_traversal(root):
  result = []

  def traverse(node):
    if node == None:
      return
    result.append(node.value)
    traverse(node.left)
    traverse(node.right)

  traverse(root)
  return result

def post_order_traversal(root):
  result = []

  def traversal(node):
    if node == None:
      return

    traversal(node.left)
    traversal(node.right)
    result.append(node.value)

  traversal(root)
  return result

def level_order_traversal(root):
  result = []

  if root is None:
    return result

  queue = deque([root])

  while queue:
    node = queue.popleft()
    result.append(node.value)

    if node.left:
      queue.append(node.left)

    if node.right:
      queue.append(node.right)

  return result


# Create a binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Example usage:
print("In-Order Traversal:", in_order_traversal(root))
print("Pre-Order Traversal:", pre_order_traversal(root))
print("Post-Order Traversal:", post_order_traversal(root))
print("Level-Order Traversal:", level_order_traversal(root))

# Output
# In-Order Traversal: [4, 2, 5, 1, 3]
# Pre-Order Traversal: [1, 2, 4, 5, 3]
# Post-Order Traversal: [4, 5, 2, 3, 1]
# Level-Order Traversal: [1, 2, 3, 4, 5]
