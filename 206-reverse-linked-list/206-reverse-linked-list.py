# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head is None:
    #         return None
    #     elif head.next is None:
    #         return head
    #     rvrsd = self.reverseList(head.next)
    #     tmp = rvrsd
    #     while tmp.next is not None:
    #         tmp = tmp.next
    #     tmp.next = head
    #     head.next = None
    #     return rvrsd
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        back, front = None, head
        while front is not None:
            tmp = front.next
            front.next = back
            back = front
            front = tmp
        return back
            