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
        nodes = []
        queue = deque([root])
        while queue:
            levelLen = len(queue)
            for _ in range(levelLen):
                nxt = queue.popleft()
                nodes.append("null" if nxt is None else str(nxt.val))
                if nxt is not None:
                    queue.append(nxt.left)
                    queue.append(nxt.right)
        return ",".join(nodes)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "null":
            return None
        
        nodes = data.split(",")
        nodes = deque(nodes)
        head = TreeNode(int(nodes.popleft()))
        queue = deque([head])
        while queue:
            curr = queue.popleft()
            if nodes:
                left = nodes.popleft()
                curr.left = TreeNode(int(left)) if left != "null" else None
                if curr.left:
                    queue.append(curr.left)
            if nodes:
                right = nodes.popleft()
                curr.right = TreeNode(int(right)) if right != "null" else None
                if curr.right:
                    queue.append(curr.right)
        return head
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))