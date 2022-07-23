class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        modMap = defaultdict(int)
        count = 0
        for i in range(len(time)):
            currMod = time[i] % 60
            if 60 - currMod in modMap:
                count += modMap[60 - currMod]
            elif currMod == 0:
                count += modMap[0]
            modMap[currMod] += 1
        return count