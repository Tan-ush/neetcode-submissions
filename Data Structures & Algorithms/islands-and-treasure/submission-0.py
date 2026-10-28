from collections import deque
class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid) - 1
        COL = len(grid[0]) - 1
        inf = float('inf')
        seen = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.appendleft((row, col))
        
        while q:
            pos = q.pop()
            for dir in dirs:
                new = (pos[0] + dir[0], pos[1] + dir[1])
                if new in seen or new[0] < 0 or new[1] < 0 or new[0] > ROW or new[1] > COL or grid[new[0]][new[1]] == 0 or grid[new[0]][new[1]] == -1:
                    continue
                grid[new[0]][new[1]] = grid[pos[0]][pos[1]] + 1
                q.appendleft(new)
                seen.add(new)

            


        