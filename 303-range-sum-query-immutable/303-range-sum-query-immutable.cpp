class NumArray {
    vector<int> cumSum; 
public:
    NumArray(vector<int>& numsIn) : cumSum(numsIn.size()+1, 0) {
        int curr = 0;
        for(int i = 0 ; i < numsIn.size(); i++){
            curr += numsIn[i];
            cumSum[i+1] = curr;
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