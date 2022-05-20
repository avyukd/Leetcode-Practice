# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        memo_ending = {}
        memo_maxpath = {}
        
        def maxPathSumHelper(root):
            if root is None:
                return 0
            if root in memo_maxpath:
                return memo_maxpath[root]
            connected = root.val + maxPathSumEndingAt(root.left) + maxPathSumEndingAt(root.right)
            connectedleft = root.val + maxPathSumEndingAt(root.left) 
            connectedright = root.val + maxPathSumEndingAt(root.right)
            connected = max(connected, connectedleft, connectedright)
            res = max(maxPathSumHelper(root.left), maxPathSumHelper(root.right), connected, root.val)
            memo_maxpath[root] = res
            return res
        
        def maxPathSumEndingAt(root):
            if root is None:
                return 0
            if root in memo_ending:
                return memo_ending[root]
            res = root.val + max(maxPathSumEndingAt(root.left), maxPathSumEndingAt(root.right))
            res = max(root.val, res)
            memo_ending[root] = res
            return res
        
        def checkAllNodesNegative(root):
            if root is None:
                return True
            return root.val < 0 and checkAllNodesNegative(root.right) and checkAllNodesNegative(root.left)
        
        def largestNode(root):
            if root is None:
                return -1001
            return max(root.val, largestNode(root.right), largestNode(root.left))
        
        res = maxPathSumHelper(root)
        if res == 0 and checkAllNodesNegative(root):
            return largestNode(root)
        
        return res
            