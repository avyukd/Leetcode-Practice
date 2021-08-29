class MyQueue {
private:
    stack<int> stackFront;
    stack<int> stackBack;
public:
    /** Initialize your data structure here. */
    MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        stackBack.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if(stackFront.empty()){
            while(!stackBack.empty()){
                stackFront.push(stackBack.top());
                stackBack.pop();
            }
        }
        
        int toRet = stackFront.top();
        stackFront.pop();
        return toRet;
    }
    
    /** Get the front element. */
    int peek() {
        if(stackFront.empty()){
            while(!stackBack.empty()){
                stackFront.push(stackBack.top());
                stackBack.pop();
            }
        }
        return stackFront.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return stackFront.empty() && stackBack.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */