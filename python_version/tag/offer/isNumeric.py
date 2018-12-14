# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code her
        if len(s) == 0:
            return False
        sign_flag, decimal_flag, eflag = False,False,False
        for i in range(len(s)):
            if s[i] == 'e' or s[i] == 'E':
                if i == len(s) - 1:
                    return False
                elif eflag:
                    return False
                eflag = True

            elif s[i] == '+' or s[i] == '-':
                if sign_flag and s[i - 1] != 'E' and s[i - 1] != 'e':
                    return False
                if not sign_flag and i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
                sign_flag = True

            elif s[i] == '.':
                if eflag or decimal_flag:
                    return False
                decimal_flag = True

            elif s[i] < '0' or s[i] > '9':
                return False

        return True


