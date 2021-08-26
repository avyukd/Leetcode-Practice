class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string longestPrefix = "";
        for(int i = 0 ; i < strs[0].length(); i++){
            auto curr_char = strs[0][i];
            for(int j = 1 ; j < strs.size(); j++){
                if(i >= strs[j].length() || strs[j][i] != curr_char){
                    return longestPrefix;
                }
            }
            longestPrefix+=curr_char; 
        }
        return longestPrefix;     
    }
};