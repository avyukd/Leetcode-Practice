# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        tmp = head
        while tmp is not None:
            if id(tmp) in visited:
                return True
            else:
                visited.add(id(tmp))
            tmp = tmp.next
        return False