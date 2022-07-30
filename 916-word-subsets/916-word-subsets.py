class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        def isSubset(wMap, subMap):
            for i in range(len(subMap)):
                if subMap[i] > wMap[i]:
                    return False
            return True
        
        singleRep = [0] * 26
        for subset in words2:
            chMap = [0] * 26
            for ch in subset:
                chMap[ord(ch) - ord('a')] += 1
            
            for i in range(len(chMap)):
                singleRep[i] = max(singleRep[i], chMap[i])
        
        res = []
        for word in words1:
            wordMap = [0] * 26
            for ch in word:
                wordMap[ord(ch) - ord('a')] += 1
            
            if isSubset(wordMap, singleRep):       
                res.append(word)
        
        return res