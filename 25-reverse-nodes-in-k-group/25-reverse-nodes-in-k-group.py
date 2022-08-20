# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        listLen = 0
        tmp = head
        while tmp is not None:
            listLen += 1
            tmp = tmp.next
        
        def reverseHelper(head, grp):
            if grp == (listLen // k):
                return head
            prev, nxt = None, head
            start = head
            i = 0
            while i % k != 0 or i == 0:
                tmp = nxt.next
                nxt.next = prev
                prev = nxt
                nxt = tmp
                i += 1
            start.next = reverseHelper(nxt, grp + 1)
            return prev
        
        return reverseHelper(head, 0)
        