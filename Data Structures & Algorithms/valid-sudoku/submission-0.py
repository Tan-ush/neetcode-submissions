class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowdict = {}
        coldict = {}
        griddict = {}
        for row in range(len(board)):
            if 0 <= row <= 2:
                grid = 0
            elif 3 <= row <= 5:
                grid = 3
            else:
                grid = 6
            for col in range(len(board[0])):
                if col == 3 or col == 6:
                    grid += 1
                if board[row][col] != ".":
                    # For each row
                    if row not in rowdict:
                        rowdict[row] = {board[row][col]: True}
                    else:
                        if board[row][col] in rowdict[row]:
                            return False
                        rowdict[row][board[row][col]] = True

                    # For each col
                    if col not in coldict:
                        coldict[col] = {board[row][col]: True}
                    else:
                        if board[row][col] in coldict[col]:
                            return False
                        coldict[col][board[row][col]] = True

                    # For each grid
                    if grid not in griddict:
                        griddict[grid] = {board[row][col]: True}
                    else:
                        if board[row][col] in griddict[grid]:
                            return False
                        griddict[grid][board[row][col]] = True
        return True  

        