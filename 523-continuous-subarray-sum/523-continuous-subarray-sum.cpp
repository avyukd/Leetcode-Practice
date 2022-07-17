class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> idxMap;
        idxMap[0] = -1;
        int cumSum = 0; 
        for(int i = 0 ; i < nums.size() ; ++i){
            cumSum += nums[i];
            if(idxMap.find(cumSum % k) != idxMap.end()){
                if(i - idxMap[cumSum % k] >= 2){
                    return true;
                }
            }else{
                idxMap[cumSum % k] = i;
            }
        }
        return false;
    }
};