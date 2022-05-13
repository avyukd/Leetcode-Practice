class Solution: 
    def insert(self, intervals: List[List[int]], newInterval: List[int]):
        if intervals == []:
            return [newInterval]
        
        merged = []
        i = 0
        while i < len(intervals) and intervals[i][0] <= newInterval[0]:
            merged.append(intervals[i])
            i += 1
        
        if merged == []:
            merged.append(newInterval)
        elif merged[-1][1] >= newInterval[0]:
            merged[-1][1] = max(newInterval[1], merged[-1][1])
        else:
            merged.append(newInterval)

        while i < len(intervals):
            if merged[-1][1] >= intervals[i][0]:
                merged[-1][1] = max(intervals[i][1], merged[-1][1])
            else:
                merged.append(intervals[i])
            i += 1
        
        return merged
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         # 1 binary search to find insertpos
#         # 2 merge overlapping intervals
#         if len(intervals) == 0:
#             return [newInterval]
#         elif len(intervals) == 1:
#             if newInterval[0] > intervals[0][0]:
#                 if newInterval[0] <= intervals[0][1]:
#                     return [[intervals[0][0], max(intervals[0][1], newInterval[1])]]
#                 else:
#                     return intervals + [newInterval]
#             elif newInterval[0] < intervals[0][0]:
#                 if intervals[0][0] <= newInterval[1]:
#                     return [[newInterval[0], max(intervals[0][1], newInterval[1])]]
#                 else:
#                     return [newInterval] + intervals
#             else:
#                 return [[intervals[0][0], max(intervals[0][1], newInterval[1])]]
#         inserted = False
#         left, right = 0, len(intervals)
#         while left <= right:
#             mid = (left + right) // 2
#             if intervals[mid][0] < newInterval[0]:
#                 left = mid + 1
#             elif intervals[mid][0] > newInterval[0]:
#                 right = mid - 1
#             else:
#                 intervals[mid][1] = max(newInterval[1], intervals[mid][1])
#                 inserted = True
        
        
#         if not inserted:
#             intervals = intervals[:mid+1] + [newInterval] + intervals[mid+1:]
        
        
#         merged = [intervals[0]]
#         for interval in intervals[1:]:
#             if merged[-1][1] >= interval[0]:
#                 merged[-1][1] = max(interval[1], merged[-1][1])
#             else:
#                 merged.append(interval)
        
#         return merged
        