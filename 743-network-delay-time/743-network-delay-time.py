class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for time in times:
            edges[time[0]].append((time[1],time[2]))
        #for time in times:
        #    edges[time[0]].sort(key=lambda x: x[1], reverse=True)
        
        visited = [1000]*(n+1)
        
        def dfs(currNode, currDelay):
            if currDelay >= visited[currNode]: 
                return
            
            visited[currNode] = currDelay
            
            for child, weight in edges[currNode]:
                dfs(child, currDelay + weight)
            
        dfs(k, 0)
        
        answer = max(visited[1:])
        return -1 if answer == 1000 else answer 