class Solution:
    def isHappy(self, n):
        if n == 1:
            return True
        while n > 10:
            str_n = str(n)
            n = sum(int(i) * int(i) for i in str_n)
        if n == 1:
            return True
        else:
            return False

if __name__ == "__main__":
    l = Solution()
    print(l.isHappy(19))
        