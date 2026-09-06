# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node: TreeNode, max_value):
            if node is None: # null check
                return 0
            
            result = 0 # create result

            if node.val >= max_value: # if nodee.val, that is passed in, is greater than max_value
                result +=1 # add 1
            
            max_value = max(max_value, node.val) # update max_value

            result += dfs(node.left, max_value) # gets result of the rest of the tree, carrying along  max_value
            result += dfs(node.right, max_value)

            return result
      
        return dfs(root, root.val)
        