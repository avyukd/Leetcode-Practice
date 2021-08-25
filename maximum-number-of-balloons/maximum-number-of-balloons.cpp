class Solution {
public:
    int maxNumberOfBalloons(string text) {
        //balloon
        //b=0, a=1, l=2, o=3, n=4
        int b = 0;
        int a = 0;
        int l = 0; 
        int o = 0;
        int n = 0;
        for(char &c: text){
            if(c == 'b'){
                b++;
            }else if(c == 'a'){
                a++;
            }else if(c == 'l'){
                l++;
            }else if(c == 'o'){
                o++;
            }else if(c=='n'){
                n++;
            }
        }
        l/=2;
        o/=2;
        int num_balloons = 
            min(b, min(a, min(l,min(o,n))));
        return num_balloons;
    }
};