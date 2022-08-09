class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        factorMap = {}
        arr.sort()
        for i in range(len(arr)):
            total = 1
            num = arr[i]
            for key in factorMap:
                if num % key == 0 and num / key in factorMap:
                    total += factorMap[key] * factorMap[num / key]
            factorMap[num] = total
        return sum(factorMap.values()) % (10**9 + 7)