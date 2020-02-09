class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1
            result += str(sum % 2)
            carry = sum // 2

        if carry != 0:
            result += str(carry)
        return result[::-1]


if __name__ == "__main__":
    l = Solution()
    print(l.addBinary("11","1"))
