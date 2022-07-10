class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for ticket in tickets:
            adj[ticket[0]].append(ticket[1])
        
        for key in adj:
            adj[key].sort()
                
        iten = ""
        visited = Counter([tuple(ticket) for ticket in tickets])
        memo = set()
        def dfs(start="JFK", path=["JFK"]):
            nonlocal iten
            if iten != "":
                return
            elif sum(visited.values()) == 0:
                iten = " ".join(path)
                return
            
            for child in adj[start]:
                if visited[(start, child)] > 0:
                    visited[(start, child)] -= 1
                    dfs(child, path + [child])
                    visited[(start, child)] += 1
        
        dfs()
        return iten.split(" ")