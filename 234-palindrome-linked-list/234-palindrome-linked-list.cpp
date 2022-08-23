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
    bool isPalindrome(ListNode* head) {
        // get length of linked list
        int len = 0;
        auto tmp = head;
        while(tmp){
            tmp = tmp->next;
            ++len;
        }
        
        // get halfway -- get to this point, reverse after, comp
        int half = len / 2;
        
        tmp = head; int i = 0;
        while(i < half){
            tmp = tmp->next;
            i++;
        }
         
        ListNode* prev = nullptr;
        ListNode* nxt = tmp;

        while(nxt){
            tmp = nxt->next;
            nxt->next = prev;
            prev = nxt; 
            nxt = tmp;
        }
        
        ListNode* revHead = prev;
                
        i = 0; tmp = head; 
        while(i < half){
            cout << tmp->val << " " << revHead->val << endl;
            if(revHead->val != tmp->val){
                return false;
            }
            revHead = revHead->next;
            tmp = tmp->next;
            ++i;
        }
        
        return true;
    }
};