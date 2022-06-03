class NumArray {
    vector<int> cumSum; 
public:
    NumArray(vector<int>& numsIn) {
        int curr = 0;
        cumSum.push_back(0);
        for(int i = 0 ; i < numsIn.size(); i++){
            curr += numsIn[i];
            cumSum.push_back(curr);
        }
    }
    
    int sumRange(int left, int right) {
        return cumSum[right+1] - cumSum[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */