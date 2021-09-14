class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> memo(nums.size());
        memo[0] = 1; 
        for(int i = 1 ; i < nums.size(); i++){
            int maxLength = 0; 
            for(int j = 0; j < i; j++){
                if(nums[j] < nums[i])
                    maxLength = max(maxLength, memo[j]);
            }
            cout << nums[i] << endl; 
            cout << maxLength << endl; 
            memo[i] = maxLength + 1; 
        }
        int maxLIS = 0; 
        for(auto m : memo) maxLIS = max(maxLIS, m);
        return maxLIS; 
    }
};