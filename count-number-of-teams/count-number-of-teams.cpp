class Solution {
public:
    int numTeams(vector<int>& rating) {
        
        //O(n^2) solution
        //keep track of how many teams are greater and less on the left and right of each index
        //then left[greater]*right[less] is number of triplets in descending order
        //right[greater]*left[less] is number of triplets in ascending order
        
        int res = 0; 
        
        for(int i = 1 ; i < rating.size()-1; i++){
            
            size_t left_less = 0;
            size_t right_less = 0;
            size_t right_greater = 0;
            size_t left_greater = 0;
            
            for(int j = 0 ; j < rating.size() ; j++){
                if(j < i){
                    //left
                    if(rating[j] < rating[i]){
                        left_less++;
                    }else{
                        //rating values are unique 
                        left_greater++;
                    }
                }else if(j > i){
                    //right
                    if(rating[j] < rating[i]){
                        right_less++;
                    }else{
                        right_greater++;
                    }
                }

            }
            
            res += right_less*left_greater + left_less*right_greater;
            
        }
        
        return res; 
        
        
        /*
        
        brute force solution:
        
        int numTeams = 0;
        for(int i = 0 ; i < rating.size(); i++){
            for(int j = i + 1; j < rating.size(); j++){
                for(int k = j + 1; k < rating.size(); k++){
                    if(i < j && j < k){
                        if( (rating[i] < rating[j] && rating[j] < rating[k]) ||
                            (rating[i] > rating[j] && rating[j] > rating[k])
                          ){
                            numTeams++;
                        }
                    }
                }
            }
        }
        return numTeams;*/
    }
};