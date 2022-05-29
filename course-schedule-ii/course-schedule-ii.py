class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adjlist = defaultdict(list)
        indeg = defaultdict(int)
        
        for pair in prerequisites:
            adjlist[pair[1]].append(pair[0])
            indeg[pair[0]] += 1
        
        # find indeg = 0
        start = []
        for key in range(numCourses):
            if indeg[key] == 0:
                start.append(key) 
        if len(start) == 0:
            return [] #impossible
        
        order = []
        queue = deque(start)
        while queue:
            nxt = queue.popleft()
            order.append(nxt)
            children = adjlist[nxt]
            for child in children:
                indeg[child] -= 1
                if indeg[child] == 0:
                    queue.append(child)
        
        
        return [] if len(order) != numCourses else order
            
        
        