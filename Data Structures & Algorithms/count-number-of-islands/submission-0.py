class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid) - 1
        cols = len(grid[0]) - 1
        islands = 0
        
        def dfs(x, y):
            if x < 0 or y < 0 or x > cols or y > rows or grid[y][x] == "0":
                return None
            grid[y][x] = "0"
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    dfs(x, y)
                    islands += 1
        return islands


        