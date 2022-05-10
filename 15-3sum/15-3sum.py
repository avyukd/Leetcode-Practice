class Solution:
    
    # sort and two pointers
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        triplets = set()
        
        for i in range(len(nums)):
            num = nums[i]
            rest = nums[0:i] + nums[i+1:]
            start, end = 0, len(rest) - 1
            while start < end:
                if rest[start] + rest[end] < -num:
                    start+=1
                elif rest[start] + rest[end] > -num:
                    end-=1
                else:
                    x = [rest[start],num,rest[end]]
                    x.sort()
                    triplets.add(tuple(x))
                    start+=1
                    end-=1
        
        return triplets
    
    # brute force-ish solution
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     triplets = set()
    #     for i in range(len(nums)):
    #         num = nums[i]
    #         rest = nums[0:i] + nums[i+1:]
    #         # fix number and find sum to -num in rest of list
    #         seen = set()
    #         dbls = []
    #         for r in rest:
    #             if -num - r in seen:
    #                 dbls.append([min(r,-num -r), max(r,-num - r)])
    #             else:
    #                 seen.add(r)
    #         for dbl in dbls:
    #             if num < dbl[0]:
    #                 triplets.add((num,dbl[0],dbl[1]))
    #             elif num > dbl[1]:
    #                 triplets.add((dbl[0],dbl[1],num))
    #             else:
    #                 triplets.add((dbl[0],num,dbl[1]))
    #     return list(triplets)