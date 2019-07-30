class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s):
        # write your code here

        left = 0
        right = len(s) - 1
        l = ",./#"
        while left < len(s) and right >= left:
            if s[left] == ' ' or not s[left].isalpha() and not s[left].isdigit():
                left += 1
            if s[right] == ' ' or not s[right].isalpha() and not s[right].isdigit():
                right -= 1

            elif s[left].capitalize() == s[right].capitalize():
                left += 1
                right -= 1
            elif s[left].capitalize() != s[right].capitalize():
                return False

        return True
