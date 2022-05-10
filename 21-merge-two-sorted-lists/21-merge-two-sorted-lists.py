# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        p1, p2 = list1, list2
        
        if p1.val < p2.val:
            tmp = p1
            p1 = p1.next
        else:
            tmp = p2
            p2 = p2.next
            
        head = tmp
        
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                tmp.next = p1
                tmp = tmp.next
                p1 = p1.next
            else:
                tmp.next = p2
                tmp = tmp.next
                p2 = p2.next
        
        if p1 is not None:
            tmp.next = p1
        
        if p2 is not None:
            tmp.next = p2
        
        return head