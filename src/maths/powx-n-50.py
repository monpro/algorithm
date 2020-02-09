class Solution:
    def myPow(self, x, n):
        
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1/self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)
        
if __name__ == "__main__":
    l = Solution()
    print(round(l.myPow(2.00000, 5),5))
    print(round(3.4123123, 5))