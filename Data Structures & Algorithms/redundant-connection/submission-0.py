class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)

        #find the root of a node 
        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]  # point to grandparent
                node = parent[node]
            return node
        #merge components of two nodes 
        def union(a,b):
            root_a, root_b = find(a), find(b)
            if find(a) == find(b):
                return False
            #if components are in seperate trees, merge them based on rank
            if rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
                rank[root_a] += rank[root_b]
            else:
                parent[root_a] = root_b
                rank[root_b] += rank[root_a]
            return True
        for a, b in edges:
            if not union(a,b):
                return [a,b]
