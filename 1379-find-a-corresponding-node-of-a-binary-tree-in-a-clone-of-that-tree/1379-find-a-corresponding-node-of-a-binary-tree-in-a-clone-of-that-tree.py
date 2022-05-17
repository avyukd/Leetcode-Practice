# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def recurse(node):
            if not node:
                return None
            elif node.val == target.val:
                return node
            foundRight = recurse(node.right)
            foundLeft = recurse(node.left)
            return foundLeft if foundLeft else foundRight
        
        return recurse(cloned)