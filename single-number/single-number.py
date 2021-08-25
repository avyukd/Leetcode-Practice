class Solution(object):
    def singleNumber(self, nums):
        #some how bitwise XOR works here?? need to figure out what bitwise XOR acc does
        
        res = nums[0] 
      
        # Do XOR of all elements and return 
        for i in range(1,len(nums)): 
            res = res ^ nums[i] 

        return res 
        