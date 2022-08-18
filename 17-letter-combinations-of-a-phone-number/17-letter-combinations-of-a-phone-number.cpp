class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if(digits == "")
            return {};
        
        vector<string> combs;
        
        unordered_map<int, vector<char>> digitMap;
        initDigitMap(digitMap);
        
        backtrack(0, digits, "", combs, digitMap);
        
        return combs;
    }
    
    void backtrack(int i, const string digits, string comb, vector<string>& combs, unordered_map<int, vector<char>> digitMap){
        if(i == digits.length()){
            combs.push_back(comb);
            return;
        }
        
        vector<char> validLetters = digitMap[digits[i] - '0'];
        
        for(auto ch: validLetters){
            string newComb = comb + ch;
            backtrack(i + 1, digits, newComb, combs, digitMap);
        }
    }
    
    void initDigitMap(unordered_map<int, vector<char>>& digitMap){
        digitMap[2] = {'a', 'b', 'c'};
        digitMap[3] = {'d', 'e', 'f'};
        digitMap[4] = {'g', 'h', 'i'};
        digitMap[5] = {'j', 'k', 'l'};
        digitMap[6] = {'m', 'n', 'o'};
        digitMap[7] = {'p', 'q', 'r', 's'};
        digitMap[8] = {'t', 'u', 'v'};
        digitMap[9] = {'w', 'x', 'y', 'z'};
    }
};