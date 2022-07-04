class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {courseNum: [] for courseNum in range(numCourses)}
        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
        
        indegree = {courseNum: 0 for courseNum in range(numCourses)}
        for prereq in prerequisites:
            indegree[prereq[0]] += 1 
        
        # perform topological sort
        # if success, return true
        # if fail, there is a cycle
        
        toposorted = []
        
        no_incoming_edges = []
        for num in indegree:
            if indegree[num] == 0:
                no_incoming_edges.append(num)
        
        while len(no_incoming_edges) > 0:
            curr = no_incoming_edges.pop()
            toposorted.append(curr)
            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    no_incoming_edges.append(neighbor)
        
        return len(toposorted) == numCourses