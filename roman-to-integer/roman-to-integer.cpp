class Solution {
public:
    int romanToInt(string s) {
        unordered_map<string, int> hashmap; 
        hashmap["I"] = 1; 
        hashmap["V"] = 5; 
        hashmap["X"] = 10; 
        hashmap["L"] = 50; 
        hashmap["C"] = 100; 
        hashmap["D"] = 500; 
        hashmap["M"] = 1000; 
        hashmap["IV"] = 4; 
        hashmap["IX"] = 9; 
        hashmap["XL"] = 40; 
        hashmap["XC"] = 90;
        hashmap["CD"] = 400;
        hashmap["CM"] = 900;
        int decimal = 0;
        for(int i = 0 ; i < s.length(); i++){
            string curr = ""; curr += s[i];
            if(i < (s.length() - 1) ){
                string next = ""; next += s[i+1]; 
                if( hashmap[curr] < hashmap[next] ){
                    decimal += hashmap[curr+next];
                    i++; 
                }else{
                    decimal += hashmap[curr];
                } 
            }else{
                decimal += hashmap[curr];
            }
        }
        return decimal;
    }
};