# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1 get length of list
        tmp = head
        size = 0
        while tmp is not None:
            tmp = tmp.next
            size += 1
        
        # 2 put second half into stack
        stack = deque()
        tmp = head
        i = 0
        while i < (size / 2):
            tmp = tmp.next
            i += 1
        while tmp is not None:
            stack.append(tmp)
            tmp = tmp.next
        # 3 reorder the list
        tmphead = head
        while stack:
            nxt = tmphead.next
            toins = stack.pop()
            tmphead.next = toins
            toins.next = nxt
            tmphead = nxt
        tmphead.next = None
        return head