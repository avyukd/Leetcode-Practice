class Solution:
    def alienOrder(self, words: List[str]) -> str:
        allNodes = set(words[0])
        edges = []
        for i in range(len(words) - 1):
            # word1 < word2
            for ch in set(words[i + 1]):
                allNodes.add(ch)
            
            word1, word2 = words[i], words[i + 1]
            
            if word1 == word2:
                continue
            
            i, j = 0, 0
            while i < len(word1) and j < len(word2) and word1[i] == word2[j]:
                i += 1
                j += 1
            
            
            if i >= len(word1): # no info gain
                continue
            
            if j >= len(word2): # invalid
                return ""
                
            edges.append((word1[i], word2[j]))
        
        # find the node with indegree 0
        indeg = defaultdict(int)
        adjList = defaultdict(list)        
                
        for node in allNodes:
            indeg[node] = 0
            adjList[node] = []

        for edge in edges:
            indeg[edge[1]] += 1
            adjList[edge[0]].append(edge[1])
                
        roots = []
        for key in indeg:
            if indeg[key] == 0:
                roots.append(key)
        
        retStr = ""
        while len(roots) > 0:
            root = roots.pop()
            retStr += root
            for child in adjList[root]:
                indeg[child] -= 1
                if indeg[child] == 0:
                    roots.append(child)
                
        return "" if len(retStr) != len(allNodes) else retStr
    