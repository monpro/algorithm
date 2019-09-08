class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(n, k, result, [], 1)
        return result

    def helper(self, n, k, result, subset, digit):
        if len(subset) == k:
            result.append([i for i in subset])
            return
        if digit > n:
            return
        for i in range(digit, n + 1):
            subset.append(i)
            self.helper(n, k, result, subset, i + 1)
            subset.pop()