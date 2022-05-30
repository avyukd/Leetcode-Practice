class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> leftProds = {};
        vector<int> rightProds(nums.size(), 0);
        
        int cumProd = 1; 
        for(int i = 0 ; i < nums.size(); i++){
            leftProds.push_back(cumProd);
            cumProd *= nums[i];
        }
        
        cumProd = 1; 
        for(int i = nums.size() - 1 ; i >= 0 ; i--){
            rightProds[i] = cumProd;
            cumProd *= nums[i];
        }
        
        vector<int> result(nums.size(), 0);
        for(int i = 0 ; i < nums.size(); i++){
            result[i] = leftProds[i] * rightProds[i];
        }
        
        return result;
        
    }
};