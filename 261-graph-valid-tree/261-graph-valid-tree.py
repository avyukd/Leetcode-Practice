class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= 1:
            return len(edges) == 0
        
        adjList = defaultdict(set)
        degree = [0] * n
        
        for edge in edges:
            # cycle
            if edge[0] == edge[1]:
                return False
            adjList[edge[0]].add(edge[1])
            adjList[edge[1]].add(edge[0])
            degree[edge[1]] += 1
            degree[edge[0]] += 1
            
        # there's an isolated node
        if any([deg == 0 for deg in degree]):
            return False
        
        
        # perform dfs
        stack = deque([0])
        visited = set()
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                for child in adjList[curr]:
                    adjList[child].remove(curr)
                    stack.append(child)
            else:
                return False
        
        return len(visited) == n