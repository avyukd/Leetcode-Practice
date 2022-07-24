class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def backtrack(word, i):
            if len(word) == 0:
                return True
                
            for prefix in wordDict:
                if prefix == word[:len(prefix)]:
                    if len(prefix) <= len(word):
                        curr = backtrack(word[len(prefix):], len(prefix))
                        if curr:
                            return True
            
            return False
    
        return backtrack(s, 0)