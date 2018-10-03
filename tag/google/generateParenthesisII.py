class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        self.nextLevel(0, 0, [],result,n)
        return result
    def nextLevel(self,left,right,substring,result,n):
        if left == right == n:
            result.append("".join(substring))
            return

        if left < n:
            substring.append('(')
            self.nextLevel(left + 1, right, substring,result,n)
            substring = substring[:-1]

        if right < left:
            substring.append(')')
            self.nextLevel(left,right + 1, substring,result,n)
            substring.pop()

l = Solution()
print(l.generateParenthesis(3))
