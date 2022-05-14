class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #edge cases t has length 1
        if len(t) == 1:
            return t if t in s else ""
        
        freq = Counter(t)
        
        i, j = 0, 0
        minStart = 0
        minLength = 100000
        queue = deque()
        while i < len(s) and s[i] not in freq:
            i += 1
            j += 1
        
        while j < len(s):
            if s[j] in freq:
                freq[s[j]] -= 1
                queue.append(j)

            if all([x <= 0 for x in list(freq.values())]):
                if j - i + 1 < minLength:
                    minStart = i
                    minLength = j - i + 1
                queue.popleft()
                # length of t > 1 so queue is nonempty
                freq[s[i]] += 1
                i = queue[0]
                while all([x <= 0 for x in list(freq.values())]):
                    if j - i + 1 < minLength:
                        minStart = i
                        minLength = j - i + 1
                    queue.popleft()
                    # length of t > 1 so queue is nonempty
                    freq[s[i]] += 1
                    i = queue[0]
            
            j += 1
            
        return "" if minLength == 100000 else s[minStart:minStart + minLength]