class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        adjList = defaultdict(list)
        for i in range(len(edges)):
            (a, b) = edges[i]
            p = succProb[i]
            adjList[a].append((p, b))
            adjList[b].append((p, a))
        
        curr = (1, start)
        visited = set() # node to best known path
        queue = [curr]
        
        maxprob = 0
        
        while queue:
            (cost, node) = heapq.heappop(queue)
            cost *= -1
            
            if node not in visited:
                
                if node == end:
                    maxprob = max(maxprob, cost)
                
                else:
                    visited.add(node)

                    for (prob, child) in adjList[node]:
                        heapq.heappush(queue, (-abs(cost * prob), child))
        
        return maxprob