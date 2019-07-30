class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        dp = [0 for _ in range(m + 1)]
        dp[0] = 1
        result = 0
        for i in A:
            for j in range(m, -1, -1):
                if j - i >= 0 and dp[j - i] == 1:
                    dp[j] = 1
                    result = max(j, result)

        return result
