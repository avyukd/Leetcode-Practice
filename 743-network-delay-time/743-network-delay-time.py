import heapq

class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for src, dst, c in times:
            graph[src].append((dst, c)) 
        
        
        queue = [(0, k)] #(cost, node)
        visited = set()
        max_cost = 0
            
        while queue:
            
            #Always pop the min value
            cost, node = heapq.heappop(queue)
            
            if node in visited:
                continue
                
            visited.add(node)
            
            max_cost = max(max_cost, cost)

            neighbours = graph[node]
            
            for neighbour in neighbours:
                
                new_node, new_cost = neighbour
                
                if new_node not in visited:
                    
                    curr_cost =  cost + new_cost
                    
                    heapq.heappush(queue, (curr_cost, new_node))
        

        return max_cost if len(visited) == n else -1
        
    # dfs
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         edges = defaultdict(list)
#         for time in times:
#             edges[time[0]].append((time[1],time[2]))
#         #for time in times:
#         #    edges[time[0]].sort(key=lambda x: x[1], reverse=True)
        
#         visited = [1000]*(n+1)
        
#         def dfs(currNode, currDelay):
#             if currDelay >= visited[currNode]: 
#                 return
            
#             visited[currNode] = currDelay
            
#             for child, weight in edges[currNode]:
#                 dfs(child, currDelay + weight)
            
#         dfs(k, 0)
        
#         answer = max(visited[1:])
#         return -1 if answer == 1000 else answer 