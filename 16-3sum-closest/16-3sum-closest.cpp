class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        
        int closestSum = nums[0] + nums[1] + nums[2];
        
        for(int m = 1; m < nums.size() - 1; m++){
            int i = 0, j = nums.size() - 1;
            while(i < m && j > m){
                int currSum = nums[i] + nums[m] + nums[j];
                if(abs(target - currSum) < abs(target - closestSum)){
                    closestSum = currSum;
                } 
                if(currSum < target){
                    i++;
                }else if(currSum > target){
                    j--;
                }else{
                    return currSum;
                }
            }
        }
        
        return closestSum;
    }
};