class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        //hashmap keeps track of maximum value at every index going from right to left
        unordered_map<int, int> max_values;
        max_values[arr.size() - 2] = arr[arr.size() - 1];
        for(int i = arr.size() - 3; i >= 0; i--){
            max_values[i] = max(max_values[i+1], arr[i+1]);
        }
        for(int i = 0 ; i < arr.size() - 1; i++){
            arr[i] = max_values[i];
        }
        arr[arr.size() - 1] = -1; 
        return arr; 
        /*for(int i = 0 ; i < arr.size() - 1; i++){
            int maxV = arr[i+1];
            for(int j = i+1; j < arr.size(); j++){
                maxV = max(maxV, arr[j]);
            }
            arr[i] = maxV; 
        }
        arr[arr.size() - 1] = -1;
        return arr; */
    }
};