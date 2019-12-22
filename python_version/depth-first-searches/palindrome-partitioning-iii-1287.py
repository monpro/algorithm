class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        memo = {}
        n = len(s)

        def cost(s, i, j):
            result = 0
            while i < j:
                if s[i] != s[j]:
                    result += 1
                i += 1
                j -= 1
            return result

        def helper(i, k):
            if (i, k) in memo:
                return memo[(i, k)]
            if k == 1:
                return cost(s, i, n - 1)
            elif k == n - i:
                return 0
            
            result = float("Inf")
            # n - j >= k - 1
            # j <= n - k + 1
            for j in range(i + 1, n - k + 2):
                result = min(result, cost(s, i, j - 1) + helper(j, k - 1))
            memo[(i, k)] = result
            return result
            
        return helper(0, k)