class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> solution(2);
        unordered_map<int, int> m; 
        for(int i = 0 ; i < nums.size(); i++){
            if(m.find(nums[i]) != m.end()){
                solution[0] = i; 
                solution[1] = m[nums[i]];
                return solution;
            }else{
                m[target-nums[i]] = i;
            }
        }
        return solution;
    }
};