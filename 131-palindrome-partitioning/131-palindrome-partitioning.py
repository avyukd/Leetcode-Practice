class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        partitions = []
        
        def isPalindrome(word):
            i, j = 0, len(word) - 1
            while i <= j:
                if word[i] != word[j]: return False
                i += 1
                j -= 1
            return True
        
        def backtrack(word, partition):
            if word == "":
                partitions.append(partition)
                return
            
            if len(word) == 1:
                backtrack("", partition + [word])
                return 
            
            for i in range(1, len(word) + 1):
                pre, suff = word[:i], word[i:]
                if isPalindrome(pre):
                    backtrack(suff, partition + [pre])
        
        backtrack(s, [])
        
        return partitions