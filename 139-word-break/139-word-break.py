class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        def backtrack(word):
            if word in memo:
                return memo[word]
            
            if len(word) == 0:
                return True
                
            for prefix in wordDict:
                if prefix == word[:len(prefix)]:
                    if len(prefix) <= len(word) and backtrack(word[len(prefix):]):
                        return True
            
            memo[word] = False
            return False
    
        return backtrack(s)