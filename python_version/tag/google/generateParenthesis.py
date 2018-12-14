class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        n = 3
                [
                  "((()))",
                  "(()())",
                  "(())()",
                  "()(())",
                  "()()()"
                ]
        """
        if n == 0:
            return []
        result = []
        self.helper(result,"",n)
        return result

    def helper(self,result,substring,n):
        if len(substring) == n * 2 :
            if self.isValid(substring):
                result.append(substring)
            return
        if len([i for i in substring if i == ')']) > len([i for i in substring if i == '(']):
            return
        substring += '('
        self.helper(result,substring,n)
        substring = substring[:-1]
        substring += ')'
        self.helper(result,substring,n)

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
        corresponding_list = ['(',]
        corresponding_dict = {'(':')'}
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
n = 3

l = Solution()

print(l.generateParenthesis(n))