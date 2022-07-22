class Solution {
public:
    string longestPalindrome(string s) {
        string maxSubstring(1, s[0]);
        if(s.length() <= 1) return s;
        for(int i = 0 ; i < s.length()-1; i++){
            string p1 = palindromeAroundCenter(s, i, i);
            string p2 = palindromeAroundCenter(s, i, i+1);
            string longest = (p1.length() > p2.length()) ? p1 : p2; 
            if(longest.length() > maxSubstring.length()) 
                maxSubstring = longest; 
        }
        return maxSubstring;
    }
    
private:
    string palindromeAroundCenter(string &s, int left, int right){
        while(right < s.length() && left >= 0 && s[left] == s[right]){
            left--;
            right++;
        }
        return s.substr(left+1, right-(left+1));
    }
};