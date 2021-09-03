class Solution {
public:
    int trap(vector<int>& height) {
        
        if(height.size() <= 2 || 
           is_sorted(height.begin(), height.end())
        ) return 0;
        
        int maxRain = 0; 
        
        for(int i = 0 ; i < height.size(); i++){
            //for the ith element, get max left, max right
            int maxLeft = 0; 
            for(int left = 0; left < i; left++){
                maxLeft = max(height[left], maxLeft);
            }
            int maxRight = 0; 
            for(int right = i+1; right < height.size(); right++){
                maxRight = max(height[right], maxRight);
            }
            if(maxLeft > height[i] && maxRight > height[i]){
                maxRain += min(maxRight, maxLeft) - height[i];
            }
        }
        return maxRain; 
        /*
        try a column by column solution?
        basically an O(n) solution
        
        int maxLeftBlockIdx = -1;
        int maxLeftBlockHeight = 0; 
        vector<int> memo(height.size(), 0); 
        for(int i = 0 ; i < height.size(); i++){
            if(height[i] > maxLeftBlockHeight){
                memo[i] = maxLeftBlockIdx; 
                maxLeftBlockHeight = height[i];
                maxLeftBlockIdx = i; 
            }else{
                memo[i] = maxLeftBlockIdx; 
            }
        }
        for(int i = height.size() - 1 ; i >= 0; i++){
            
        }
        
        return 0; */
        /* iterating row over row
            too slow with large input
        //get max height
        int maxHeight = height[0];
        for(auto h : height) maxHeight = max(maxHeight, h);
        //iterate row over row
        int i = 1; 
        int maxRain = 0; 
        while(i <= maxHeight){
            //iterate over current row
            int left = -1; 
            for(int j = 0; j < height.size(); j++){
                if(height[j] > 0){
                    //found a block 
                    if(left != -1){
                        maxRain += ( (j - 1) - left );
                    }
                    left = j; 
                }
                height[j]--;
            }
            i++;
        }
        return maxRain; */
    }
};