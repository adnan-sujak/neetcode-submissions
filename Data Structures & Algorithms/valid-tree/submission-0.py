from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n-1):
            return False
        if n == 1:
            return len(edges) == 0 #checking if this is true
        

        visited = set()
        graph = defaultdict(list) # creates list if something doesnt exist

        nodes = set()

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

            #nodes that have a neighbor
           
            nodes.add(a)
            nodes.add(b)
        
        if len(nodes) != n: #one node doesnt have an edge
            return False

        def has_no_cycles(node, parent):
            if node in visited:
                return False # cycle
            
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not has_no_cycles(neighbor, node):
                    return False
            return True
        
        start_node = next(iter(nodes))
        return has_no_cycles(start_node, None) and len(visited) == n
                


