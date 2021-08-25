class Solution {
public:
    vector<double> sampleStats(vector<int>& count) {
        vector<double> solution(5);  
        
        int minIdx = 0; 
        while(count[minIdx] == 0) minIdx++;
        solution[0] = minIdx;
        
        int maxIdx = count.size() - 1;
        while(count[maxIdx] == 0) maxIdx--;
        solution[1] = maxIdx;
        
        double sumOfElements = 0;
        double numElements = 0;
        int maxElIdx = 0;
        int maxFreq = 0; 
        for(int i = 0; i < count.size(); i++){
            sumOfElements += (double) i * count[i];
            numElements += count[i];
            if(count[i] > maxFreq){
                maxFreq = count[i];
                maxElIdx = i;
            }
        }
        solution[2] = sumOfElements / numElements; 
        
        solution[4] = maxElIdx; 
        
        int newNumCount = 0; 
        int leftMedian = 0;
        for (int i = 0; i < count.size(); ++i) {
            newNumCount += count[i];
            if (newNumCount >= numElements / 2) {
                leftMedian = i;
                break;
             }
        }
        newNumCount = 0;
        int rightMedian = 0;
        for(int i = count.size() - 1; i>=0; i--){
            newNumCount += count[i];
            if(newNumCount >= numElements/2){
                rightMedian = i;
                break;
            }
        }
        
        solution[3] = ( (double) (rightMedian + leftMedian) ) / 2;
        
        return solution;
    }
};