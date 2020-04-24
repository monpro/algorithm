class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if root is None:
            return '{}'
        queue = [root]
        result = []
        while queue != []:
            e = queue.pop(0)
            result.append(e)
            if e is not None:
                queue.append(e.left)
                queue.append(e.right)
        
        serialized_array, serialized_str = result, ""
        
        for i in range(len(serialized_array)):
            if serialized_array[i] == None:
                serialized_str += '#'
            else:
                serialized_str += "{}".format(serialized_array[i].val)
            if i != len(serialized_array) - 1:
                serialized_str += ','
        
        return '{' + serialized_str + '}'
            
    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        if data == '{}':
            return None
            
        #split data
        data = data[1:-1].split(',')
        dummy = TreeNode(-1)
        head = TreeNode(data[0])
        dummy.left = head
        queue = []
        queue.append(head)
        isLeft = True
        index = 0
        for i in range(1,len(data)):
            if data[i] != '#':
                node = TreeNode(data[i])
                if isLeft:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)
            #pass 2 digit, index += 1, consider the structure of binary tree
            if isLeft == False:
                index += 1
            isLeft = not isLeft
        return head
            