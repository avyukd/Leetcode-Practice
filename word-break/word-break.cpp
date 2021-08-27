class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp(s.size()+1, false);
        dp[0] = true;
        
        // we mark as true every index that we managed to segment so far
        for (int i = 1; i <= s.size(); i++)
            for (int j = 0; j < i; j++)
                if ((dp[j]) && (find(wordDict.begin(), wordDict.end(), s.substr(j, i-j)) != wordDict.end())) {
                    dp[i] = true;
                    break;
                }
        return dp.back();
    }
    
    /*unordered_map<string, bool> memo; 
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_map<string, int> memo;
        return wordBreakHelper(s, wordDict, memo);
    }
    
    bool wordBreakHelper(string s, vector<string>& wordDict, unordered_map<string, int> &memo){
        if(s == "") return true; 
        int i = 1;
        bool breakable = false;
        while(i <= s.length()){
            string searchWord = s.substr(0, i);
            bool wordValid = false;
            if(memo.find(searchWord) == memo.end()){
                for(auto &w : wordDict){
                    if(w == searchWord) {
                        wordValid = true; 
                        break;
                    } 
                }
                memo[searchWord] = wordValid; 
            }else{
                wordValid = memo[searchWord];
            }
            
            if(wordValid){
                breakable = wordBreakHelper(s.substr(i, s.length()), wordDict, memo); 
                memo[s.substr(i, s.length())] = breakable;
            }
            if(breakable) return true; 
            i++;
        }
        return breakable;
    }*/
};