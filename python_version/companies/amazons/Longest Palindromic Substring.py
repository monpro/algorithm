############################ time exceed ###################################
class Solution:
    max_value = -float("Inf")
    result = ""
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        if len(s) == 2 and self.isPalindrome(s):
            return s
        self.helper(s,0, len(s))
        return self.result
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def helper(self,s,left,right):
        if left == right:
            return
        if self.isPalindrome(s[left:right]):
            if right - left + 1 > self.max_value:
                self.max_value = right - left + 1
                self.result = s[left: right]
        self.helper(s, left + 1, right)
        self.helper(s, left, right - 1)
class optimization:
    lower = 0
    maxLen = 0
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        for i in range(len(s) - 1):
            self.helper(s,i,i)
            self.helper(s,i,i+1)
        print(self.lower, self.maxLen)
        return s[self.lower: self.lower + self.maxLen]
    def helper(self, s, j, k):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        if self.maxLen < k - j - 1:
            self.lower = j + 1
            self.maxLen = k - j - 1



if __name__ == "__main__":
    l = optimization()
    print(l.longestPalindrome("ccc"))