class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        dp = [0 for _ in range(m + 1)]
        dp[0] = 0
        for i in range(len(A)):
            for j in range(m, -1, -1):
                if j - A[i] >= 0:
                    dp[j] = max(dp[j], dp[j - A[i]] + V[i])
        return dp[-1]