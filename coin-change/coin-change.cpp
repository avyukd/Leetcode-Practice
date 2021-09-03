class Solution {
public:
    unordered_map<int, int> memo; 
    int coinChange(vector<int>& coins, int amount) {
        if(amount == 0) return 0;
        if(find(coins.begin(), coins.end(), amount) != coins.end()){
            return 1; 
        }
        int minNumber = INT_MAX;
        for(int coin : coins){
            if( (amount - coin) > 0){
                int n; 
                if(memo.find(amount-coin) != memo.end()){
                    n = memo[amount-coin];
                }else{
                    n = coinChange(coins, amount - coin);
                }
                if(n != -1){
                    minNumber = min(n, minNumber);
                }
            }
        }
        if(minNumber == INT_MAX){
            memo[amount] = -1;
            return -1; 
        }else{
            memo[amount] = minNumber+1; 
            return minNumber+1;
        }
    }
};