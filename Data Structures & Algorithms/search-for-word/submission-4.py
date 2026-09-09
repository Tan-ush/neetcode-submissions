class Solution:
    def dfs(self, i, j, word, board):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == 0:
            return False
        if word[0] != board[i][j]:
            return False
        temp = board[i][j]
        board[i][j] = 0
        if len(word) == 1:
            return True
        a = self.dfs(i + 1, j, word[1:], board)
        b = self.dfs(i - 1, j, word[1:], board)
        c = self.dfs(i, j + 1, word[1:], board)
        d = self.dfs(i, j - 1, word[1:], board)
        if a or b or c or d:
            return True
        board[i][j] = temp
        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    val = self.dfs(i, j, word, board)
                    if val:
                        return True
        return False