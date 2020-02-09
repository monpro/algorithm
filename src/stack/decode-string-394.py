class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, curNum, curString = [], 0, ""
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ""
                curNum = 0
                
            elif c == ']':
                prevNum = stack.pop()
                prevString = stack.pop()
                curString = prevString + prevNum * curString
                
            elif c.isdigit():
                curNum = 10 * curNum + int(c)
                
            else:
                curString += c
        
        return curString
                