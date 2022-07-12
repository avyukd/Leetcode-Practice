# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        numGood = 0
        stack = deque([(root, -10**5)])
        while stack:
            (node, maxVal) = stack.pop()
            if node.val >= maxVal:
                maxVal = node.val
                numGood += 1
            if node.right:
                stack.append((node.right, maxVal))
            if node.left:
                stack.append((node.left, maxVal))
        return numGood
        