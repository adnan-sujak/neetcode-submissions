class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        number_of_islands = 0

        def traverse(row: int, col: int):
            if col < 0 or row < 0 or row >= len(grid) or col >= len(grid[0]):
                # len(grid[0]), only need to compare against first row 
                return
            if grid[row][col] == "0" or (row,col) in visited:
                return
            
            visited.add((row,col)) # adds it as a tuple
            traverse(row+1, col) # down for row + 1
            traverse(row-1, col) # up for row -1 
            traverse(row, col+1) # moving right one column
            traverse(row, col-1) # moving left one column

            return traverse(row, col)

        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                if col == "1" and (row_index, col_index) not in visited:
                    number_of_islands +=1
                    traverse(row_index, col_index)

        return number_of_islands
                





        



        