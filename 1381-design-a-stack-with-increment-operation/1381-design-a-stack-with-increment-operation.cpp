class CustomStack {
public:
    CustomStack(int maxSize) : capacity(maxSize), size(0), 
        s{}, increments(maxSize + 1, 0) {}
    
    void push(int x) {
        if(size + 1 <= capacity){
            s.push(x);
            ++size;
        }
    }
    
    int pop() {
        if(!s.empty()){
            int tmp = s.top() + increments[size]; s.pop();
            increments[size] = 0;
            --size;
            return tmp;
        }else{
            return -1;
        }
    }
    
    void increment(int k, int val) {
        for(int i = 1; i <= min(k, size); ++i)
            increments[i] += val;
    }

private:
    vector<int> increments;
    stack<int> s;
    int capacity;
    int size;
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */