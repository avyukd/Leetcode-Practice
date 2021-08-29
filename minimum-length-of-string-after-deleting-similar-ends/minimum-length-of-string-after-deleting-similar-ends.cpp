class Solution {
public:
    int minimumLength(string s) {
        int start = 0; 
        int end = s.length() - 1;
        while(s[start] == s[end] && start < end){
            //compare everything to this
            char c = s[start];
            while(s[start] == c && start <= end) start++;
            while(s[end] == c && end >= start) end--;
        }
        return (end+1)-start;
    }
};