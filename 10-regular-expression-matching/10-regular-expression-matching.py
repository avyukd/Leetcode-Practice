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
        
        def backtrack(word, pattern):
            if len(pattern) == 0 and len(word) == 0:
                return True
            elif len(pattern) == 0:
                return False
            
            char, pat = word[0] if len(word) > 0 else "", pattern[0]
            
            if char == pat or (pat == '.' and char != ""):
                return backtrack(word[1:], pattern[1:])
            
            if pat[-1] == '*':
                i = -1
                while i < len(word) and (i == -1 or word[i] == pat[0] or pat[0] == '.'):
                    if backtrack(word[i+1:], pattern[1:]):
                        return True
                    i += 1
                return False
            return False
        
        return backtrack(s, plist)
        