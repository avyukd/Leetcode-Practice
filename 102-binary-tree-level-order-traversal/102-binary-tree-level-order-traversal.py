# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        levels = []
        queue = deque([root])
        while queue:
            levels.append([q.val for q in queue])
            s = len(queue)
            for _ in range(s):
                nxt = queue.popleft()
                if nxt.left:
                    queue.append(nxt.left)
                if nxt.right:
                    queue.append(nxt.right)
        return levels