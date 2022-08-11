class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        plist = []
        i = 0
        while i < len(p) - 1:
            if p[i + 1] != '*':
                plist.append(p[i])
                i += 1
            else:
                plist.append(p[i] + p[i+1])
                i += 2
        if p[-1] != '*':
            plist.append(p[-1])
        
        @cache
        def backtrack(i, j):
            word, pattern = s[i:], plist[j:]
            if len(pattern) == 0 and len(word) == 0:
                return True
            elif len(pattern) == 0:
                return False
            
            char, pat = word[0] if len(word) > 0 else "", pattern[0]
            
            if char == pat or (pat == '.' and char != ""):
                return backtrack(i+1, j+1)
            
            if pat[-1] == '*':
                k = -1
                while k < len(word) and (k == -1 or word[k] == pat[0] or pat[0] == '.'):
                    if backtrack(i+k+1, j+1):
                        return True
                    k += 1
                return False
            return False
        
        return backtrack(0, 0)
        