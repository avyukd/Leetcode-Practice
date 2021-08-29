class Solution {
public:
    int consecutiveNumbersSum(int x) {
        //idea 3 -- check the math on this later
        int total = 1;
        for(int n = 2 ; n <= sqrt(2 * x); n++){
            if( (2 * x) % n == 0){
                if( ( (2 * x) / n ) > (n-1) ){
                    if( ( ( (2 * x) / n ) - (n-1) ) % 2 == 0){
                        total++;
                    }
                }else{
                    break;
                }
            }
        }
        
        /*
        idea: precalculate sums
        unordered_set<int> sums; //sums starting with 1
        for(int i = 2; i <= (n/2 + 1); i++){
            sums.insert( ( ( i * (i+1) ) / 2 ) - i);
        }
        for(int a0 = 1; a0 <= n/2; a0++){
            
        }*/
        /*
        int total = 1;
        for(int a0 = 1; a0 <= n/2; a0++){
            for(int i = 1; i <= (n/2 + 1) ; i++){
                //a0 is the start term
                //i is the number of consec pos integers
                long sum = ( ( (long) i * (long) ( i + 1 )) / 2 ) + (long) i * (long) (a0 - 1);
                if( (long) n == sum){
                    total++;
                    break;
                }else if( (long) n < sum){
                    break;
                }
            }
        }
        */
        return total;
    }
};