class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        island = 0
        row, col = len(grid), len(grid[0])
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                curr_row, curr_col = q.popleft()
                for x,y in directions:
                    new_row = curr_row + x
                    new_col = curr_col + y
                    if (new_row in range(row) and new_col in range(col) and grid[new_row][new_col] == "1" and (new_row,new_col) not in visited):
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))

            


        for r in range(row):
            for c in range(col):
                if ((grid[r][c] == "1") and ((r,c) not in visited)):
                    bfs(r,c)
                    island += 1
        return island