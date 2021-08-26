class Solution {
public:
    bool isValid(string s) {
        stack<char> helper;
        for(char next_c : s){
            if(next_c == '(' || next_c == '[' || next_c == '{'){
                helper.push(next_c);
            }else{
                if(helper.empty()) return false;
                char top = helper.top();
                if(next_c == ')'){
                    if(top == '('){
                        helper.pop();
                    }else{
                        return false; 
                    }
                }else if(next_c == ']'){
                    if(top == '['){
                        helper.pop();
                    }else{
                        return false; 
                    }
                }else{
                    if(top == '{'){
                        helper.pop();
                    }else{
                        return false; 
                    }
                }
            }
        }
        if(!helper.empty()) return false;
        return true;
    }
};