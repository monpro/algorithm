class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for i in range(len(S)):
            while len(stack) > 0 and S[i] == ')' and (stack[-1] == '(' or stack[-1].isdigit()):
                temp = 0
                while stack[-1].isdigit():
                    temp += int(stack.pop())
                if temp == 0:
                    stack.pop()
                    stack.append('1')
                    break
                else:
                    stack.pop()
                    stack.append(str(temp * 2))
                    break
            else:
                stack.append(S[i])
        result = 0
        for val in stack:
            result += int(val)
        return result

    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        cur = 0
        for val in S:
            if val == '(':
                stack.append(cur)
                cur = 0
            else:
                cur = stack.pop() + max(2 * cur, 1)
        return cur
