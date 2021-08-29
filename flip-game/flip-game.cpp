class Solution {
public:
    vector<string> generatePossibleNextMoves(string currentState) {
        vector<string> solution;
        for(int i = 0 ; i < currentState.size() - 1; i++){
            if(currentState[i] == '+' && currentState[i+1] == '+'){
                solution.push_back(
                    currentState.substr(0,i) + "--" + currentState.substr(i+2, currentState.size())
                );
            }
        }
        return solution;
    }
};