# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], sub_root: Optional[TreeNode]):
            if root is None and sub_root is None:
                return True
            if root is None and sub_root is not None:
                return False
            elif root is not None and sub_root is None:
                return False
            
            left = dfs(root.left, sub_root.left)
            right = dfs(root.right, sub_root.right)

            if root.val == sub_root.val and left and right:
                return True
            return False  
            
              
        if root is None:
            return False

        if dfs(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)




        

