class Solution:
    def calculate(self, s):
        num, sign = 0, '+'
        stack = []
        for i in s:
            if i.isdigit():
                num += num * 10 + int(i)
            elif (not i.isdigit() and i != ' ') or i == s[-1]:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = i
        return sum(stack)
if __name__ == "__main__":
    l = Solution()
    print(l.calculate(' 3/2 '))