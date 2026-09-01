# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        reverse_binary_tree(root)

        return root

    
def reverse_binary_tree(root: Optional[TreeNode]):
    if root is None:
        return None
    
    if root.left is None and root.right is None:
        return root
    
    original_left = root.left

    root.left = root.right
    root.right = original_left

    reverse_binary_tree(root.left)
    reverse_binary_tree(root.right)
   
        