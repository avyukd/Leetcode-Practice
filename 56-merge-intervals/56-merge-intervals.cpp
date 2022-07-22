class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        
        vector<vector<int>> merged;
        merged.push_back(intervals[0]);
        for(auto &interval: intervals){
            if(merged[merged.size() - 1][1] >= interval[0]){
                merged[merged.size() - 1][1] = max(merged[merged.size() - 1][1], interval[1]);
            }else{
                merged.push_back(interval);
            }
        }
        return merged;
    }
};