# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        q = [root]
        values = []

        while q:
            level = []
            max_level_size = len(q)

            for i in range(max_level_size):
                node = q.pop(0)
                level.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            values.append(level)
        return values

        #q = deque([root])
        #res = []

       #while q:
       #    level = []
       #    for _ in range(len(q)):
       #        node = q.popleft()
       #        level.append(node.val)
       #        if node.left:
       #            q.append(node.left)
       #        if node.right:
       #            q.append(node.right)
       #    res.append(level)

       #return res



        