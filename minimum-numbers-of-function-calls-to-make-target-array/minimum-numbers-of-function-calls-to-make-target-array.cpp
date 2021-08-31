class Solution {
public:
    int minOperations(vector<int>& nums) {
        //see bit count solution in discussion -- very cool
        
        int maxBits = 1; 
        int minAddByOnes = 0;
        
        for(int num : nums){
            if(num == 0) continue; 
            std::bitset<64> bs(num);
            string bitstring = bs.to_string();
            int i = 0;
            while(bitstring[i] == '0' && i != bitstring.length()){
                i++;
            }
            maxBits = max(maxBits, (int) bitstring.length() - i);
            while(i != bitstring.length()){
                if(bitstring[i] == '1') minAddByOnes++;
                i++;
            }
        }
        
        return minAddByOnes + maxBits - 1; 
        
        
        /*int totalCalls = 0;
        int sumOfNums = 0;
        for(auto &n : nums) sumOfNums+=n;
        while(sumOfNums != 0){
            for(auto &n : nums){
                if(n % 2 == 1){
                    n--;
                    totalCalls++;
                }
            }
            int i = 0;
            int minHalfs = 0;
            while(i < nums.size() && nums[i] == 0){
                i++;
            }
            if(i>=nums.size()) return totalCalls;
            int nu = nums[i];
            while(nu % 2 == 0){
                nu/=2; minHalfs++;
            }
            while(i < nums.size() - 1){  
                if(nums[i]!=0){
                    int doubles = 0;
                    int nu = nums[i];
                    while(nu % 2 == 0){
                        nu/=2; doubles++;
                    }
                    minHalfs = min(doubles, minHalfs);
                }
                i++;
            }
            totalCalls += minHalfs;
            for(auto &n : nums) n/=pow(2, minHalfs);
            for(auto n : nums) cout << n;
            cout << endl;
        }
        return totalCalls;*/
    }
};