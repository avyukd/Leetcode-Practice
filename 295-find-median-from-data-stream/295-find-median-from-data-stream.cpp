class MedianFinder {
    priority_queue<int, vector<int>, greater<int>> minHeap;
    priority_queue<int, vector<int>, less<int>> maxHeap;
public:
    MedianFinder(){}
    
    void addNum(int num) {
        if(maxHeap.empty()){
            maxHeap.push(num);
        }else{
            int left = maxHeap.top();
            if(num <= left){
                maxHeap.push(num);
            }else{
                minHeap.push(num);
            }
        }
        if( ((int) maxHeap.size() - (int) minHeap.size()) > 1){
            minHeap.push(maxHeap.top()); maxHeap.pop();
        }
        if( ((int) minHeap.size() - (int) maxHeap.size()) > 1){
            maxHeap.push(minHeap.top()); minHeap.pop();
        }
    }
    
    double findMedian() {
        if(minHeap.size() > maxHeap.size()){
            return minHeap.top() / 1.0;
        }else if(minHeap.size() < maxHeap.size()){
            return maxHeap.top() / 1.0;
        }else{
            return (minHeap.top() + maxHeap.top()) / 2.0;
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */