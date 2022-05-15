# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        if root.right:
            tmp = root.right
            while tmp.left:
                tmp = tmp.left
            if tmp.val <= root.val:
                return False
        if root.left:
            tmp = root.left
            while tmp.right:
                tmp = tmp.right
            if tmp.val >= root.val:
                return False
            
        return self.isValidBST(root.left) and self.isValidBST(root.right)