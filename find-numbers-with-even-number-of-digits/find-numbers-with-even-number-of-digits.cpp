class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int even_d_nums = 0;
        for(int n : nums){
            int num_digits = 0;
            while(n != 0){
                num_digits++;
                n /= 10;
            }
            if(num_digits % 2 == 0){
                even_d_nums += 1; 
            }
        }
        return even_d_nums; 
    }
};