# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        if head is None:
            return False
        slow, fast = head, head.next
        while fast is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next
        return False
    
    
    
    
    
    
    
#     # O(1) solution
#     def hasCycle(self, head) -> bool:
#         slow, fast = head, head
        
#         if slow.next is None:
#             return False
        
#         while slow is not None and fast is not None:
            
#             slow = slow.next
#             fast = fast.next
#             if fast is not None:
#                 fast = fast.next
            
#             if id(slow) == id(fast):
#                 return True

        
#         return False
# #     def hasCycle(self, head: Optional[ListNode]) -> bool:
# #         visited = set()
# #         tmp = head
# #         while tmp is not None:
# #             if id(tmp) in visited:
# #                 return True
# #             else:
# #                 visited.add(id(tmp))
# #             tmp = tmp.next
# #         return False