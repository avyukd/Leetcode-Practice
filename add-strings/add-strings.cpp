class Solution {
public:
    string addStrings(string num1, string num2) {
        int i = 1; 
        string result = "";
        bool carryOver = 0; 
        while( i <= max(num1.length(), num2.length()) ){
            int d1 = 0;
            int d2 = 0; 
            if( ( (int) num1.length() - i) >= 0 ){
                d1 = num1[num1.length() - i] - '0';
            }
            if( ( (int) num2.length() - i) >= 0 ){
                d2 = num2[num2.length() - i] - '0';
            }
            
            
            int sum = d1 + d2 + carryOver; 
            if(sum >= 10){
                carryOver = 1; 
                sum %= 10; 
            }else{
                carryOver = 0;
            }
            result = to_string(sum) + result;
            i++;
        }
        
        if(carryOver){
            result = "1" + result; 
        }
        
        return result; 
    }
};