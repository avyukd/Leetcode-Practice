# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def depth(root):
            nonlocal diameter
            if root is None:
                return 0
            right, left = depth(root.right), depth(root.left)
            diameter = max(diameter, right + left)
            return max(right, left) + 1
        
        depth(root)
        return diameter