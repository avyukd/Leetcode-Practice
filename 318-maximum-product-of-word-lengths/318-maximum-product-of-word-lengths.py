class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x), reverse=True)
        
        freqs = [[0] * 26 for _ in range(len(words))]
        for i in range(len(words)):
            for char in words[i]:
                freqs[i][ord(char) - ord('a')] = 1
        
        def haveCommon(idx1, idx2):
            i = 0
            while i < 26:
                if freqs[idx1][i] == 1 and freqs[idx2][i] == 1:
                    return True
                i += 1
            return False
        
        maxProd = 0
        for i in range(len(words) - 1):
            for j in range(i+1, len(words)):
                currProd = len(words[i]) * len(words[j])
                if currProd <= maxProd:
                    break
                if not haveCommon(i, j):
                    maxProd = currProd
        
        return maxProd
    
        