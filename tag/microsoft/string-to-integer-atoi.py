class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ans = 0
        num_str = "0123456789"
        if len(str) != 0:
            a = str.lstrip()
            ans_str = ""
            for i in range(0, len(a)):
                if i == 0:
                    if a[i] not in {'-', '+'} and a[i] not in num_str:
                        return 0
                    else:
                        ans_str += a[i]
                else:
                    if a[i] in num_str:
                        ans_str += a[i]
                    else:
                        break
            if len(ans_str) == 0:
                return 0
            if len(ans_str) == 1 and not ans_str.isdigit():
                return 0
            ans = int(ans_str)

            if ans < -2 ** 31:
                ans = -2 ** 31
            elif ans > 2 ** 31 - 1:
                ans = 2 ** 31 - 1
        return ans