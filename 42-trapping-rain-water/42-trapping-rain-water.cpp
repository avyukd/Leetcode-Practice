class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        
        if(n < 3)
            return 0;
        
        vector<int> left(n), right(n);
        
        int currMax = 0;
        for(int i = 0 ; i < n; i++){
            left[i] = currMax;
            currMax = max(height[i], currMax);
        }
        
        currMax = 0;
        for(int i = n - 1; i >= 0; i--){
            right[i] = currMax;
            currMax = max(height[i], currMax);
        }
        
        int trapped = 0;
        for(int i = 1; i < n - 1; i++){
            trapped += max(min(left[i], right[i]) - height[i], 0);
        }
        
        return trapped;
    }
};