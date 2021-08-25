class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if(nums.size()==1 || nums.size()==0){
            return;
        }
        //take out extra rotations
        while(k > nums.size()){
            k-=nums.size();
        }
        vector<int> rotatedPart(k);
        for(int i = nums.size() - k; i < nums.size(); i++){
            rotatedPart[i - (nums.size() - k)] = nums[i];
        }
        //shiftRight
        for(int j = nums.size() - 1; j >= k; j--){
            nums[j] = nums[j-k];
        }
        //add back rotatedPart
        for(int x = 0; x < k; x++){
            nums[x] = rotatedPart[x];
        }
    }
};