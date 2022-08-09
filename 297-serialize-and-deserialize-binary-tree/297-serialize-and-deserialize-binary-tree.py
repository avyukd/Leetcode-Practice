# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        tree = []
        while True:
            level = queue.copy()
            queue = deque([])
            allNullFlag = True
            for node in level:
                if node is None:
                    tree.append("null")
                else:
                    allNullFlag = False
                    tree.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
            if allNullFlag:
                break
        return " ".join(tree)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
                
        tree = data.split(" ")
        if len(tree) == 1:
            return None
        
        tree = [None if node == "null" else int(node) for node in tree]
        
        tree = deque(tree)
        
        i = 0
        root = TreeNode(tree[0])
        tree.popleft()
        queue = deque([root])
        while tree:
            level = queue.copy()
            queue = deque([])
            for node in level:
                if node is not None:
                    if tree:
                        left = tree.popleft()
                        node.left = None if left is None else TreeNode(left)
                        queue.append(node.left)
                    if tree:
                        right = tree.popleft()
                        node.right = None if right is None else TreeNode(right)
                        queue.append(node.right)
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))