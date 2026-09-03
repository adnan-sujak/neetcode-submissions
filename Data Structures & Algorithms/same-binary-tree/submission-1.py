# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:



        def dfs(root1: Optional[TreeNode], root2: Optional[TreeNode]):
            if root1 is None and root2 is None:
                return True
            
            #if root1 is None and root2 is not None:
                #return False
            #elif root1 is not None and root2 is None:
                #return False

            if root1 is None or root2 is None:
                return False

    
            left = dfs(root1.left, root2.left)
            right = dfs(root1.right,root2.right)

            if root1.val == root2.val and left and right:
                return True
            return False
            
        return dfs(p,q)
        