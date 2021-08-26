class MinStack {
public:
    /** initialize your data structure here. */
    stack<int> minStack;
    int currentMin; 
    MinStack() {
        currentMin = INT_MAX; 
    }
    
    void push(int val) {
        minStack.push(val);
        currentMin = min(val, currentMin);
    }
    
    void pop() {
        if(minStack.top() == currentMin){
            minStack.pop();
            //find new min
            stack<int> aux; 
            currentMin = INT_MAX;
            while(!minStack.empty()){
                aux.push(minStack.top());
                currentMin = min(minStack.top(), currentMin);
                minStack.pop();
            }
            while(!aux.empty()){
                minStack.push(aux.top());
                aux.pop();
            }
        }else{
            minStack.pop();
        }
    }
    
    int top() {
        return minStack.top();
    }
    
    int getMin() {
        return currentMin;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */