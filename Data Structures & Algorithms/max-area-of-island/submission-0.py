class Solution:
    max = 0
    local = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROW = len(grid) - 1
        COL = len(grid[0]) - 1

        def dfs(row, col):
            if row < 0 or col < 0 or row > ROW or col > COL or grid[row][col] == 0:
                return None
            self.local += 1
            grid[row][col] = 0
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(row, col)
                    self.max = max(self.max, self.local)
                    self.local = 0
        return self.max

        