class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        long chalkPerCycle = 0;
        for(int c: chalk) chalkPerCycle+=c;
        cout << "chalkPerCycle" << chalkPerCycle << endl;
        while(k >= chalkPerCycle) k -= chalkPerCycle;
        cout << "k after subtractions" << k << endl;
        int idx = 0;
        k-=chalk[idx];
        cout << k << " " << idx << endl;
        while(k >= 0){
            idx++;
            k-=chalk[idx];
            if(k < 5)
                cout << k << " " << idx << endl;
        }
        return idx;
    }
};