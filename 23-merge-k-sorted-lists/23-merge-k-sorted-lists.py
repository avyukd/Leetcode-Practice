# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNodeWrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return id(self.node) < id(other.node)
        
class Solution:
    def mergeKLists(self, lists):
        # PQ solution
        pq = []
        for l in lists:
            if l is not None:
                heapq.heappush(pq, (l.val, ListNodeWrapper(l)))
        
        head = ListNode()
        tmp = head
        while pq:
            (nxt, l) = heapq.heappop(pq)
            l = l.node
            tmp.next = ListNode(nxt)
            tmp = tmp.next
            l = l.next
            if l is not None:
                heapq.heappush(pq, (l.val, ListNodeWrapper(l)))
        
        return head.next
        
        
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         head = None
#         for i in range(len(lists)):
#             head = self.mergeLists(head, lists[i])
#         return head
    
#     def mergeLists(self, list1, list2):
#         if list1 is None:
#             return list2
#         elif list2 is None:
#             return list1
        
#         p1, p2 = list1, list2
#         if p1.val <= p2.val:
#             tmp = p1
#             p1 = p1.next
#         else:
#             tmp = p2
#             p2 = p2.next
#         head = tmp
        
#         while p1 is not None and p2 is not None:
#             if p1.val <= p2.val:
#                 tmp.next = p1
#                 tmp = tmp.next
#                 p1 = p1.next
#             else:
#                 tmp.next = p2
#                 tmp = tmp.next
#                 p2 = p2.next
        
#         if p1 is not None:
#             tmp.next = p1
#         elif p2 is not None:
#             tmp.next = p2
        
#         return head