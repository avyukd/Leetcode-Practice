class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        if(s1.length() + s2.length() != s3.length())
            return false;
        
        vector<vector<bool>> memo(s1.size() + 1, vector<bool>(s2.size() + 1, 1));
        return recurse(s1, s2, s3, 0, 0, memo);
    }
    
    bool recurse(string& s1, string& s2, string& s3, int i1, int i2, vector<vector<bool>>& memo){
        if(i1 + i2 == s3.length())
            return true;
        
        if(!memo[i1][i2])
            return false;
        
        if(i1 < s1.length() && s1[i1] == s3[i1 + i2])
            if(recurse(s1, s2, s3, i1 + 1, i2, memo))
                return true;

        if(i2 < s2.length() && s2[i2] == s3[i1 + i2])
            if(recurse(s1, s2, s3, i1, i2 + 1, memo))
                return true;
        
        memo[i1][i2] = false;
        return memo[i1][i2];
    }
};