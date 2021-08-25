class Solution {
public:
    bool isPalindrome(int x) {
        //revert last half of number
        if(x < 0 || (x != 0 && x%10 == 0)) return false; 
        int revHalf = 0;
        while(x > revHalf){
            revHalf = revHalf * 10 + x%10;
            x/=10;
        }
        return (x == revHalf) || (x == revHalf/10);
        return true;
        
        /*if(x < 0) return false; 
        int numDigits = 0; 
        int helper = x;
        while(helper != 0){
            helper/=10;
            numDigits++;
        }
        int helper2 = x; 
        int left = x / (pow(10, numDigits-1));
        int right = helper2 % 10; 
        for(int i = 1 ; i <= numDigits/2; i++){
            if(left != right)
                return false; 
            left = (int) (x / pow(10, (numDigits-1-i) )) % 10;
            helper2/=10; 
            right = helper2 % 10; 
        }
        return true; */
    }
};