class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res = {};
        vector<int> subset = {};
        combinationSumHelper(candidates, 0, target, subset, res);
        return res;
    }
    
    void combinationSumHelper(vector<int>& candidates, int start, int curr, vector<int> &subset, vector<vector<int>>& result){
        if(curr == 0){
            result.push_back(subset);
        }else if(curr < 0){
            return;
        }
        
        for(int i = start; i < candidates.size(); ++i){
            subset.push_back(candidates[i]);
            combinationSumHelper(candidates, i, curr - candidates[i], subset, result);
            subset.pop_back();
        }
    }
};