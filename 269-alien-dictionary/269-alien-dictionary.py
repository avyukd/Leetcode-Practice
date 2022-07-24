class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        isoNodes = set(words[0])
        
        edges = []
        for i in range(len(words) - 1):
            # word1 < word2
            for ch in set(words[i + 1]):
                isoNodes.add(ch)
            
            word1, word2 = words[i], words[i + 1]
            
            if word1 == word2:
                continue
            
            i, j = 0, 0
            while i < len(word1) and j < len(word2) and word1[i] == word2[j]:
                i += 1
                j += 1
            
            
            if i >= len(word1): # no info gain
                continue
            
            if j >= len(word2):
                return ""
                
            edges.append((word1[i], word2[j]))
        
        # find the node with indegree 0
        indeg = defaultdict(int)
        adjList = defaultdict(list)
        for edge in edges:
            indeg[edge[0]] += 0
            indeg[edge[1]] += 1
            adjList[edge[0]].append(edge[1])
            if edge[0] in isoNodes:
                isoNodes.remove(edge[0])
            if edge[1] in isoNodes:
                isoNodes.remove(edge[1])
        
        for node in isoNodes:
            indeg[node] = 0
            adjList[node] = []
                
        retStr = ""
        visited = set()
        while len(visited) != len(indeg.keys()):
            roots = []
            for key in indeg:
                if indeg[key] == 0 and key not in visited:
                    roots.append(key)
            if len(roots) == 0:
                return ""
            for root in roots:
                visited.add(root)
                retStr += root
                for child in adjList[root]:
                    indeg[child] -= 1
        
        return retStr
    
#         ret = ""
#         for node in isoNodes:
#             ret += node
        
#         roots = []
#         for key in indeg:
#             if indeg[key] == 0:
#                 roots.append(key)
        
#         if roots == [] and ret == "":
#             return ""
                
#         for root in roots:
#             curr = root
#             while curr in adjList:
#                 ret += curr
#                 curr = adjList[curr]
#             ret += curr
                
#         return ret
                    