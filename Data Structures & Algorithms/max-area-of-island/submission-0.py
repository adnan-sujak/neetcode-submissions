class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        rows = len(grid) # gets the number of rowskis
        cols = len(grid[0])

        def get_area(row, col):
            if col < 0 or row < 0 or row >= rows or col >= cols or (row, col) in visited or grid[row][col] == 0:
                return 0
            visited.add((row, col))
            area = 1
            
            area += get_area(row + 1, col)
            area += get_area(row -1, col)
            area += get_area(row, col + 1)
            area += get_area(row, col - 1)
            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max(max_area, get_area(row,col))
        return max_area
