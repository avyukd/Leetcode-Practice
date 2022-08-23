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
    ListNode* sortList(ListNode* head) {
        if(!head || !head->next)
            return head;
        auto mid = getMid(head); // modifies head
        auto left = sortList(head);
        auto right = sortList(mid);
        return merge(left, right);
    }
    
    ListNode* merge(ListNode* left, ListNode* right){
        ListNode dummyHead(0);
        ListNode* curr = &dummyHead;        
        while (left && right) {
            if (left->val < right->val){
                curr->next = left;
                left = left->next;
            }else{
                curr->next = right;
                right = right->next;
            }
            
            curr = curr->next;
        }
        
        if(left){
            curr->next = left;
        }
        
        if(right){
            curr->next = right;
        }
        
        return dummyHead.next;
    }
    
    ListNode* getMid(ListNode* head) {
        ListNode* midPrev = nullptr;
        while (head && head->next) {
            midPrev = (midPrev == nullptr) ? head : midPrev->next;
            head = head->next->next;
        }
        ListNode* mid = midPrev->next;
        midPrev->next = nullptr;
        return mid;
    }
};