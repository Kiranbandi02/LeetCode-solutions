class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = deque()
        visited = [[False] * (1 << n) for _ in range(n)]
        
        for i in range(n):
            queue.append((1 << i, i, 0))
            visited[i][1 << i] = True
            
        while queue:
            mask, x, dist = queue.popleft()
            
            if mask == (1 << n) - 1:
                return dist
            
            for neighbor in graph[x]:
                new_mask = mask | (1 << neighbor)
                
                if not visited[neighbor][new_mask]:
                    queue.append((new_mask, neighbor, dist + 1))
                    visited[neighbor][new_mask] = True