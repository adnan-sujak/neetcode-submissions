# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, node: Optional[TreeNode], k: int) -> int:

        smallest = []

        def dfs(node: TreeNode):
            if node is None:
                return

            dfs(node.left) # visit smaller values first

            smallest.append(node.val) # add current value after the smaller values

            dfs(node.right) # then visit the larger values
        
        dfs(node) # start inorder traversal from the node

        return smallest[k-1] #retrun k-1?

        