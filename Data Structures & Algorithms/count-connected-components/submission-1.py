class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1]*n

        #find the root of a node
        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node 
        
        #merge two components and decrement by one component count 
        counter = n
        def union(a, b):
            root_a, root_b = find(a), find(b)

            #if componenets are in same tree, no need to decrement
            if root_a == root_b:
                return 0
            
            #merge by rank 
            if rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
                rank[root_b] += rank[root_a]
            else:
                parent[root_b] = root_a
                rank[root_a] += rank[root_b]
            return 1
        for a, b in edges:
            counter -= union(a,b)
        return counter