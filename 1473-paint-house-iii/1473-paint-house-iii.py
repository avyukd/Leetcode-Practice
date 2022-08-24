class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dfs(i, k, p):
            if i == m and k == target: return 0
            if i >= m or k > target: return inf
            
            res = inf
            if houses[i]:
                res = min(res, dfs(i+1, k + (houses[i] != p), houses[i]))
            else:
                for c in range(1, n+1):
                    res = min(res, cost[i][c-1] + dfs(i+1, k + (c != p), c))
            return res
        
        res = dfs(0, 0, None)
        return res if res < inf else -1

    
#     def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
#         # get current number of neighborhoods
#         numHoods = 0
#         i, j = 0, 0
        
#         while j < len(houses):
#             while j < len(houses) and houses[i] == houses[j]:
#                 j += 1
#             if houses[i] != 0:
#                 numHoods += 1
#             i = j
        
#         minCost = 10**6
        
#         memo = {}
#         def dp(i, count, currCost):
#             if (i, count, currCost) in memo:
#                 return memo[(i, count, currCost)]
            
#             if i == m:
#                 if count == target and all([house > 0 for house in houses]):
#                     return currCost
#                 return 10**6
            
            
#             if houses[i] != 0:
#                 if i - 1 >= 0 and houses[i] == houses[i - 1]:
#                     ans = dp(i + 1, count, currCost)
#                 else:
#                     ans = dp(i + 1, count + 1, currCost)
#             else:
#                 ans = 10**6
#                 for col in range(n + 1):
#                     houses[i] = col
#                     if i - 1 >= 0 and houses[i - 1] == col:
#                         ans = min(ans, dp(i + 1, count, currCost + cost[i][col - 1]))
#                     else:
#                         ans = min(ans, dp(i + 1, count + 1, currCost + cost[i][col - 1]))
#                     houses[i] = 0
            
#             memo[(i, count, currCost)] = ans
#             return ans
        
#         fin = dp(0, 0, 0)
#         return -1 if fin == 10**6 else fin