class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int, deque<int>, less<int>> pq(stones.begin(), stones.end());
        while(pq.size() >= 2){
            auto first = pq.top(); pq.pop();
            if(pq.empty()){
                return first;
            }
            auto second = pq.top(); pq.pop();
            if(first != second){
                pq.push(first - second);
            }
        }
        if(pq.size() == 1){
            return pq.top();
        }else{
            return 0;
        }
    }
};