# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length of list
        listlen = 0
        tmp = head
        while tmp is not None:
            tmp = tmp.next
            listlen += 1
        
        if listlen <= 1:
            return None
        
        pos = listlen - n
        if pos == 0:
            return head.next
        tmp = head
        i = 0
        while i < pos - 1:
            tmp = tmp.next
            i += 1
        tmp.next = tmp.next.next
        return head