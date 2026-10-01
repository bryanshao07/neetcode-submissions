class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        parent = [i for i in range(n)]
        rank = [1] * n
        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        def union(a,b):
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                return False
            if rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
                rank[root_a] += rank[root_b]
            else:
                parent[root_a] = root_b
                rank[root_b] += rank[root_a] 
            return True
        for a, b in edges:
            if not union(a,b):
                return False
        return True