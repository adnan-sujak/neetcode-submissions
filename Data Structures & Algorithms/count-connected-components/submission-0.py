from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        visited = set()
        

        for x, y in edges:
            graph[x].append(y) #accessing x but its not there yet, create a list in its place with x
            graph[y].append(x)


        def visit(node):

            if node in visited:
                return
           
            visited.add(node)
            
            for x in graph[node]:
                visit(x)
        
        counter = 0
        for node in range(n): # range n is needed because we might have a node by itself and that counts as a 
        #separete graph. if it has no edges it wont be in graph, so range(n) accounts for it
            if node not in visited:
                counter +=1
                visit(node)

        return counter

            