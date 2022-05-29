# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if self.isEqual(root, subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        
    
    def isEqual(self, root, subRoot):
        if subRoot is None and root is None:
            return True
        if root is None or subRoot is None:
            return False
        if root.val != subRoot.val:
            return False
        return self.isEqual(root.right, subRoot.right) and self.isEqual(root.left, subRoot.left)
        
        