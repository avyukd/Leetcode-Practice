class Solution {
    public:
        int maxSubArray(vector<int>& nums){
            int maxSum = nums[0];
            int currSum = nums[0];
            for(int i = 1 ; i < nums.size() ; i++){
                if(currSum < 0)
                    currSum = 0;
                currSum += nums[i];
                maxSum = max(currSum, maxSum);
            }            
            return maxSum;
        }        
};













// class Solution {
// public:
//     int maxSubArray(vector<int>& nums) {
//         //no memo
//         int maxValue = nums[0];
//         for(int i = 1 ; i < nums.size() ; i++){
//             nums[i] = max(nums[i], nums[i]+nums[i-1]);
//             maxValue = max(maxValue, nums[i]);
//         }
//         return maxValue;
//         /*
//         DP with memo
//         vector<int> sums(nums.size());
//         sums[0] = nums[0];
//         for(int i = 1 ; i < nums.size() ; i++){
//             sums[i] = max(nums[i], sums[i-1]+nums[i]);
//         }
//         int maxValue = sums[0];
//         for(int s: sums) maxValue = max(s, maxValue);
//         return maxValue;*/ 
//     }
// };