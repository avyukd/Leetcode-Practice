class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        # the only way its NOT possible is if source or target are locked in a circle
        # dfs and end if ur depth is 200+ 
        
        blockedSet = set([tuple(x) for x in blocked])
        
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        
        def bfs(xin, yin, other):
            
            queue = deque([(xin, yin)])
            
            
            depth = 0
            visited = set()
            while queue:
                if depth >= 201:
                    break
                
                level = queue.copy()
                queue = deque([])
                for (x, y) in level:
                    if (x, y) not in visited:
                        if (x, y) == other:
                            return True
                        
                        visited.add((x, y))
                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < 10**6 and 0 <= ny < 10**6 and (nx, ny) not in blockedSet:
                                queue.append((nx, ny))
                
                depth += 1
            
            return True if depth >= 201 else False
        
        return bfs(source[0], source[1], tuple(target)) and bfs(target[0], target[1], tuple(source))