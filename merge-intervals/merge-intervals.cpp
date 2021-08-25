class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> solution; 
        sort(intervals.begin(), intervals.end(), 
            [](const vector<int>& a, const vector<int>& b) -> bool{
                return a[0] < b[0];
            }
        );
        solution.push_back(intervals[0]);
        int solution_idx = 0; 
        for(int i = 1 ; i < intervals.size(); i++){
            if(intervals[i][0] <= solution[solution_idx][1]){
                solution[solution_idx][1] = max(intervals[i][1], solution[solution_idx][1]);
            }else{
                solution.push_back(intervals[i]);
                solution_idx++;
            }
        }
        return solution;
    }
};