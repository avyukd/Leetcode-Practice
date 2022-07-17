class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res = {};
        permuteHelper(0, nums, res);
        return res;
    }
    
    void permuteHelper(int start, vector<int>& nums, vector<vector<int>>& res) {
        if(start == nums.size()){
            res.push_back(nums);
            return;
        }
        for(int i = start; i < nums.size(); i++){
            swap(nums[i], nums[start]);
            permuteHelper(start + 1, nums, res);
            swap(nums[i], nums[start]);
        }
    }
};