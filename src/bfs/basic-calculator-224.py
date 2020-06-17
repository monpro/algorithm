class Solution:
    def calculate(self, s):
        result, num, sign = 0, 0, 1
        stack = []
        for i in s:
            if i >= '0' and i <= '9':
                num = num * 10 + int(i)
            elif i == '+':
                result += num * sign
                num = 0
                sign = 1
            elif i == '-':
                result += num * sign
                num = 0
                sign = -1
            elif i == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif i == ')':
                result += sign * num
                num = 0
                result *= stack.pop()
                result += stack.pop()
        if num != 0:
            result += sign * num
        return result

if __name__ == "__main__":
    l = Solution()
    print(l.calculate('1-2-(3-4)'))
    # print(l.calculate("1+2-(3+4)-5"))
            
        