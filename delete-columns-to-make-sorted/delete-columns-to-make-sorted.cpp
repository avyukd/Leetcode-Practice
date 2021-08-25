class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        if(strs.size() <= 1){
            return 0; 
        }
        int num_columns_delete = 0;
        int str_length = strs[0].length();
        for(int col = 0 ; col < str_length; col++){
            for(int row = 1 ; row < strs.size() ; row++){
                char curr_letter = strs[row][col]; 
                if(curr_letter < strs[row-1][col]){
                    num_columns_delete++; 
                    break;
                }
            }
        }
        return num_columns_delete;
    }
};