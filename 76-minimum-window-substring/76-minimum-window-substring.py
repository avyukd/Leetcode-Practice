class Solution:
    def minWindow(self, s, t):
        minWindowSize, minSubStr = 10**6, ""
        currWindow = Counter(t)
        i, j = 0 
        formed = 0
        while j < len(s):
            if s[j] in currWindow: 
                if currWindow[s[j]] <= 0 and s[i] == s[j]:
                    currWindow[s[i]] += 1
                    if currWindow[s[i]] > 0:
                        formed -= 1
                    i += 1
                    while s[i] not in currWindow and i <= j:
                        i += 1
                currWindow[s[j]] -= 1
                if currWindow[s[j]] == 0:
                    formed += 1
            elif s[j] not in currWindow and i == j:
                i += 1
                j += 1
            if formed == len(t):# all([currWindow[key] <= 0 for key in currWindow]):
                if j - i + 1 < minWindowSize:
                    minWindowSize = j - i + 1
                    minSubStr = s[i:j+1]
                currWindow[s[i]] += 1
                if currWindow[s[i]] > 0:
                    formed -= 1
                i += 1
                while s[i] not in currWindow and i <= j:
                    i += 1
        return minSubStr     
    
    
    
    
    
    
    
    
    
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