# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#class DiamterContext:
    #best = 0

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #ctx=DiamterContext()
        
        #self.best = 0
        best = 0


        def diam_dfs(node):
            if node is None:
                return 0
            nonlocal best

            left = diam_dfs(node.left)
            right = diam_dfs(node.right)

            best = max(best, left + right)

            return 1 + max(left, right) #we need to return the height back up to the parent so its knows which way is longest




        def dfs(node): # writing it outside the main function saves memory if you call diamOfBin more than once

# this is called a closure, a function with state outside of its scope

            if node is None:
                return 0

            nonlocal best # acceses the best variable outside of dfs

            left = dfs(node.left)
            right = dfs(node.right)

            best = max(best, left + right) # get both distances down both paths, set best

            return 1 + max(left, right) # return the height

        diam_dfs(root)
        return best
    
def dfs(ctx, node): # writing it outside the main function saves memory if you call diamOfBin more than once

# this is called a closure, a function with state outside of its scope
    if node is None:
        return 0

    left = dfs(ctx, node.left)
    right = dfs(ctx, node.right)

    ctx.best = max(ctx.best, left + right) # get both distances down both paths, set best

    return 1 + max(left, right) # return the height