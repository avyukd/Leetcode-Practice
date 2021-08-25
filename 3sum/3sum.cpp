class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> solutions; 
        if(nums.size() < 3){
            return solutions;
        }
        sort(nums.begin(), nums.end());
        //i, j, and k
        //i increments by 1
        //j,k is two pointer technique
        for(size_t i = 0; i < nums.size() - 2; i++){
            if(i==0 || nums[i] != nums[i-1]){
                size_t left = i+1;
                size_t right = nums.size() - 1;
                while(left < right){
                    auto sum = nums[i] + nums[left] + nums[right];
                    if(sum < 0){
                        left++;
                    }else if(sum > 0){
                        right--;
                    }else{
                        vector<int> solution(3);
                        solution[0] = nums[i];
                        solution[1] = nums[left];
                        solution[2] = nums[right]; 
                        solutions.push_back(solution);
                        left++;
                        while(left < right && nums[left] == nums[left-1]){
                            left++;
                        }
                        right--;
                    }
                }
            }
        }
        return solutions;
    }
};