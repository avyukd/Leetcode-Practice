class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = Counter(s)
        for char in t:
            if char in freq:
                freq[char] -= 1
            else:
                return False
        return all([val == 0 for val in freq.values()])