class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> sums(nums.size());
        sums[0] = nums[0];
        for(int i = 1 ; i < nums.size() ; i++){
            sums[i] = max(nums[i], sums[i-1]+nums[i]);
        }
        int maxValue = sums[0];
        for(int s: sums) maxValue = max(s, maxValue);
        return maxValue; 
    }
};