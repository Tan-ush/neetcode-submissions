from collections import deque
class Solution:
    max = 0
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid) - 1
        COL = len(grid[0]) - 1
        q = deque()

        num_fruit = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i, j))
                    num_fruit += 1
                elif grid[i][j] == 1:
                    num_fruit += 1
        if not q:
            return 0 if num_fruit == 0 else -1

        new_num_fruit = 0
        while q:
            pos = q.popleft()

            for d in self.dir:
                new = (pos[0] + d[0], pos[1] + d[1])

                if new[0] < 0 or new[0] > ROW or new[1] < 0 or new[1] > COL or grid[new[0]][new[1]] == 0 or grid[new[0]][new[1]] > 1:
                    continue
                
                grid[new[0]][new[1]] += grid[pos[0]][pos[1]]
                q.append(new)
                self.max = max(grid[new[0]][new[1]], self.max)

            if grid[pos[0]][pos[1]] == 2:
                grid[pos[0]][pos[1]] = 0
            new_num_fruit += 1
        
        if new_num_fruit != num_fruit:
            return -1
            
        return max(self.max - 2, 0)
                
            
            
            

                



        