class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        # Find all treasures

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col)) # we have the location of the treasure
        
        directions = [(1,0), (-1,0), (0,1), (0, -1)]

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                # Out of bounds
                if (
                    new_row < 0 or
                    new_col < 0 or
                    new_row >= rows or
                    new_col >= cols
                ):
                    continue

                # Skip water, treasures, and already-visited land
                if grid[new_row][new_col] != 2147483647:
                    continue

                # Neighbor is 1 step farther than current cell
                grid[new_row][new_col] = grid[row][col] + 1

                # Visit this cell's neighbors later
                queue.append((new_row, new_col))
                
                
        
