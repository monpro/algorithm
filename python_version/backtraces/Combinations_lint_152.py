class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        if n < k:
            return []
        result = []
        self.helper(result, [], n, k, 1)
        return result
    
    def helper(self, result, subset, n, k, position):
        if k == 0:
            result.append([i for i in subset])
            return
        if position > n:
            return
        for i in range(position, n + 1):
            subset.append(i)
            self.helper(result, subset, n, k - 1, i + 1)
            subset.pop()
