/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode * p = l1;
        ListNode * q = l2; 
        ListNode * dummy = new ListNode(0);
        ListNode * curr = dummy;
        int carryOver = 0;
        while( !(p == nullptr && q == nullptr) ){
            if(p == nullptr) p = new ListNode(0);
            if(q == nullptr) q = new ListNode(0);
            int sum = p->val + q->val + carryOver; 
            carryOver = sum/10;
            if(carryOver > 0) sum-=10;
            ListNode * n = new ListNode(sum);
            curr->next = n; 
            curr = curr->next; 
            p = p->next;
            q = q->next;
        }
        if(carryOver != 0){
            curr->next = new ListNode(carryOver);
        }
        return dummy->next; 
    }
};