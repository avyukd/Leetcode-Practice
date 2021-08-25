class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, bool> freq;
        for(int i = 0; i < nums.size(); i++){
            if(freq.find(nums[i])==freq.end()){
                freq[nums[i]] = true;
            }else{
                return true; 
            }
        }
        return false; 
    }
};