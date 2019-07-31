class Solution:
    def restoreIpAddresses(self, s):
        """
        :param s: One long Ip string without .
        """
        result = []
        if len(s) == 0 or len(s) > 12:
            return result
        self.helper(s, "", result, 0)
        return result

    def helper(self, s, temp, result, index):
        if index == 4:
            if len(s) == 0:
                result.append(temp[0: -1])
                return
        if len(s) > 12 - index * 3:
            return
        for k in range(1, 4):
            if len(s) < k:
                continue
            val = s[0: k]
            if int(val) > 255 or len(str(int(val))) != len(val):
                continue
            self.helper(s[k:], temp + s[0:k] + '.', result, index + 1)