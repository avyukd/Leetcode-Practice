class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        int m = matrix.size();
        int n = matrix[0].size();
        
        int top = 0; 
        int bottom = m - 1;
        
        int row = 0;
        while(top <= bottom){
            int mid = (top + bottom) / 2;
            int start = matrix[mid][0], end = matrix[mid][n - 1];
            if(target >= start && target <= end){
                row = mid;
                break;
            }else if(target < start){
                bottom = mid - 1;
            }else{
                top = mid + 1;
            }
        }
        
        int left = 0; 
        int right = n - 1;
        
        while(left <= right){
            int mid = (left + right) / 2;
            int curr = matrix[row][mid];
            if(curr < target){
                left = mid + 1;
            }else if(curr > target){
                right = mid - 1;
            }else{
                return true;
            }
        }
        
        return false;
    }
};