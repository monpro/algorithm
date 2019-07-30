class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        queue = []
        corresponding_list = ['[','(','{']
        corresponding_dict = {'[':']','(':')','{':'}'}
        for i in s:
            if i in corresponding_list:
                queue.append(i)
            else:
                if len(queue) == 0:
                    return False
                if corresponding_dict[queue[-1]] != i:
                    return False
                else:
                    queue = queue[:-1]

        if len(queue) != 0:
            return False
        return True
text = "}("
l = Solution()

print(l.isValid(text))

