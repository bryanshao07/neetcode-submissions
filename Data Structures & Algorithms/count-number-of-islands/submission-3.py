class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        if not grid:
            return island
        row, col = len(grid), len(grid[0])
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                curr_row, curr_col = q.popleft()
                directions = [[1,0], [0,1], [-1,0], [0,-1]]
                for r_d, c_d in directions:
                    new_row, new_col = curr_row + r_d, curr_col + c_d
                    if ((new_row in range(row)) and (new_col in range(col)) and grid[new_row][new_col] == "1" and (new_row, new_col) not in visited):
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    island += 1
        return island
        