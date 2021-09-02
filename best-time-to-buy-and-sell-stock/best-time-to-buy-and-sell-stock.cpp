class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minBuy = prices[0];
        vector<int> memo(prices.size());
        memo[0] = -1;
        for(int i = 1 ; i < prices.size(); i++){
            memo[i] = prices[i] - minBuy; 
            minBuy = min(minBuy, prices[i]);
        }
        int maxProfit = 0; 
        for(int p : memo) maxProfit = max(p, maxProfit);
        return maxProfit; 
    }
};