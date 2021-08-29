class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        //using kmp
        int n = s.length();
        vector<int> memo(n+1, 0);
        int i = 1; int j = 0; 
        while(i < n){
            if(s[i] == s[j]){
                memo[++i] = ++j;
            }else{
                if(j == 0){
                    ++i;
                }else{
                    j = memo[j];
                }
            }
        }
        return (memo[n] != 0) && ( (memo[n] % (n - memo[n]) == 0) ); 
        
    }
};