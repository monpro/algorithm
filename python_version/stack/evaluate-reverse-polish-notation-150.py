class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        n = len(tokens)
        if n == 0:
            return 0
        operators = '+-*/'
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if token == '+':
                    stack.append(op1 + op2)
                elif token == '-':
                    stack.append(op1 - op2)
                elif token == '*':
                    stack.append(op1 * op2)
                elif token == '/':
                    stack.append(int(float(op1) / op2))
        return stack[0]
        
        
if __name__ == "__main__":
    l = Solution()
    print(int(133 // -132))