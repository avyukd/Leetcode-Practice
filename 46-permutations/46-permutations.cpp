class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> perms = {};
        genPerms(0, nums, perms);
        return perms;
    }
    
    void genPerms(int i, vector<int>& curr, vector<vector<int>>& perms) {
        if(i == curr.size()){
            perms.push_back(curr);
            return;
        }
        
        for(int j = i; j < curr.size(); ++j){
            swap(curr[i], curr[j]);
            genPerms(i + 1, curr, perms);
            swap(curr[j], curr[i]);
        }
    }
};