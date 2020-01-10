class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        
        n = len(text)
        for i in range(n // 2):
            # n = 4, left 1, right = 3
            left, right = i + 1, n - i - 1
            if text[:left] == text[right:]:
                return 2 + self.longestDecomposition(text[left:right])
        if n == 0:
            return 0
        else:
            return 1