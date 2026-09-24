class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        visited = set()
        row, col = len(grid), len(grid[0])

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                currR, currC = q.popleft()
                directions = [[0,1], [0,-1], [1,0], [-1,0]]
                for x, y in directions:
                    newR, newC = currR + x, currC + y
                    if newR in range(row) and newC in range(col) and grid[newR][newC] == '1' and (newR, newC) not in visited:
                        q.append((newR, newC))
                        visited.add((newR, newC))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands