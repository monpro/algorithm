import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return " "
        vals = []

        def preOrder(node):
          if node:
            vals.append(node.val)
            preOrder(node.left)
            preOrder(node.right)
        
        preOrder(root)
        return ' '.join([str(i) for i in vals])
        # return ' '.join(map(str, vals))

      
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == " ":
            return []
        vals = collections.deque(int(val) for val in data.split(" "))

        def build(minVal, maxVal):
          if len(vals) > 0 and minVal < vals[0] and vals[0] <  maxVal:
            val = vals.popleft()
            node = TreeNode(val)
            node.left = build(minVal, val)
            node.right = build(val, maxVal)
            return node
        
        return build(-float('Inf'), float('Inf'))
    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))