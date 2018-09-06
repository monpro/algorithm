# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        if len(s) == 0:
            return s

        result = []
        start_index = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                result.append(s[start_index:i + 1])
                break
            if s[i] == " ":
                result.append(s[start_index:i])
                start_index = i + 1
        final_string = ""
        for i in range(len(result) -1, -1, -1):
            final_string += result[i]
            if i != result[0]:
                final_string += " "
        return final_string


l = Solution()
print(l.ReverseSentence("student. a am I"))


