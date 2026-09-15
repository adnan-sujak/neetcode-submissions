class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or
                c == COLS or board[r][c] != "O"
            ): # checking out of bounds OR if square is not 0
              # we only care about those squares
                return
           
            board[r][c] = "T" 

            #board[r][c] = the CURRENT square DFS is visiting.
            #
            # This is NOT necessarily an edge 0.
            # The loops BELOW are what initially call capture()
            # on an edge 0
            #
            #We change it to "T" to mean:
            #"This 0 is connected to an edge, so it is SAFE"

            capture(r + 1, c) #dfs down
            capture(r - 1, c) #dfs up   
            capture(r, c + 1) #dfs move right
            capture(r, c - 1) #dfs move left

        for r in range(ROWS):
            # PURPOSE:
            # Go through every ROW and check the
            # Left and right edges
            if board[r][0] == "O":
                # column 0 = LEFT edge
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                # last column = RIGHT EDGE
                capture(r, COLS - 1)

        for c in range(COLS):
            # Go through every COLUMN and check the 
            # TOP and bottom edges
            if board[0][c] == "O":
                # row 0 = top edge
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                # bottom eedge
                capture(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":

                # if its still 0, DFS never reached it.
                # therefore it wasn't connected to an edge
                # its surrounded, so capture it
                    board[r][c] = "X"
               
                elif board[r][c] == "T":
                    # this was connected to an edhe
                    # its safe, so turn it back into 0
                    board[r][c] = "O"