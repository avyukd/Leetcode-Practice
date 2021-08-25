class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> charMap(128, 0);
        int left = 0; 
        int right = 0; 
        int longestSubstring = 0; 
        while(right < s.length()){
            charMap[s[right]]++;
            while(charMap[s[right]] > 1){
                charMap[s[left]]--;
                left++;
            }
            longestSubstring = max(longestSubstring, right-left+1);
            right++;
        }
        return longestSubstring; 
    }
};