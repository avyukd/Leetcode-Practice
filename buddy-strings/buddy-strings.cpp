class Solution {
public:
    bool buddyStrings(string s, string goal) {
        //O(n) solution
        //go through both strings, keep track of number of differences
        //if exactly two differences, then you can swap
        //if 1 or >2 differences, then you can't swap
        //if no differences, see if characters repeat
        
        if(s.length() != goal.length()) return false;
        
        unordered_set<char> chars; 
        int diff1 = -1; int diff2 = -1;
        
        int i = 0; 
        while(i < s.length()){
            if(s[i] != goal[i]){
                //there's a difference
                if(diff1 == -1 && diff2 == -1){
                    //no differences seen yet
                    diff1 = i; 
                }else if(diff1 != -1 && diff2 == -1){
                    //one difference seen
                    diff2 = i;
                }else if(diff1 != -1 && diff2 != -1){
                    //two differences already
                    //another one means swap not possible
                    return false; 
                }
            }
            chars.insert(s[i]);
            i++;
        }
        if(diff1 != -1 && diff2 != -1){
            //check if swap will work
            return s[diff1] == goal[diff2] && s[diff2] == goal[diff1];
        }else if( (diff1 == -1 || diff2 == -1) && (diff1 != -1 || diff2 != -1) ) {
            //only one difference
            return false;
        }
        cout << chars.size() << endl; 
        return chars.size() < goal.length();
    }
};