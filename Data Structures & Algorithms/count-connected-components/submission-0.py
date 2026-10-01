class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #adjacency list 
        graph = [[] for i in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        counter = 0
        #dfs algorithim
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        #run dfs method for every node 
        for i in range(n):
            if i not in visited:
                counter += 1 
                dfs(i)
        return counter