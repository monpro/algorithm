class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = [i for i in path.split('/') if i != "" and i != "."]
        stack = []
        for i in path:
            if i == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(i)

        return '/' + '/'.join(stack)

if __name__ == "__main__":
    l = Solution()
    print(l.simplifyPath("/a/./b/../../c/"))