"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        old_to_new = {}

        def traverse_graph(node: Node):

            if node in old_to_new: # check if node is alr in dictionary
                return old_to_new[node] # return that said node, because we need to make sure
                # each node gets exactly one cloned node
            
            if node is None:
                return None

            copy = Node(node.val) # create a copy of Node(node.val)

            old_to_new[node] = copy # why we do this?

            for neighbor in node.neighbors:
                copy.neighbors.append(traverse_graph(neighbor)) # explain this

            return copy
                
        return traverse_graph(node) #call recrusive function
        
