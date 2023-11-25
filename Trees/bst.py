from traversal import TreeNode, in_order_traversal, level_order_traversal, post_order_traversal, pre_order_traversal

class BST:
  def insert(self, root, value):
    if root == None:
      return TreeNode(value)

    if value < root.value:
      root.left = self.insert(root.left, value)
    else:
      root.right = self.insert(root.right, value)

    return root

  def delete(self, root, value):
    if not root:
      return root

    if value < root.value:
      root.left = self.delete(root.left, value)
    elif value > root.value:
      root.right = self.delete(root.right, value)
    else:
      # Node with one child or no child
      if not root.left:
        return root.right
      elif not root.right:
        return root.left

      # Node with two children
      # Find the small node from the root's right and replace the root
      root.value = self.min_val(root.right)

      # Delete that smallest node from the root's right
      root.right = self.delete(root.right, root.value)
      return root

    return root


  def min_val(self, node):
    while node and node.left:
      node = node.left
    return node.value

  def search(self, root, value):
    if not root or root.value == value:
      return root

    if value < root.value:
      return self.search(root.left, value)
    else:
      return self.search(root.right, value)


    # Create a BST:
#       4
#      / \
#     2   6
#    / \ / \
#   1  3 5  7

bst = BST()
root = None
values_to_insert = [4, 2, 6, 1, 3, 5, 7]

for value in values_to_insert:
  root = bst.insert(root, value)

# Example usage:
print("In-Order Traversal:", in_order_traversal(root))
print("Pre-Order Traversal:", pre_order_traversal(root))
print("Post-Order Traversal:", post_order_traversal(root))
print("BFS Traversal:", level_order_traversal(root))

# Search for a value:
search_value = 3
result_node = bst.search(root, search_value)
print(f"Search for {search_value}: {'Found' if result_node else 'Not Found'}")

# Delete a value:
delete_value = 2
root = bst.delete(root, delete_value)
print(f"Deleted node with value {delete_value}")
print("In-Order Traversal after deletion:", in_order_traversal(root))
print("BFS Traversal:", level_order_traversal(root))
