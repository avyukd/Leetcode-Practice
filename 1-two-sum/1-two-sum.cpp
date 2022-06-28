class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> dict; 
        for(int i = 0; i < nums.size(); i++){
            if(dict.find(target - nums[i]) != dict.end()){
                auto ret = {dict[target - nums[i]], i};
                return ret;
            }else{
                dict[nums[i]] = i;
            }
        }
        return {};
    }
};