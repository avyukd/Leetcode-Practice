class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> solution;
        if(n == 0){
            solution.push_back("");
        }else{
            for(int c = 0; c < n; c++){
                for(string left: generateParenthesis(c)){
                    for(string right: generateParenthesis(n-1-c)){
                        solution.push_back("("+left+")"+right);
                    }
                }
            }
        }
        return solution;
        /*if(n == 1){
            vector<string> s(1); 
            s[0] = "()";
            return s; 
        }
        
        vector<unordered_set<string>> memo(n+1); 
        unordered_set<string> base; base.insert("()");
        memo[1] = base;
        
        for(int i = 2; i <= n; i++){
            unordered_set<string> next; 
            for(auto it: memo[i-1]){
                next.insert("(" + it +")");
                next.insert("()" + it);
                next.insert(it + "()");
            }
            memo[i] = next; 
        }
        vector<string> sol; 
        for(auto it: memo[n]) sol.push_back(it);
        return sol;*/
    }
};