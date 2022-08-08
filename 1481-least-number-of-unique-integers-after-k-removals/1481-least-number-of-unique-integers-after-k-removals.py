class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        pairs = [list(item) for item in freq.items()]
        pairs.sort(key=lambda x: x[1])
        i = 0
        while k > 0:
            pairs[i][1] -= 1
            if pairs[i][1] == 0:
                i += 1
            k -= 1
        return len(pairs) - i