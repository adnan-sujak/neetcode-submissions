# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return [] # empty tree -> empty result
        
        q = deque([root]) # add root to the double ended queue
        res = [] # create a result array which stores the rightmost value from each level

        while q: # while q is not empty
            level = [] # create a levels array
            
            for _ in range(len(q)): # loop through 0 -> length of q and get the index in _, len(q) here is the number of nodes currently in this level

                node = q.popleft() 
                # removes the leftmost node from the queue
                # First pass through, this is the root itself, NOT root.left
                # so node = Node(1)


                level.append(node.val) # q = [1]


                if node.left: # if node.left exists
                    q.append(node.left) #add the left node to the queue
                if node.right:
                    q.append(node.right) # same for right
                
            res.append(level[-1])

            # level[-1] is the LAST node we visited on this level
            # because we process nodes from left to right
            # the last node is the rightmost visible node

        return res

