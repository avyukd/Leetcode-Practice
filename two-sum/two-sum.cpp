class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        /*
            Explanation: We need to find two numbers in the array that sum to target.
            We can use a hashmap to store their value and indices.
            The value stored in the hashmap is target - current value.
            If the current value is in the hashmap, that means its complement is in the array.
            Thus, we have found the two numbers. 
        */
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