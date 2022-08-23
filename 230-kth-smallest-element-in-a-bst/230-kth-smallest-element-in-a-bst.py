# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        cnt = 0
        kthSmall = None
        def traverse(node):
            nonlocal cnt, kthSmall
            if node is not None and cnt < k:
                traverse(node.left)
                cnt += 1
                if cnt == k:
                    kthSmall = node.val
                traverse(node.right)
        
        traverse(root)
        return kthSmall
        