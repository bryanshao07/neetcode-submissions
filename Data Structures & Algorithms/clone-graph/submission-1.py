class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        map = {}
        map[node] = Node(node.val)
        q = collections.deque()
        q.append(node)
        
        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in map:
                    map[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                map[curr].neighbors.append(map[neighbor])
        
        return map[node]